from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):

    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('SETTINGS:main_dashboard')
        else:
            return view_func(request, *args, **kwargs)
    
    return wrapper_func
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
def allowed_users(allowed_departments=[]):

    def deceorator(view_func):

        def wrapper_func(request, *args, **kwargs):

            group = None

            if request.user.groups.exists():
                groups = request.user.groups.all().order_by('-name')
                for group in groups:
                    if group.name in allowed_departments:
                        return view_func(request, *args, **kwargs)
                    else:
                        return redirect('SETTINGS:unauthorized')
            else:
                return redirect('SETTINGS:unassigned_roles')

            # Original algorithm from Dennis Ivy(Youtube)
            # if request.user.groups.exists():
            #     group = request.user.groups.all()[0].name

            # if group in allowed_departments:
            #     return view_func(request, *args, **kwargs)
            # else:
            #     return redirect('SETTINGS:unauthorized')

        return wrapper_func

    return deceorator
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
