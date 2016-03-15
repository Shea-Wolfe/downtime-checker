from django.shortcuts import render
from .forms import URLForm
from requests import get
# Create your views here.

def status_view(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            status = get(request.POST["url"]).status_code
            return render(request, 'checker/status.html', {'url':request.POST["url"],
                                                      'status': status})
    else:
        form = URLForm()
    return render(request, 'checker/url_entry.html', {'form': form})
