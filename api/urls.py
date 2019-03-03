from django.views.decorators.csrf import csrf_exempt
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from api.views import GraphQLView, robots


urlpatterns = [
    path('robots.txt', robots, name='robots.txt'),
    path('ping', lambda r: HttpResponse('OK')),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True)), name='graphql'),
    path('graphql', csrf_exempt(GraphQLView.as_view(graphiql=True)), name='graphql'),
    path('admin/', admin.site.urls),
]
