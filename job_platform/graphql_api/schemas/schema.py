import graphene
from .job_scheme import JobQuery, CreateJob


class Query(JobQuery, graphene.ObjectType):
    pass


class JobMutation(graphene.ObjectType):
    create_job = CreateJob.Field()


class Mutation(JobMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)