from django.http import JsonResponse
from functools import wraps
from django.conf import settings

def admin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        token = request.headers.get('Authorization')
        if token == settings.ADMIN_TOKEN:
            return view_func(request, *args, **kwargs)
        return JsonResponse({'error': 'Unauthorized'}, status=401)
    return _wrapped_view
