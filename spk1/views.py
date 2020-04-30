from django.shortcuts import render
def index(request):
    context = {
        'title':'SPK',
    }
    return render(request, 'index.html', context)
# Create your views here.
