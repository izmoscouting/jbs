from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django_select2.forms import ModelSelect2Widget
from django.forms import ModelForm
from .models import Player, Coach, Report, InfoMercato, Business, Club, Agency, Contact, BusiTargets

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Adresse Mail'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Prénom'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nom'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Requis. 150 lettres ou moins. Format : nom.prenom.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Mot de Passe'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Le mot de passe ne peut ressembler aux autres infos personnelles.</li><li>Minimum 8 caractères.</li><li>Ne doit pas être commun.</li><li>Ne peut pas être à 100% numérique.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirmez le Mot de Passe'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Entrez le même mot de passe, pour la vérification.</small></span>'


# Sous-formulaire pour l'étape 1
class PlayerAdd1(forms.ModelForm):
    class Meta:
        model = Player
        fields = ('last_name', 'first_name', 'birth', 'position', 'other_pos', 'club_id', 'foot', 'phone','size')
        widgets = {
            'birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        labels = {
            'last_name': 'Nom',
            'first_name': 'Prénom',
            'birth': 'Date de Naissance',
            'position': 'Poste',
            'other_pos': 'Autre Poste',
            'club_id': 'Club',
            'foot': 'Pied Fort',
            'phone':'Telephone',
            'size': 'Taille',
        }

        help_texts = {'club_id':'Cliquez sur \'Clubs\' et rajoutez le si le club du joueur manque.'}

    def __init__(self, *args, **kwargs):
        super(PlayerAdd1, self).__init__(*args, **kwargs)
        unique_positions = set(Player.objects.values_list('position', flat=True))
        unique_positions = [(pos, pos) for pos in unique_positions if pos]  # Exclure les positions vides
        unique_positions.sort(key=lambda x: x[1])
        
        # Appliquer les labels et les configurations définis dans Meta
        self.fields['position'] = forms.ChoiceField(
            label=self.Meta.labels['position'],
            choices=unique_positions,
            required=True,
            widget=forms.Select(attrs={'class': 'form-control'})
        )
        self.fields['other_pos'] = forms.MultipleChoiceField(
            label=self.Meta.labels['other_pos'],
            choices=unique_positions,
            required=False,
            widget=forms.SelectMultiple(attrs={'class': 'form-control'})
        )
        unique_foots = set(Player.objects.values_list('foot', flat=True))
        unique_foots = [(foo, foo) for foo in unique_foots if foo]
        unique_foots.sort(key=lambda x: x[1])
        
        self.fields['foot'] = forms.ChoiceField(
            label=self.Meta.labels['foot'],
            choices=unique_foots,
            required=True,
            widget=forms.Select(attrs={'class': 'form-control'})
        )


