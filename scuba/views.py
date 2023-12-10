from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.forms import formset_factory

from .models import User, Dive, Destination, DiverProfile
from .forms import DiveForm, DestinationForm, DiverProfileForm, DivePlannerForm, BackgasForm, DecoGasForm


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


def diver_profile(request):
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
    BackgasFormSet = formset_factory(BackgasForm, extra=0)
    DecoGasFormSet = formset_factory(DecoGasForm, extra=0)

    if request.method == 'POST':
        dive_form = DivePlannerForm(request.POST)
        backgas_formset = BackgasFormSet(request.POST)
        deco_gas_formset = DecoGasFormSet(request.POST)

        if dive_form.is_valid() and backgas_formset.is_valid() and deco_gas_formset.is_valid():
            # Process the form data and calculate Total Backgas Required
            dive = dive_form.save(commit=False)
            dive.user = request.user
            dive.save()

            total_backgas_required = (
                dive.backgas_set
                .annotate(depth_time=F('depth') * F('time') * Cast('diver_profile__functional_sac_rate', FloatField()))
                .aggregate(total_backgas_required=Sum('depth_time'))
            )['total_backgas_required'] or 0

            # ... other calculations ...

            return render(request, 'scuba/dive_planner.html', {
                'dive_form': dive_form, 
                'backgas_formset': backgas_formset, 
                'deco_gas_formset': deco_gas_formset,
                'total_backgas_required': total_backgas_required,
                # ... other calculated values ...
            })
    
    else:
        # Handle GET request here
        dive_form = DivePlannerForm()
        backgas_formset = BackgasFormSet()
        deco_gas_formset = DecoGasFormSet()

        return render(request,'scuba/dive_planner.html',{
            'dive_form': dive_form, 
            'backgas_formset': backgas_formset, 
            'deco_gas_formset': deco_gas_formset,
        })



def get_sac(request):
    profile, created = DiverProfile.objects.get_or_create(user=request.user)

    return JsonResponse({
        'functional_sac_rate': profile.functional_sac_rate,
        'deco_sac_rate': profile.deco_sac_rate,
        'min_gas_sac': profile.min_gas_sac
    })

