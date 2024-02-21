from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
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
        return render(request, 'core/login.html', {})

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
        return render(request, 'core/register.html', {'form':form})
    


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
    form_list = [PlayerAdd1, PlayerAdd2, PlayerAdd3]  # Remplacez par vos formulaires réels
    template_name = 'core/add_player.html'

    def done(self, form_list, **kwargs):
        form_data = {}
        for form in form_list:
            form_data.update(form.cleaned_data)
        
        form_data['created_by'] = self.request.user.username
        
        # Créez une instance de Player avec les données combinées et sauvegardez-la
        player = Player(**form_data)  # Assurez-vous que Player est correctement importé
        player.save()

        # Marquez comme soumis dans la session une fois le formulaire traité avec succès
        self.request.session['submitted'] = True
    
        return HttpResponseRedirect('/core/add_player_success')

@login_required()
def club(request,pk):
    cloub = Club.objects.get(id=pk)
    playas = Player.objects.filter(club_id=pk)
    busi = Business.objects.filter(club_id=pk)

    return render(request, 'core/club.html',{'club':cloub,'players':playas, 'Business':busi})

@login_required()
def success_view(request):
    return render(request, 'core/success.html', {})

@login_required()
def delete_player(request, pk):
    player = Player.objects.get(id=pk)
    pik = player.club_id.id
    player.delete()
    return redirect('club',pk=pik)

@method_login_required('dispatch')
class UpdateAddWizard(SessionWizardView):
    form_list = [PlayerAdd1, PlayerAdd2, PlayerAdd3]
    template_name = 'core/update_player.html'

    def get_form_initial(self, step):
        """
        Cette méthode est appelée par Django pour obtenir les données initiales pour chaque étape du formulaire,
        vous pouvez l'utiliser pour pré-remplir le formulaire avec les données de l'instance de joueur.
        """
        player_id = self.kwargs.get('pk')  # Récupère l'id du joueur depuis l'URL ou la session
        player = get_object_or_404(Player, id=player_id)
        initial_data = model_to_dict(player)  # Convertit l'instance en dictionnaire pour l'initialisation du formulaire
        return self.initial_dict.get(step, initial_data)

    def done(self, form_list, **kwargs):
        form_data = {}
        for form in form_list:
            form_data.update(form.cleaned_data)
        
        # Chargez l'instance existante de Player à mettre à jour
        player_id = self.kwargs.get('pk')  # Assurez-vous d'avoir passé 'id' dans les kwargs de l'URL
        player = get_object_or_404(Player, id=player_id)
        for field, value in form_data.items():
            setattr(player, field, value)
        player.save()

        # Marquez comme soumis dans la session une fois le formulaire traité avec succès
        self.request.session['submitted'] = True
    
        return HttpResponseRedirect('/core/add_player_success')
