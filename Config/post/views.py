from django.shortcuts import render
from .models import *
# Create your views here.

# def post(request):
#     post = {
#         "posts": ["Man kecha ameriakga bordim", "Python juda yaxshi dasturlash tili", "Django o'rganish uchun oson"]
#     }
#     return render(request, 'post.html', context=post)


def post(request):
    posts = Post.objects.all() 
    return render(request, 'post.html', {"posts": posts})
