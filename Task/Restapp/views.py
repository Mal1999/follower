from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from .forms import RegisterForm, StudentForm, LoginForm

def home_view(request):
    return render(request, 'home.html')

def department_view(request, department_name):
    # Assuming you have a function to generate Wikipedia links based on department names
    wikipedia_link = generate_wikipedia_link(department_name)

    context = {
        'department': department_name,
        'wikipedia_link': wikipedia_link,
    }

    return render(request, 'department_view.html', context)

def generate_wikipedia_link(department_name):
    # Implement your logic to generate Wikipedia link based on the department name
    # Example: Constructing a simple link with department name in the URL
    return f"https://en.wikipedia.org/wiki/{department_name}"

def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(request)
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {"error": "Invalid user or pass,"}
            return render(request, "login.html", context)
        login(request, user)
        return redirect("Restapp:new_page")
    else:
        form = AuthenticationForm(request)
    return render(request, "login.html",{})

def new_page(request):
    return render(request, 'new_page.html')

def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect('Restapp:login_view')
    context = {"form": form}
    return render(request, 'register.html', context)

def form_page(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # Save the form data
            order_instance = form.save()

            # Custom logic - print order details to the console
            print(f"Order Confirmed - Order ID: {order_instance.id}, Details: {order_instance}")

            # Display a success message to the user
            messages.success(request, 'Order Confirmed')

            # Redirect to the home page
            return redirect('Restapp:form_confirm')
    else:
        form = StudentForm()

    return render(request, 'form.html', {'form': form})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("Restapp:login_view")
    return render(request, "logout.html", {})

def submit_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Restapp:form_confirm')
    else:
        form = StudentForm()
    return render(request, 'form_submitted.html', {'form': form})


def form_confirm(request, message):
    # Your logic here

    return render(request, 'form_submitted.html')