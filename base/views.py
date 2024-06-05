from typing import Any
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.generic.edit import UpdateView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView, DestroyAPIView
from rest_framework.renderers import JSONRenderer

from wagtail.api.v2.views import PagesAPIViewSet
from wagtail.api.v2.router import WagtailAPIRouter
# Create your views here.
from home.models import HomePage
from base.selializer import HomePageSerializers

import traceback
import json

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
    
class CustomPageCreateView(APIView):
    '''
        This api create new instance add new row data to the database.
    '''
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        data = request.read()
        data = json.loads(data)
        print(f'printed data = {data}')
        serializer = HomePageSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CustomPageUpdateView(UpdateAPIView):
    '''
        This api update partial part to the row table
    '''
    queryset = HomePage.objects.all()
    serializer_class = HomePageSerializers
    
    def perform_update(self, serializer):
        # return super().perform_update(serializer)
        serializer.save()

class CustomPageDeleteView(DestroyAPIView):
    """
        This api delete blogs pages.
    """
    queryset = HomePage.objects.all()
    serializer_class = HomePageSerializers
    
    # def get_queryset(self):
    #     # return super().get_queryset()
    #     queryset = super().get_queryset()
    #     username = self.request.query_params.get('username', None)
    #     if username is not None:
    #         queryset = queryset.filter(owner__username=username)
    #     return queryset

    
# * Create a api router fro view api using WagtailAPIRouter
api_router = WagtailAPIRouter('wagtailapi')
api_router.register_endpoint("pages", CustomPagesAPIViewSet)