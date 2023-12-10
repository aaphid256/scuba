from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import User, Dive, Destination
from .forms import DiveForm, DestinationForm


def index(request):
    dives = Dive.objects.filter(user=request.user).order_by("-pk")
    if request.method == 'POST':
        form = DiveForm(request.POST)
        if form.is_valid():
            dive = form.save(commit=False)
            dive.user = request.user
            dive.save()
            return redirect('index')
    else:
        form = DiveForm()

    return render(request, 'scuba/index.html', {
        'dives': dives,
        'form': form
        })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "scuba/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "scuba/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "scuba/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "scuba/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "scuba/register.html")


def dive_detail(request, pk):
    dive = get_object_or_404(Dive, pk=pk)
    return render(request, 'scuba/dive_detail.html', {
        'dive': dive
        })


def destination_list(request):
    destinations = Destination.objects.filter(user=request.user).order_by("-pk")
    if request.method == 'POST':
        form = DestinationForm(request.POST)
        if form.is_valid():
            destination = form.save(commit=False)
            destination.user = request.user
            destination.save()
            return redirect('destination_list')
    else:
        form = DestinationForm()

    return render(request, 'scuba/destination_list.html', {
        'destinations': destinations,
        'form': form
        })

def destination_detail(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    return render(request, 'scuba/destination_detail.html', {
        'destination': destination
        })


#def create_dive(request):
#    if request.method == 'POST':
#        form = DiveForm(request.POST)
#        if form.is_valid():
#            dive = form.save(commit=False)
#            dive.user = request.user
#            dive.save()
#            return redirect('dive_list')
#    else:
#        form = DiveForm()
#    return render(request, 'scuba/create_dive.html', {
#        'form': form
#        })
#
#
#def create_destination(request):
#    if request.method == 'POST':
#        form = DestinationForm(request.POST)
#        if form.is_valid():
#            destination = form.save(commit=False)
#            destination.user = request.user
#            destination.save()
#            return redirect('destination_list')
#    else:
#        form = DestinationForm()
#    return render(request, 'scuba/create_destination.html', {
#        'form': form
#        })