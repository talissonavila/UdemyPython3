from tkinter import NO
from django.shortcuts import render
from django.http import HttpRequest, Http404
from blog.data import posts

from typing import Any

def blog(request):
    print('blog')

    context = {
        'text': 'Welcome to /blog page',
        'posts': posts
        
    }

    return render(request=request, template_name='blog/index.html',
    context=context
                  )


def exemplo(request):
    print('blog / exemplo')

    context = {
        'text': 'welcome to /blog/examplo page'
    }

    return render(request=request, template_name='blog/exemplo.html',
    context=context
                )


def post(request: HttpRequest, post_id: int):
    found_post: dict [str, Any] | None = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break
    
    if found_post is None:
        raise Http404("Post doesn't exists.")
    
    context = {
        'post': found_post,
        'title': found_post['title'] + ' - '
    }

    return render(
        request=request, template_name='blog/post.html',context=context
    )