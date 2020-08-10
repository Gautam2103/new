from django.shortcuts import render, redirect
from travelservices.forms import TravelservicesForm
from travelservices.models import Travelservices
# Create your views here.
def emp(request):
    if request.method == "POST":
        form = TravelservicesForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = TravelservicesForm()
    return render(request,'index.html',{'form':form})
def show(request):
    travelservices = Travelservices.objects.all()
    return render(request,"show.html",{'travelservices':travelservices})
def edit(request, id):
    travelservices = Travelservices.objects.get(id=id)
    return render(request,'edit.html', {'travelservices':travelservices})
def update(request, id):
    travelservices = Travelservices.objects.get(id=id)
    form = TravelservicesForm(request.POST, instance = travelservices)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'travelservices': travelservices})
def destroy(request, id):
    travelservices = Travelservices.objects.get(id=id)
    travelservices.delete()
    return redirect("/show")
def tra(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def blog(request):
    return render(request,'blog.html')
def contact(request):
    return render(request,'contact.html')
def contact_process(request):
    return render(request,'contact_process.php')
def destination_details(request):
    return render(request,'destination_details.html')
def elements(request):
    return render(request,'elements.html')

def singleblog(request):
    return render(request,'singleblog.html')
def travel_destination(request):
    return render(request,'travel_destination.html')
