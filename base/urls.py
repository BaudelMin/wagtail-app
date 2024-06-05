from django.urls import path, include
from .views import api_router, CustomPageCreateView, CustomPageUpdateView, CustomPageDeleteView

urlpatterns = [
    # ... your other url patterns ...
    path('v2/', api_router.urls, name='pages'),
    path('create', CustomPageCreateView.as_view()),
    path('update/<int:pk>', CustomPageUpdateView.as_view()),
    path('delete/<int:pk>', CustomPageDeleteView.as_view())
]
