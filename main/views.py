from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone

# Create your views here.
def mainpage(request):
    blogs = Blog.objects.all()#blogs 변수에 모든 Blog 객체 저장(모든 게시물 저장)
    return render(request, 'main/mainpage.html',{'blogs':blogs})

def secondpage(request):
    return render(request, 'main/secondpage.html')

def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.pub_date = timezone.now()
    new_blog.body = request.POST['body']

    new_blog.save()

    return redirect('detail', new_blog.id)#여기서 detail은 뭘까?

def new(request):#어디에서 호출되는지?
    return render(request, 'main/new.html')

def detail(request, id):
    blog = get_object_or_404(Blog, pk = id)
    return render(request, 'main/detail.html',{'blog':blog})#중괄호 안에 blog는 뭘까