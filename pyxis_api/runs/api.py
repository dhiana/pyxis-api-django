from tastypie.resources import ModelResource
from tastypie import fields
from runs.models import Run


class RunResource(ModelResource):
    success_percentage = fields.IntegerField(attribute='success_percentage', readonly=True)

    class Meta:
        queryset = Run.objects.all()
        resource_name = 'runs'
        collection_name = 'runs'
