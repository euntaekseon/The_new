from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from .models import Post

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
import json

from account.models import CustomUser

def board(request):
    posts = Post.objects.order_by('-id')
    return render(request, 'board.html', {'posts': posts})

def creating(request):
    return render(request, 'creating.html')

def about(request):
    return render(request, 'about.html')

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post': post_detail})

def postcreate(request):
    post = Post()
    post.user = request.user
    post.title = request.GET['title']
    post.goal = request.GET['goal']
    post.body = request.GET['body']
    post.pub_date = timezone.datetime.now()
    post.keyword = request.GET['keyword']
    post.save()
    return redirect('/cratecommunity/detail/' + str(post.id))
    # 디테일페이지 먼저 추가하고, 게시글 작성하는 템플릿 완성
     
def like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.like_users.all():
        #좋아요 취소
        post.like_users.remove(request.user)
    else:
        post.like_users.add(request.user)
    return redirect('/cratecommunity/detail/' + str(post.id))

def mypage(request,user_id):  
    user = CustomUser.objects.get(id = user_id)
    postsave = user.like_posts.all()
    context={
        "postsave":postsave,
    }
    return render(request, 'mypage.html',context)