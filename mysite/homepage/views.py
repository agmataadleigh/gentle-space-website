from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Post
from .forms import GratitudeForm

def home(request):
    # 1. AUTO-ADMIN CREATOR
    if not User.objects.filter(username='zaytka').exists():
        User.objects.create_superuser('zaytka', 'admin@example.com', 'zaytkastrongpassword')

    # 2. GET ALL POSTS
    posts = Post.objects.all().order_by('-created_at')
    
    # 3. HANDLE FORM SUBMISSION
    if request.method == 'POST':
        form = GratitudeForm(request.POST)
        if form.is_valid():
            form.save()
            # This redirect triggers the 'Welcome Screen' to show the quote!
            return redirect('/?submitted=true') 
    else:
        form = GratitudeForm()

    return render(request, 'home.html', {'posts': posts, 'form': form})

def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.likes += 1
    post.save()
    return redirect('/')

def delete_post(request, post_id):
    # This makes the trash can icon work
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('/')