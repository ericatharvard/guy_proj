from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from tastypie import fields
from guy.models import Guy
from position.models import Position

class PositionResource(ModelResource):
    class Meta:
        queryset = Position.objects.all()
        resource_name = 'position'

class GuyResource(ModelResource):
    position = fields.ForeignKey(PositionResource, 'position')

    class Meta:
        queryset = Guy.objects.all()
        resource_name = 'guy'
        authorization= Authorization()
