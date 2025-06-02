from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ReservationForm

# Create your views here.
def index(request):
    form = ReservationForm()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Reservation saved successfully!')
    return render(request, 'index.html', {'form': form})
def about(request):
    return render(request, '/about.html')
def contact(request):   
    return render(request, '/contact.html')
def services(request):              
    return render(request, '/services.html')


# Create class based views
class MyView(View):
    def get(self, request):
        return HttpResponse('This is a class-based view')