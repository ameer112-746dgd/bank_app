
# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import login, authenticate, logout
# from django.contrib import messages
# from django.core.mail import send_mail
# from .forms import RegistrationForm
# from django.contrib.auth.models import User


# def home(request):
#     return render(request, 'bank_app/home.html')

# def register(request):

#     if request.method == 'POST':
        
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             error = 'this cant work'
#             print(error)
#             username = form.cleaned_data.get('username')
#             email = form.cleaned_data.get('email')
#             password1 = form.cleaned_data.get('password1')

#             user = User.objects.create_user(username=username, email=email, password=password1)
#             login(request, user)
#             messages.success(request, 'Registration successful!')

#             subject = "Welcome to GTBank"
#             message = f"Hi {user.username}, welcome to GTBank! Thank you for registering."
#             from_email = 'atobateleameer204@gmail.com'
#             recipient_list = [user.email]
#             send_mail(subject, message, from_email, recipient_list)


#             return redirect('login')
#         else:
#             messages.error(request, 'Form is invalid. Please correct the errors.')
#     else:
#         form = RegistrationForm()
#     return render(request, 'bank_app/register.html', {'form': form})


# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, 'Login successful! Welcome back.')
#             return redirect('dashboard')
#         else:
#             messages.error(request, 'Invalid username or password')
#     return render(request, 'bank_app/login.html')

# @login_required
# def dashboard(request):
#     return render(request, 'dashboard.html')

# @login_required  # Ensure the user is logged in to access this view
# def logout_view(request):
#     logout(request)
#     messages.success(request, 'You have been logged out successfully.')
#     return redirect('login')




from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.core.mail import send_mail
from .forms import RegistrationForm
from django.contrib.auth.models import User

def home(request):
    return render(request, 'bank_app/home.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')

            # Create the new user
            user = User.objects.create_user(username=username, email=email, password=password1)
            login(request, user)
            messages.success(request, 'Registration successful!')

            # Send registration email
            subject = "Welcome to GTBank"
            message = f"Hi {user.username}, welcome to GTBank! Thank you for registering."
            from_email = 'atobateleameer204@gmail.com'
            recipient_list = [user.email]
            try:
                send_mail(subject, message, from_email, recipient_list)
            except Exception as e:
                messages.error(request, f"Error sending email: {e}")

            return redirect('login')
        else:
            print("Form errors:", form.errors)  # Debug message
            messages.error(request, 'Form is invalid. Please correct the errors.')
    else:
        form = RegistrationForm()
    return render(request, 'bank_app/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful! Welcome back.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'bank_app/login.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')