# Sous-formulaire pour l'étape 2
class PlayerAdd2(ModelForm):
    class Meta:
        model = Player
        fields = ('wage', 'release','end_contract','agence_id','contact','end_mand')
        labels = {
             'end_contract':'Fin de Contrat',
             'wage':'Salaire',
             'release':'Clause Libératoire',
             'agence_id':'Agence',
             'contact':'Agent lié',
             'end_mand':'Fin du Mandat',
        }
 
        widgets = {
            'end_contract': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_mand': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }

        help_texts = {'end_contract':'Mettre 30/06/année en cours si vous ne connaissez pas la date de fin',
                      'agence_id':'Cliquez sur \'Agences\' et rajoutez le si l\'agence du joueur manque.',
                      'contact':'Cliquez sur \'Contacts\' et rajoutez le si le contact du joueur manque.',}
# Sous-formulaire pour l'étape 3
class PlayerAdd3(ModelForm):
    class Meta:
        model = Player
        fields = ( 'transfermarkt', 'potential', 'note_actuel', 'note_financ','comment')

        widgets = {
            'phone': forms.NumberInput(attrs={'class': 'form-control'})
        }

        help_texts = {'comment':'Décrivez le joueur en mots clés, ex:\'Créatif, Rapide, Finisseur...\'','agence_id':'Cliquez sur \'Agence\' et rajoutez la si l\'agence du joueur manque.'}

        labels = {
             'potential':'Note Potentielle',
             'note_actuel':'Note Actuelle',
             'note_financ':'Note Financière',
             'comment':'Commentaires',
             'Transfermarkt':'transfermarkt'
        }


class CoachAddWizard1(forms.ModelForm):
    class Meta:
        model = Coach
        fields = ('name', 'system', 'birth', 'system', 'mentality', 'flexibility', 'personnality')
        widgets = {
            'birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        labels = {
            'name': 'Prénom & NOM',
            'system': 'Formation(s)',
            'birth': 'Date de Naissance',
            'mentality': 'Mentalité',
            'flexibility': 'Flexible',
            'personnality': 'Personnalité',
            'style':'Style de Jeu'
        }

class CoachAddWizard2(forms.ModelForm):
    class Meta:
        model = Coach
        fields = ('potential', 'rating', 'financial')
        labels = {
             'potential':'Potential',
             'rating':'Note Actuelle',
             'financial':'Note Financière'
        }

class ReportAddWizard1(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('player','poste','contre','competition','date')
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        labels = {
             'player':'Joueur',
            'contre':'Adversaire',            
        }
        help_texts = {'contre':'Cliquez sur \'Clubs\' et rajoutez le si le club du joueur manque.'}

class ReportAddWizard2(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('note_actuelle','note_potentielle','commentaires')
        labels = {
            'note_actuelle':'Note du Joueur',
            'note_potentielle':'Note Potentielle',
            'commentaires':'Rapport détaillé'       
        }

class InfoMercatoForm(forms.ModelForm):
    class Meta:
        model = InfoMercato
        fields = ['nature', 'info']
        labels = {
             'nature':'Nature de l\'info',
             'info':'Information'
        }
        help_texts={'nature':'Presse, rumeurs, infos confidentielles'}


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['pos_voulu', 'club_id', 'stage', 'closing_date', 'desc']
        labels = {
            'pos_voulu': 'Poste recherché',
            'club_id': 'Club',
            'stage': 'Stage',
            'closing_date': 'Avant le',
            'desc': 'Infos Complémentaires'
        }
        help_texts = {'club_id': 'Cliquez sur \'Clubs\' et rajoutez le si le club du joueur manque.',
                      'pos_voulu':'Utilisez des abréviations'}

        widgets = {
            'closing_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(BusinessForm, self).__init__(*args, **kwargs)
        unique_positions = set(Business.objects.values_list('stage', flat=True))
        unique_positions = [(pos, pos) for pos in unique_positions if pos]  # Exclure les positions vides
        unique_positions.sort(key=lambda x: x[1])

        # Appliquer les labels et les configurations définis dans Meta
        self.fields['stage'] = forms.ChoiceField(
            label=self.Meta.labels['stage'],
            choices=unique_positions,
            required=True,
            widget=forms.Select(attrs={'class': 'form-control'})
        )

class ClubsForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['Club', 'champ', 'country', 'coach', 'actual','financial','commentaires']
        labels = {
            'champ': 'Championnat',
            'country': 'Pays',
            'actual': 'Note Actuelle',
            'financial': 'Note Financière',
        }


class AgencesForm(forms.ModelForm):
    class Meta:
        model = Agency
        fields = ['name', 'contact_id', 'country', 'notes']
        labels = {
            'name': 'Nom',
            'contact_id':'Contacts',
            'country': 'Pays'
        }

class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['last_name', 'first_name', 'phone', 'commentaires']
        labels = {
            'last_name': 'Nom',
            'first_name': 'Prénom',
            'phone':'Téléphone',
            'commentaires': 'Infos Complémentaires'
        }

class ShortlistForm(forms.ModelForm):
    class Meta:
        model = BusiTargets
        fields = ['business']
        labels = {
            'business': 'Demandes Clubs'
        }