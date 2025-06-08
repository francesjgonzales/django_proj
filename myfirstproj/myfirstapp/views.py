from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ReservationForm
from .models import MenuItem, Reservation, Menu

# Create your views here.
def index(request):
    return render(request, 'index.html')

def book(request):
    form = ReservationForm()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Reservation saved successfully!')
    return render(request, 'reserve.html', {'form': form})

def menu(request):
    menu_data = Menu.objects.all()
    return render(request, 'menu.html', {'menu': menu_data})

def about(request):
    return render(request, 'about.html')

def contact(request):   
    return render(request, 'contact.html')

def services(request):              
    return render(request, 'services.html')

def reservation(request):              
    return render(request, 'reservation.html')


# Create class based views
class MyView(View):
    def get(self, request):
        return HttpResponse('This is a class-based view')