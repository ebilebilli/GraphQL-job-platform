import graphene
from .job_scheme import JobQuery


class Query(JobQuery, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)