from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import RegistrationForm
from .models import Department
from .models import ContactSubmission
from .forms import ContactForm



def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('confirmation')  
    else:
        form = RegistrationForm()  

    context = {
        'form': form
    }
    return render(request, 'registration.html', context)

def confirmation(request):
    return render(request, 'confirmation.html')

def department(request):
    dict_dept = {
        'dept': Department.objects.all()
    }
    return render(request, 'Department.html', dict_dept)

def department_detail(request, pk):
    department = Department.objects.get(pk=pk)
    return render(request, 'department_detail.html', {'department': department, 'pk': pk})


def biology_view(request):
    try:
        department = Department.objects.get(name='Biology')
    except Department.DoesNotExist:
        department = None
    
    return render(request, 'biology.html', {'department': department})


def business_administration_view(request, pk):  # Change dept_id to pk
    # Retrieve the department object based on the pk
    department = Department.objects.get(pk=pk)
    return render(request, 'business_administration.html', {'department': department})


def computer_science_view(request, dept_id):
    # Retrieve the department object based on the dept_id
    department = Department.objects.get(pk=dept_id)
    return render(request, 'computer_science.html', {'department': department})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('complaint_confirmation')  
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def complaint_confirmation(request):
    return render(request, 'complaint_confirmation.html')