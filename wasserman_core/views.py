from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from .forms import SignUpForm, PlayerAdd1,PlayerAdd2,PlayerAdd3
from django import forms 
from .models import Player, Club, Business
from formtools.wizard.views import SessionWizardView


def method_login_required(method):
    return method_decorator(login_required, name=method)

def home(request):
    return render(request, 'core/home.html', {})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Vous êtes bien connectés!")
            return redirect('access')
        
        else:
            messages.success(request, "Erreur, veuillez réessayer")
            return redirect('login')
        
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "Vous vous êtes bien déconnectés!")
    return redirect('home')

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #login user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Vous vous êtes bien inscrits"))
            return redirect('access')
        else:
            messages.success(request, ("Réessayez"))
            return redirect('register')
    else:
        return render(request, 'register.html', {'form':form})
    


@login_required()
def access(request):
    return render(request, 'core/access.html', {})

@login_required()
def clubs(request):
    cleub = Club.objects.all()
    unique_club = set()

    for club in cleub:
        unique_club.add(club.Club)
    return render(request, 'core/clubs.html', {'clubs':cleub})

@login_required()
def mercato(request):
    playas = Player.objects.all()
    unique_positions = set()  # Utiliser un ensemble pour éviter les doublons

    for player in playas:
        unique_positions.add(player.position)
    return render(request, 'core/mercato.html',{'players' : playas, 'positions':unique_positions})




@method_login_required('dispatch')
class PlayerAddWizard(SessionWizardView):
    form_list = [PlayerAdd1, PlayerAdd2, PlayerAdd3]
    template_name = 'core/add_player.html'

    @login_required()
    def done(self, form_list, **kwargs):
        # Ici, vous pouvez combiner les données des formes et sauvegarder/modifier comme nécessaire

        form_data = {}
        for form in form_list:
            form_data.update(form.cleaned_data)
        
        # Créez une instance de Player avec les données combinées
        player = Player(**form_data)
        player.save()  # Sauvegardez l'instance dans la base de données
        
        return HttpResponseRedirect('core/add_player?submitted=True')

@login_required()
def club(request,pk):
    cloub = Club.objects.get(id=pk)
    playas = Player.objects.filter(club_id=pk)
    busi = Business.objects.filter(club_id=pk)

    return render(request, 'core/club.html',{'club':cloub,'players':playas, 'Business':busi})

"""def add_player(request):
    submitted = False
    if request.method == "POST":
        form = PlayerAdd(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_player?submitted=True')
    else:
        form = PlayerAdd
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_player.html', {'form':form,'submitted':submitted})"""
