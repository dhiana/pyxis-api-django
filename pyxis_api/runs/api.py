from tastypie.resources import ModelResource
from runs.models import Run


class RunResource(ModelResource):
    class Meta:
        queryset = Run.objects.all()
        resource_name = 'runs'
        collection_name = 'runs'
