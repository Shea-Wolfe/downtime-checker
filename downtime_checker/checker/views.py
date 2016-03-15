from django.shortcuts import render
from .forms import URLForm
from requests import get
# Create your views here.

def Status_View(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            status = get(form.url).status_code
            return render(request, 'checker/status', {'url':form.url,
                                                      'status': status})
