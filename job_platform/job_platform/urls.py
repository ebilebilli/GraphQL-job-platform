from django.contrib import admin
from django.urls import path, include
from django.urls import path
from graphql_jwt.decorators import jwt_cookie
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from graphql_api.schemas.schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', csrf_exempt(jwt_cookie(GraphQLView.as_view(graphiql=True, schema=schema)))),
]
