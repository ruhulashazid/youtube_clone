from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from userauths.forms import UserRegisterForm
from django.contrib.auth import authenticate, login 
from django.contrib.auth import logout

User = settings.AUTH_USER_MODEL


def RegisterView(request):

    if request.user.is_authenticated:
        return redirect("index")

    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username") #  username = request.POST.get("email") - <input name="email">
            messages.success(request, f"Hey {username}, Account Created.")
            new_user = authenticate(username=form.cleaned_data['email'], 
                       password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect("index")

    else:
        form = UserRegisterForm()

    context = {
        "form":form,
    }
    return render(request, "userauths/sign-up.html", context)


def loginView(request):
    if request.user.is_authenticated:
        return redirect("index")
    
    if request.method == "POST":
        email = request.POST.get("email") ## {{ form.email }} X
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)
        except:
            messages.warning(request, "User does not exist")
        
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You are logged in")
            return redirect("index")
        else:
            messages.warning(request, "Username or Password, Does not exist")
            
    return render(request, "userauths/sign-in.html")


def logoutView(request):
    logout(request)
    return redirect("sign-in")

