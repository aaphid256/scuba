# Django Views

from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import User, Dive, Destination, DiverProfile
from .forms import DiveForm, DestinationForm, DiverProfileForm


def index(request):
    # Retrieve and display user's dives
    dives = Dive.objects.filter(user=request.user).order_by("-pk")

    # Dive form submission
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
    # Handle user login
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
    # Logout
    logout(request)
    return HttpResponseRedirect(reverse("login"))


def register(request):
    # User registration
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
    # Display details of specific dive
    dive = get_object_or_404(Dive, pk=pk)
    return render(request, 'scuba/dive_detail.html', {
        'dive': dive
    })


def destination_list(request):
    # Display user's destinations and handle destination form
    destinations = Destination.objects.filter(
        user=request.user).order_by("-pk")
    
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


def diver_profile(request):
    # Display details of specific destination
    profiles = DiverProfile.objects.all()
    profile, created = DiverProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = DiverProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('diver_profile')
    else:
        form = DiverProfileForm(instance=profile)

    return render(request, 'scuba/diver_profile.html', {
        'form': form,
        'profiles': profiles
    })


def dive_planner(request):
    # Display dive planner page
    return render(request, 'scuba/dive_planner.html', {})
