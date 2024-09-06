from django.shortcuts import render
from .models import Post , Comment 
from django.db.models import Count
# Create your views here.

# 
def test1(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()
    context = {'posts': posts, 'comments': comments}
    # 2 queries here and len(comments) queries in template
    return render(request,'test1.html' , context=context)

def test2(request):
    posts = Post.objects.all()
    context = {'posts': posts,}
    # 1 queries here and len(posts) queries in template
    return render(request,'test2.html' , context=context)


def test3(request):
    posts = Post.objects.all().prefetch_related('comments')
    context = {'posts': posts,}
    # 1 queries here and len(posts) queries in template
    # or
    # 2 queries here and 0 in template if prefetch_related('comments')
    return render(request,'test3.html' , context=context)



def test4(request):
    posts = Post.objects.get_posts_with_comments()  # type: ignore
    context = {'posts': posts}
    # 2 queries here and 0 in template
    return render(request, 'test4.html', context=context)

def test5(request):
    
    # 0 queries here and 2 in template
    return render(request, 'test5.html', )


def test6(request):
    
    # 0 queries here and 2 in template
    return render(request, 'test6.html', )