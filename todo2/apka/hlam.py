from django.shortcuts import render

def log(f):
    def wrap(request,*args, **kwargs):
        if not request.user.is_authenticated() or not request.user.is_active:
            return render(request, 'apka/signin.html')
        return f(request,*args, **kwargs)
    return wrap