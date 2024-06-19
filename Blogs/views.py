from django.shortcuts import render,HttpResponse
from Blogs.models import Post
# Create your views here.
def blogpage(request):
    allposts = Post.objects.all()
    context = {'allposts':allposts}
    return render(request,'Blogs/blogpage.html',context)

def blogPost(request,slug):
    post = Post.objects.filter(slug = slug)
    context = {"post":post}
    return render(request,'Blogs/blogpost.html',context)