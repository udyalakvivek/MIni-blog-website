from django.conf import settings

class SeparateAdminSessionMiddleware:
    def __init__(self , get_response):
        self.get_response = get_response
        
        
    def __call__(self, request):
        if request.path.startswith('/admin'):
            settings.SESSION_COOKIE_NAME = "admin_sessionid"
        else:
            settings.SESSION_COOKIE_NAME = "website_sessionid"
        return self.get_response(request)