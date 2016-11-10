from django.shortcuts import render
from posts.models import Post
# Create your views here.

#def posts(request):
#    return render(request, 'posts.html',{})

def posts(request):

	posts = Post.objects.all()

	return render(request, 'posts.html',{'posts':posts})

def post(request, id_post):

	post = Post.objects.filter(id=id_post).get()

	return render(request, 'post.html',{'post':post})