from django.shortcuts import render, redirect
from django.db.models import Max, Min, F
from alternatif.models import alternatif, normalisasi
from alternatif.table import formtabel
def index(request):
    form_input = alternatif.objects.all()
    minc1 = alternatif.objects.aggregate(Min('c1')).get('c1__min')
    minc4 = alternatif.objects.aggregate(Min('c4')).get('c4__min')
    maxc2 = alternatif.objects.aggregate(Max('c2')).get('c2__max')
    maxc3 = alternatif.objects.aggregate(Max('c3')).get('c3__max')
    maxc5 = alternatif.objects.aggregate(Max('c5')).get('c5__max')
    c1norm = alternatif.objects.values_list(F('c1')/minc1, flat=True)
    c2norm = alternatif.objects.values_list(F('c2')/maxc2, flat=True)
    c3norm = alternatif.objects.values_list(F('c3')/maxc3, flat=True)
    c4norm = alternatif.objects.values_list(F('c4')/minc4, flat=True)
    c5norm = alternatif.objects.values_list(F('c5')/maxc5, flat=True)

    c1normbobot = alternatif.objects.values_list(F('c1')/minc1*0.25, flat=True)
    c2normbobot = alternatif.objects.values_list(F('c2')/maxc2*0.15, flat=True)
    c3normbobot = alternatif.objects.values_list(F('c3')/maxc3*0.30, flat=True)
    c4normbobot = alternatif.objects.values_list(F('c4')/minc4*0.25, flat=True)
    c5normbobot = alternatif.objects.values_list(F('c5')/maxc5*0.05, flat=True)

    result = alternatif.objects.all().annotate(prod=F('c1')/minc1*0.25 + 
    F('c2')/maxc2*0.15 + F('c3')/maxc3*0.30 + F('c4')/minc4*0.25 + F('c5')/maxc5*0.05)

    result2 = alternatif.objects.all().values_list(F('c1')/minc1*0.25 + 
    F('c2')/maxc2*0.15 + F('c3')/maxc3*0.30 + F('c4')/minc4*0.25 + F('c5')/maxc5*0.05)
   
    context = {
        'title':'PERHITUNGAN',
        'table':form_input,
        'normc1':c1norm,
        'normc2':c2norm,
        'normc3':c3norm,
        'normc4':c4norm,
        'normc5':c5norm,
        'botc1':c1normbobot,
        'botc2':c2normbobot,
        'botc3':c3normbobot,
        'botc4':c4normbobot,
        'botc5':c5normbobot,
        'hasil':result,
        'hasil2':result2,
    }
    return render(request, 'perhitungan/index.html', context)
def hapus(request, kode):
    tables = alternatif.objects.filter(kodealternatif=kode).delete()
    return redirect('perhitungan:index')
def edit(request, kode):
    editakun = alternatif.objects.get(kodealternatif=kode)
    data={
        'kodealternatif':editakun.kodealternatif,
        'namaalternatif':editakun.namaalternatif,
        'c1':editakun.c1,
        'c2':editakun.c2,
        'c3':editakun.c3,
        'c4':editakun.c4,
        'c5':editakun.c5,
    }
    form_input = formtabel(request.POST or None, initial=data, instance=editakun)
    if request.method == "POST":
        if form_input.is_valid():
            form_input.save()
            return redirect('perhitungan:index')
    context={
        'title':'AKUN|UPDATE',
        'table':form_input,
        'tombol':'Edit',
    }
    return render(request, 'alternatif/index.html', context)
