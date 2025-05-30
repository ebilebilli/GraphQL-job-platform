import graphene
from graphene_django.types import DjangoObjectType

from jobs.models.job_model import Job


class JobType(DjangoObjectType):
    class Meta:
        model = Job
        fields = '__all__'


class JobQuery(graphene.ObjectType):
    all_jobs = graphene.List(JobType)

    def resolve_all_jobs(self, info):
        return Job.objects.all()