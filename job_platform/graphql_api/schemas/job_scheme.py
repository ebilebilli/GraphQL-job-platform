import graphene
from graphene_django.types import DjangoObjectType
from django.core.exceptions import ValidationError, ObjectDoesNotExist

from jobs.models.job_model import Job
from .user_schema import UserType


class JobType(DjangoObjectType):
    employer = graphene.Field(UserType) 
    class Meta:
        model = Job
        fields = '__all__'


class JobQuery(graphene.ObjectType):
    all_jobs = graphene.List(JobType)
    job = graphene.Field(JobType, id=graphene.ID(required=True))
    jobs_by_user = graphene.List(JobType, employer_id=graphene.ID(required=True) )

    def resolve_all_jobs(self, info):
        return Job.objects.all()
    
    def resolve_job(self, info, id):
        try:
            return Job.objects.get(id=id)
        except ObjectDoesNotExist:
            raise ValidationError({'error': 'Jobs not found'})
            

    def resolve_jobs_by_user(self, info, employer_id):
        return Job.objects.filter(employer_id=employer_id)
  