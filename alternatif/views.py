from django.shortcuts import render, redirect
from .table import formtabel
from django.db.models import Max, Min, F
from .models import alternatif, normalisasi
def index(request):
    form_input = formtabel(request.POST or None)
    if form_input.is_valid():
        form_input.save()
        return redirect('alternatif:index')
    context = {
        'title':'ALTERNATIF',
        'table':form_input,
        'tombol':'Tambahkan'
    }
    return render(request, 'alternatif/index.html', context)
