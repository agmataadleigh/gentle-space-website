from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from django.http import HttpResponse

# This is the "Magic" function that creates your admin account
def create_admin(request):
    if not User.objects.filter(username='zaytka').exists():
        User.objects.create_superuser('zaytka', 'admin@example.com', 'zaytkastrongpassword')
        return HttpResponse("<h1>Success! Admin account 'zaytka' created.</h1>")
    return HttpResponse("<h1>Admin 'zaytka' already exists.</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('make-me-admin/', create_admin), # This is the secret link
    path('', include('base.urls')), # Or whatever your main app is called
]
