from django.shortcuts import render
from wagtail.api.v2.views import PagesAPIViewSet
from wagtail.api.v2.router import WagtailAPIRouter
# Create your views here.
from home.models import HomePage
from rest_framework.renderers import JSONRenderer

# ...

class CustomPagesAPIViewSet(PagesAPIViewSet):
    """
    Create API view class from PagesAPIViewSet.
    
    Class attributes:
    model : Model Class (model to read in the database)
    name : string (provide name for Model)
    """
    renderer_classes = [JSONRenderer]
    model = HomePage
    name = "pages"
    
    
# * Create a api router fro view api using WagtailAPIRouter
api_router = WagtailAPIRouter('wagtailapi')
api_router.register_endpoint("pages", CustomPagesAPIViewSet)