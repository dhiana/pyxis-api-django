from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse
from runs.api import RunResource


run_resource = RunResource()

urlpatterns = [
    url(r'^', include(run_resource.urls)),
]
