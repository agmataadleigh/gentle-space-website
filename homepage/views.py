from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import GratitudeForm

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    if request.method == 'POST':
        form = GratitudeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/?submitted=true')
    else:
        form = GratitudeForm()
    return render(request, 'home.html', {'posts': posts, 'form': form})

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('/')

def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.likes += 1
    post.save()
    return redirect('/')