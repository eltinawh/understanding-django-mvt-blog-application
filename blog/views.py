# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from blog.models import Post
from blog.forms import PostForm

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'post_list': posts})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('home')
    else:
        form = PostForm()  
    return render(request, 'post_form.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.author:
        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'post_form.html', {'form': form})
    return HttpResponseForbidden("Access denied: You can only edit your own posts!")

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.author:
        if request.method == 'POST':
            post.delete()
            return redirect('home')
        else:
            return render(request, 'post_delete.html', {'post': post})
    return HttpResponseForbidden("Access denied: You can only delete your own posts!")