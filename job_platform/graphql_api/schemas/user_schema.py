import graphene
from graphene_django.types import DjangoObjectType
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from graphql import GraphQLError
from graphql_jwt.shortcuts import get_token

from users.models import CustomerUser

__all__ = ['UserType', 'UserQuery', 'UserRegister'  
]


User = get_user_model()


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class UserQuery(graphene.ObjectType):
    all_employers = graphene.List(UserType)
    user = graphene.Field(UserType, id=graphene.ID(required=True))

    def resolve_all_employers(self, info):
        return User.objects.all()
    
    def resolve_user(self, info, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            raise ValidationError({'error': 'User not found'})


class UserRegister(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        full_name = graphene.String(required=True)
        phone_number = graphene.String(required=True)
        birthday = graphene.Date(required=True)
        gender = graphene.String(required=True)
    
    user = graphene.Field(UserType)
    token = graphene.String()

    def mutate(self, info, username, email, password, full_name, phone_number, birthday, gender):
        if User.objects.filter(email=email).exists():
            raise ValidationError({'error': 'This email already registered'})
        
        user = User(
            username=username,
            email=email,
            full_name=full_name,
            phone_number=phone_number,
            birthday=birthday,
            gender=gender,
        )
        user.set_password(password)
        user.save()
        token = get_token(user)
        return UserRegister(user=user, token=token)
