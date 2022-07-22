from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect


class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        info_dict = request.session.get("info")
        if request.path_info == '/login/' or info_dict:
            return
        else:
            redirect("/login/")
