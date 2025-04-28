from django.urls import path
from views import PostView

urlpatterns = [
    # path('', views.index, name='name'),
    path('', PostView.as_view(), name="post-view"),
]
