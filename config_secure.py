import os

# PayliteNG configuration — SECURE VERSION
# All credentials loaded from environment variables
# This file is SAFE to commit to Git

DATABASE_HOST = os.environ.get('DB_HOST', 'localhost')
DATABASE_PORT = int(os.environ.get('DB_PORT', '3306'))
DATABASE_USER = os.environ.get('DB_USER')
DATABASE_PASS = os.environ.get('DB_PASS')  # no default — must be set
DATABASE_NAME = os.environ.get('DB_NAME')

# Payment gateway
FLUTTERWAVE_SECRET = os.environ.get('FLUTTERWAVE_SECRET')
PAYSTACK_SECRET_KEY = os.environ.get('PAYSTACK_SECRET_KEY')

# AWS credentials
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_BUCKET_NAME = os.environ.get('AWS_BUCKET_NAME')

# Application settings
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')
