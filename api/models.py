from django.db import models
from tastypie.resources import ModelResource
from movies.models import Movie


class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        # this name is for /api/this_name
        resource_name = 'movies'
        excludes = ['date_created', ]
