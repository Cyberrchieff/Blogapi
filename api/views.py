from django.shortcuts import render
from rest_framework import generics
from .serializers import PostSerializer
from .models import Post

# Create your views here.
# def index(request):
#     return render(request, 'index.html')

class PostView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializers_class = PostSerializer
