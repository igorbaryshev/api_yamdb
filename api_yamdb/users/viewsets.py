from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class CreateViewSet(mixins.CreateModelMixin,
                    GenericViewSet):
    """
    A viewset that provides default `create()` action.
    """
    pass
