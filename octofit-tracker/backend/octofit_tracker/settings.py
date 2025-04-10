# Add MongoDB database connection
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_db',
        'HOST': 'localhost',
        'PORT': 27017,
    }
}

# Enable CORS
INSTALLED_APPS += [
    'corsheaders',
]
MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_METHODS = [
    'GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'
]
CORS_ALLOW_HEADERS = [
    'content-type', 'authorization', 'x-csrftoken', 'x-requested-with'
]

# Allow all hosts
ALLOWED_HOSTS = ['*']