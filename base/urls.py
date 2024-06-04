from django.urls import path, include
from .views import api_router

urlpatterns = [
    # ... your other url patterns ...
    path('v2/', api_router.urls, name='pages'),
]
