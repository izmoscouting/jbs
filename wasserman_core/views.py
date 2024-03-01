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
from .forms import SignUpForm,InfoMercatoForm, PlayerAdd1,PlayerAdd2,PlayerAdd3,CoachAddWizard1,CoachAddWizard2,ReportAddWizard1,ReportAddWizard2, BusinessForm,ClubsForm,AgencesForm,ContactsForm
from django import forms 
from .models import Player, Club, Business, Report, InfoMercato, Agency, Contact
from formtools.wizard.views import SessionWizardView
import datetime


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
def add_info_mercato(request):
    if request.method == 'POST':
        form = InfoMercatoForm(request.POST)
        if form.is_valid():
            info_mercato = form.save(commit=False)
            info_mercato.created_by = request.user.username  # Vous pouvez personnaliser ceci en fonction de la logique de votre application
            info_mercato.save()
            player_id = info_mercato.player.id
            return redirect('joueur', pk=player_id)  # Redirigez vers une page de succès ou ailleurs
    else:
        form = InfoMercatoForm()

    return render(request, 'core/add_info.html', {'form': form})

@login_required()
def add_business(request):
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            business_form = form.save(commit=False)
            business_form.created_by = request.user.username  # Vous pouvez personnaliser ceci en fonction de la logique de votre application
            business_form.save()
            return redirect('business')  # Redirigez vers une page de succès ou ailleurs
    else:
        form = BusinessForm()

    return render(request, 'core/add_business.html', {'form': form})

@login_required()
def add_club(request):
    if request.method == 'POST':
        form = ClubsForm(request.POST)
        if form.is_valid():
            clubs_form = form.save(commit=False)
            clubs_form.created_by = request.user.username  # Vous pouvez personnaliser ceci en fonction de la logique de votre application
            clubs_form.save()
            return redirect('clubs')  # Redirigez vers une page de succès ou ailleurs
    else:
        form = ClubsForm()

    return render(request, 'core/add_club.html', {'form': form})

@login_required()
def add_agence(request):
    if request.method == 'POST':
        form = AgencesForm(request.POST)
        if form.is_valid():
            clubs_form = form.save(commit=False)
            clubs_form.crea_by = request.user.username  # Vous pouvez personnaliser ceci en fonction de la logique de votre application
            clubs_form.save()
            return redirect('agences')  # Redirigez vers une page de succès ou ailleurs
    else:
        form = AgencesForm()

    return render(request, 'core/add_club.html', {'form': form})

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
def contacts(request):
    cleub = Contact.objects.all()
    unique_club = set()

    for club in cleub:
        unique_club.add(club.name)
    return render(request, 'core/agents.html', {'clubs':cleub})

@login_required()
def add_contact(request):
    if request.method == 'POST':
        form = ContactsForm(request.POST)
        if form.is_valid():
            clubs_form = form.save(commit=False)
            clubs_form.created_by = request.user.username  # Vous pouvez personnaliser ceci en fonction de la logique de votre application
            clubs_form.save()
            return redirect('contacts')  # Redirigez vers une page de succès ou ailleurs
    else:
        form = ContactsForm()

    return render(request, 'core/add_club.html', {'form': form})

@login_required()
def agences(request):
    cleub = Agency.objects.all()
    unique_club = set()

    for club in cleub:
        unique_club.add(club.name)
    return render(request, 'core/agence.html', {'clubs':cleub})


@login_required()
def mercato(request):
    playas = Player.objects.all()
    unique_positions = set()  # Utiliser un ensemble pour éviter les doublons

    for player in playas:
        unique_positions.add(player.position)
    return render(request, 'core/mercato.html',{'players' : playas, 'positions':unique_positions})

@login_required()
def business(request):
    busi = Business.objects.all()
    unique_positions = set()  # Utiliser un ensemble pour éviter les doublons

    for bus in busi:
        unique_positions.add(bus.stage)
    return render(request, 'core/business.html',{'business' : busi, 'positions':unique_positions})


@method_login_required('dispatch')
class PlayerAddWizard(SessionWizardView):
    form_list = [PlayerAdd1, PlayerAdd3, PlayerAdd2]  # Remplacez par vos formulaires réels
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
def joueur(request,pk):
    playas = Player.objects.get(id=pk)
    report = Report.objects.filter(player=pk)
    info = InfoMercato.objects.filter(player=pk)
    return render(request, 'core/joueur.html',{'player':playas,'report':report,'info':info})

def report(request,pk):
    report = Report.objects.get(id=pk)
    return render(request, 'core/rapport.html',{'report':report})

@login_required()
def success_view(request):
    return render(request, 'core/success.html', {})

@login_required()
def delete_player(request, pk):
    player = Player.objects.get(id=pk)
    pik = player.club_id.id
    player.delete()
    return redirect('club',pk=pik)

@login_required()
def delete_club(request, pk):
    player = Club.objects.get(id=pk)
    player.delete()
    return redirect('access')

@login_required()
def delete_contact(request, pk):
    player = Contact.objects.get(id=pk)
    player.delete()
    return redirect('contacts')

@login_required()
def delete_agence(request, pk):
    player = Agency.objects.get(id=pk)
    player.delete()
    return redirect('agences')

@login_required()
def delete_report(request, pk):
    player = Report.objects.get(id=pk)
    player.delete()
    return redirect('access')

@login_required()
def delete_business(request, pk):
    player = Business.objects.get(id=pk)
    player.delete()
    return redirect('business')

