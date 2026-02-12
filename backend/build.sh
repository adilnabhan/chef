#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py migrate --noinput
python manage.py collectstatic --noinput

echo "Creating admin user..."

python manage.py shell <<EOF
from django.contrib.auth import get_user_model
import os

User = get_user_model()

username = os.environ.get("DJANGO_ADMIN_USERNAME", "admin")
password = os.environ.get("DJANGO_ADMIN_PASSWORD", "admin123")
email = os.environ.get("DJANGO_ADMIN_EMAIL", "admin@example.com")

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print("SUPERUSER CREATED")
else:
    print("SUPERUSER EXISTS")
EOF
