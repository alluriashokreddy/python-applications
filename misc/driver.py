import os
import django
import sys
sys.path.append('D:\\Workspace\\Django_rest\\app')
print(sys.path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()
from core.models import User
users = User.objects.all()
print(users)