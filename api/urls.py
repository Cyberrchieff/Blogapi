from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='name'),
    path('', PostView.as_view(), name="post-view"),
]
