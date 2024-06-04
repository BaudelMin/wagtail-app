from django.shortcuts import render
from wagtail.api.v2.views import PagesAPIViewSet
from wagtail.api.v2.router import WagtailAPIRouter
# Create your views here.
from rest_framework.renderers import JSONRenderer

# ...

class BlogPagesAPIViewSet(PagesAPIViewSet):
    renderer_classes = [JSONRenderer]
    name = "pages"

api_router = WagtailAPIRouter('wagtailapi')
api_router.register_endpoint("pages", BlogPagesAPIViewSet)