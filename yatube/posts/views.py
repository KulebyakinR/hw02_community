from django.shortcuts import get_object_or_404, render

from .models import Group, Post

POST_LIMIT = 10


def index(request):
    posts = Post.objects.order_by('-pub_date')[:POST_LIMIT]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_list(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:POST_LIMIT]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
