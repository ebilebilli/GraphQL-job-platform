import graphql_jwt
import graphene
from .job_scheme import *
from .user_schema import *


class Query(JobQuery, UserQuery, graphene.ObjectType):
    pass


class JobMutation(graphene.ObjectType):
    create_job = CreateJob.Field()
    update_job = UpdateJob.Field()
    delete_job = DeleteJob.Field()


class UserMutation(graphene.ObjectType):
    user_register = UserRegister.Field()


class Mutation(JobMutation, UserMutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)