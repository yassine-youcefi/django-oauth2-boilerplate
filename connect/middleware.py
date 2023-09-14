from django.urls import resolve
from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse



class UserAuthenticationMiddleware(MiddlewareMixin):

    def __init__(self, get_response):
        self.get_response = get_response
        self.allowed_apps = ['admin']

    def process_view(self, request, view_func, view_args, view_kwargs):
        
        
        print('request.user.is_authenticated ',request.user.is_authenticated)
        if(request.user.is_authenticated):

            # if request.user.is_superuser:
            #     return None
                
            url_name = resolve(request.path_info).url_name
            app_name = resolve(request.path_info).app_name

            if not app_name in self.allowed_apps:
                print(request.user.has_permission(url_name))
                
                if not request.user.has_permission(url_name):
                    return JsonResponse({"Detail": "You are not allowed to access this functionality"}, status=403)  
            
            return None
