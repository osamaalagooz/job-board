from django.shortcuts import render
from .models import Post, Comment, Category, CommentReply
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def post_list_view(request, id=None):
    
    if id:
        category = Category.objects.get(id=id)
        posts = category.posts
    else:    
        posts =  Post.published.all()

    categories = Category.objects.all()
    paginator = Paginator(posts, 1)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)  
    except EmptyPage:
        posts  = paginator.page(paginator.num_pages)     

    return render(request, 'posts_list.html', {'posts': posts, 'categories': categories})

# def post_category_list(request, id):

#     category = Category.objects.get(id=id)

#     posts = category.posts

#     re