@login_required()
def update_contact(request, pk):
    # Récupérer l'instance du contact à mettre à jour
    contact = get_object_or_404(Contact, id=pk)

    if request.method == 'POST':
        # Remplir le formulaire avec les données soumises
        form = ContactsForm(request.POST, instance=contact)
        if form.is_valid():
            # Sauvegarder les modifications dans la base de données
            form.save()
            return redirect('contacts')  # Rediriger vers la liste des contacts après la mise à jour
    else:
        # Remplir le formulaire avec les données actuelles du contact
        form = ContactsForm(instance=contact)

    return render(request, 'core/add_club.html', {'form': form, 'contact': contact})

@login_required()
def update_agence(request, pk):
    # Récupérer l'instance du contact à mettre à jour
    contact = get_object_or_404(Agency, id=pk)

    if request.method == 'POST':
        # Remplir le formulaire avec les données soumises
        form = AgencesForm(request.POST, instance=contact)
        if form.is_valid():
            # Sauvegarder les modifications dans la base de données
            form.save()
            return redirect('agences')  # Rediriger vers la liste des contacts après la mise à jour
    else:
        # Remplir le formulaire avec les données actuelles du contact
        form = AgencesForm(instance=contact)

    return render(request, 'core/add_club.html', {'form': form, 'agence': contact})

@login_required()
def update_business(request, pk):
    # Récupérer l'instance du contact à mettre à jour
    contact = get_object_or_404(Business, id=pk)

    if request.method == 'POST':
        # Remplir le formulaire avec les données soumises
        form = BusinessForm(request.POST, instance=contact)
        if form.is_valid():
            # Sauvegarder les modifications dans la base de données
            form.save()
            return redirect('agences')  # Rediriger vers la liste des contacts après la mise à jour
    else:
        # Remplir le formulaire avec les données actuelles du contact
        form = BusinessForm(instance=contact)

    return render(request, 'core/add_business.html', {'form': form, 'business': contact})

@login_required()
def update_club(request, pk):
    # Récupérer l'instance du contact à mettre à jour
    contact = get_object_or_404(Club, id=pk)

    if request.method == 'POST':
        # Remplir le formulaire avec les données soumises
        form = ClubsForm(request.POST, instance=contact)
        if form.is_valid():
            form.mod_by = request.user.username
            # Sauvegarder les modifications dans la base de données
            form.save()
            return redirect('clubs')  # Rediriger vers la liste des contacts après la mise à jour
    else:
        # Remplir le formulaire avec les données actuelles du contact
        form = ClubsForm(instance=contact)

    return render(request, 'core/add_club.html', {'form': form, 'clubs': contact})


@method_login_required('dispatch')
class UpdateReportWizard(SessionWizardView):
    form_list = [ReportAddWizard1, ReportAddWizard2]
    template_name = 'core/add_report.html'  # Assurez-vous d'avoir un modèle pour la mise à jour

    def dispatch(self, request, *args, **kwargs):
        # Récupérez l'instance du rapport à mettre à jour
        report_id = kwargs.get('pk')
        self.report = get_object_or_404(Report, id=report_id)
        return super().dispatch(request, *args, **kwargs)

    def get_form_initial(self, step):
        # Pré-remplir le formulaire avec les données existantes du rapport
        initial = super().get_form_initial(step)
        initial.update(self.report.__dict__)
        return initial

    def done(self, form_list, **kwargs):
        form_data = {}
        for form in form_list:
            form_data.update(form.cleaned_data)

        # Mettez à jour les champs du rapport existant avec les nouvelles données
        for field, value in form_data.items():
            setattr(self.report, field, value)

        # Sauvegardez le rapport mis à jour
        self.report.save()

        # Redirigez vers la page Mercato après la mise à jour réussie
        return HttpResponseRedirect('/core/mercato')


@method_login_required('dispatch')
class UpdateAddWizard(SessionWizardView):
    form_list = [PlayerAdd1, PlayerAdd3, PlayerAdd2]
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
        
        form_data['mod_by'] = self.request.user.username
        
        # Chargez l'instance existante de Player à mettre à jour
        player_id = self.kwargs.get('pk')  # Assurez-vous d'avoir passé 'id' dans les kwargs de l'URL
        player = get_object_or_404(Player, id=player_id)
        for field, value in form_data.items():
            setattr(player, field, value)
        player.save()

        # Marquez comme soumis dans la session une fois le formulaire traité avec succès
        self.request.session['submitted'] = True
    
        return HttpResponseRedirect('/core/add_player_success')


@method_login_required('dispatch')
class CoachAddWizard(SessionWizardView):
    form_list = [CoachAddWizard1, CoachAddWizard2]  # Remplacez par vos formulaires réels
    template_name = 'core/add_coach.html'

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
    
        return HttpResponseRedirect('/core/add_coach_success')
    

@method_login_required('dispatch')
class AddReportWizard(SessionWizardView):
    form_list = [ReportAddWizard1, ReportAddWizard2]
    template_name = 'core/add_report.html'

    def done(self, form_list, **kwargs):
        form_data = {}
        for form in form_list:
            form_data.update(form.cleaned_data)
        
        form_data['created_by'] = self.request.user.username
        
        # Créez une instance de Player avec les données combinées et sauvegardez-la
        report = Report(**form_data)  # Assurez-vous que Player est correctement importé
        report.save()

        # Marquez comme soumis dans la session une fois le formulaire traité avec succès
        self.request.session['submitted'] = True
    
        return HttpResponseRedirect('/core/mercato')