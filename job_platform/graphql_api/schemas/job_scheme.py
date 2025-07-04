import graphene
from graphene_django.types import DjangoObjectType
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.db.models import Q

from jobs.models.job_model import Job
from .user_schema import UserType


__all__ = ['JobType', 'JobQuery', 'CreateJob', 'UpdateJob',
           'DeleteJob',
           
]


class JobType(DjangoObjectType):
    employer = graphene.Field(UserType) 
    class Meta:
        model = Job
        fields = '__all__'


class JobQuery(graphene.ObjectType):
    all_jobs = graphene.List(JobType)
    job = graphene.Field(JobType, id=graphene.ID(required=True))
    jobs_by_employer = graphene.List(JobType, employer_id=graphene.ID(required=True) )
    search_jobs = graphene.List(JobType, keyword=graphene.String(required=True))

    def resolve_all_jobs(self, info):
        return Job.objects.filter(is_active=True)
    
    def resolve_job(self, info, id):
        try:
            return Job.objects.get(id=id, is_active=True)
        except ObjectDoesNotExist:
            raise ValidationError({'error': 'Job not found'})
            
    def resolve_jobs_by_employer(self, info, employer_id):
        return Job.objects.filter(employer_id=employer_id)
    
    def resolve_serch_jobs(self, info, keyword):
        return Job.objects.filter(
            Q(title__icontains=keyword) |
            Q(company__icontains=keyword) |
            Q(location__icontains=keyword) 
        )


class CreateJob(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        salaryMin = graphene.Int(required=True)
        salaryMax = graphene.Int(required=True)
    
    job = graphene.Field(JobType)

    def mutate(self, info, title, description, salaryMin, salaryMax):
        user = info.context.user
        if user.is_anonymous:
            raise ValidationError({'error': 'Authentication required'})

        job = Job.objects.create(
            title=title,
            description=description,
            salary_min=salaryMin,
            salary_max=salaryMax,
            employer=user
        )
        return CreateJob(job=job)


class UpdateJob(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String()
        description = graphene.String()
        salaryMin = graphene.Int()
        salaryMax = graphene.Int()

    job = graphene.Field(JobType)

    def mutate(self, info, id, title=None, description=None, salaryMin=None, salaryMax=None):
        user = info.context.user
        if user.is_anonymous:
            raise ValidationError({'error': 'Authentication required'})
        
        job = Job.objects.get(id=id)
        if job.employer != user:
            raise ValidationError({'error': 'You do not have permission'})
        
        if title is not None:
            job.title = title

        if description is not None:
            job.description = description
        
        if salaryMin is not None:
            job.salary_min = salaryMin
        
        if salaryMax is not None:
            job.salary_max = salaryMax
        
        job.save()

        return UpdateJob(job=job)


class DeleteJob(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()

    def mutate(self, info, id):
        user = info.context.user
        if user.is_anonymous:
            raise ValidationError({'error': 'Authentication required'})

        job = Job.objects.get(id=id)
        if job.employer != user:
            raise ValidationError({'error': 'You do not have permission'})
        
        job.delete()
        return (DeleteJob(ok=True))


        