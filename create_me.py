import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings') # Change 'mysite' if your folder name is different
django.setup()

from django.contrib.auth.models import User

if not User.objects.filter(username='zaytka').exists():
    User.objects.create_superuser('zaytka', 'admin@example.com', 'zaytkastrongpassword')
    print("ADMIN CREATED SUCCESSFULLY!")
else:
    print("ADMIN ALREADY EXISTS!")