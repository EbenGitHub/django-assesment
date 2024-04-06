from rest_framework.response import Response
from rest_framework import status
from functools import wraps
from django.http import JsonResponse

def role_required(role):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.role == role:
                return view_func(request, *args, **kwargs)
            else:
                return JsonResponse({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
        return wrapper
    return decorator