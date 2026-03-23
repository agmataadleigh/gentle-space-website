from django.contrib.auth.models import User
from django.http import HttpResponse

def create_admin(request):
    if not User.objects.filter(username='zaytka').exists():
        User.objects.create_superuser('zaytka', 'admin@example.com', 'zaytkastrongpassword')
        return HttpResponse("Admin created successfully!")
    return HttpResponse("Admin already exists.")

urlpatterns = [
    path('make-me-admin/', create_admin), # Add this line
    path('admin/', admin.site.urls),
    # ... your other paths
]
