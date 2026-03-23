from django.contrib.auth.models import User # Add this import at the very top

def home(request):
    # --- AUTO-ADMIN CREATOR START ---
    if not User.objects.filter(username='zaytka').exists():
        User.objects.create_superuser('zaytka', 'admin@example.com', 'zaytkastrongpassword')
    # --- AUTO-ADMIN CREATOR END ---

    posts = Post.objects.all().order_by('-created_at')
    if request.method == 'POST':
        form = GratitudeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/?submitted=true')
    else:
        form = GratitudeForm()
    return render(request, 'home.html', {'posts': posts, 'form': form})
    