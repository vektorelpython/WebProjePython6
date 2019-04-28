from django.shortcuts import render,get_object_or_404,redirect
from .models import Gonderi
from .forms import GonderiForm
from django.utils import timezone
from django.contrib.auth.models import User

def gonderi_liste(request):
    Gonderiler = Gonderi.objects.all()
    return render(request, 'EdizBlog/gonderi_liste.html', {'Gonderis':Gonderiler})


def gonderi_detay(request,pk):
    yazi = get_object_or_404(Gonderi,pk=pk)
    return render(request, 'EdizBlog/gonderi_detay.html', {'gonderi':yazi})

def yeni_gonderi(request):
    if request.method == "POST":
        form = GonderiForm(request.POST)
        if form.is_valid():
            gonderi = form.save(commit=False)
            # ben = User.objects.get(username="edizadmin")
            gonderi.yazar = request.user
            gonderi.yayim_zaman = timezone.now()
            gonderi.save()
            return redirect('gonderi_detay', pk=gonderi.pk)
    else:
        form = GonderiForm()
    return render(request, 'EdizBlog/gonderi_duzenle.html', {'form': form})

def gonderi_duzenle(request, pk):
    gonderi = get_object_or_404(Gonderi, pk=pk)
    if request.method == "POST":
        form = GonderiForm(request.POST, instance=gonderi)
        if form.is_valid():
            gonderi = form.save(commit=False)
            gonderi.yazar = request.user
            gonderi.yayim_zaman = timezone.now()
            gonderi.save()
            return redirect('gonderi_detay', pk=gonderi.pk)
    else:
        form = GonderiForm(instance=gonderi)
    return render(request, 'EdizBlog/gonderi_duzenle.html', {'form': form})