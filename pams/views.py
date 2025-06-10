from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Patient
from .forms import PatientForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Hardcode demo credentials check
        if username == 'demo' and password == 'demo123':
            # Ensure the demo user exists in the database
            user, created = User.objects.get_or_create(
                username='demo',
                defaults={'email': 'shubhanshi652@gmail.com', 'is_active': True, 'is_staff': True, 'is_superuser': True}
            )
            if created:
                user.set_password('demo123')
                user.save()
            elif not user.check_password('demo123'):
                user.set_password('demo123')
                user.save()
            # Log in the user
            login(request, user)
            return redirect('patient_list')
        else:
            error_message = "Invalid username or password. Try demo/demo123."
            return render(request, 'pams/login.html', {'error_message': error_message})
    return render(request, 'pams/login.html')

@login_required
def patient_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        patients = Patient.objects.filter(full_name__icontains=search_query)
    else:
        patients = Patient.objects.all()
    return render(request, 'pams/patient_list.html', {'patients': patients})

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'pams/add_patient.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')