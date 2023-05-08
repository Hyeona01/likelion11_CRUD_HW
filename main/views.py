from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone

# Create your views here.
def mainpage(request):
    blogs = Blog.objects.all()#blogs 변수에 모든 Blog 객체 저장(모든 게시물 저장)
    return render(request, 'main/mainpage.html',{'blogs':blogs})

def secondpage(request):
    return render(request, 'main/secondpage.html')#render -> 템플릿을 불러옴

def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.pub_date = timezone.now()
    new_blog.body = request.POST['body']
    new_blog.image = request.FILES.get('image')
    new_blog.save()

    return redirect('main:detail', new_blog.id)#redirect -> url로 이동함(detail url이 실행되면서 ditail 함수를 다시 호출! -> main/detail.html render!)

def new(request):
    return render(request, 'main/new.html')

def detail(request, id):
    blog = get_object_or_404(Blog, pk = id)
    return render(request, 'main/detail.html',{'blog':blog})#'blog'는 지정한 변수, :blog는 함수 내에서 전달받은 데이터

def edit(request, id):
    edit_blog = Blog.objects.get(id=id)
    return render(request, 'main/edit.html', {'blog':edit_blog})

def update(request, id):
    update_blog = Blog.objects.get(id=id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']
    update_blog.pub_date = timezone.now()
    update_blog.body = request.POST['body']
    update_blog.image = request.FILES.get('image')
    update_blog.save()
    return redirect('main:detail', update_blog.id)

def delete(request, id):
    delete_blog = Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('main:mainpage')