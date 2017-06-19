from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def start(request):
    if not request.user.is_authenticated() or  not request.user.is_active:
        return render(request, 'apka/sing.html')
    return render(request,'apka/base.html')
