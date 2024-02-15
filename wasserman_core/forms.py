from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django_select2.forms import ModelSelect2Widget
from django.forms import ModelForm
from .models import Player

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


#Formulaire Joueur
          

          
		
# Sous-formulaire pour l'étape 1
class PlayerAdd1(ModelForm):
    class Meta:
        model = Player
        fields = ('last_name', 'first_name','position', 'club_id')
        help_texts = {
            'club_id': 'Clic droit sur "Clubs" pour vérifier s\'il est dans la BDD. Ajoutez le s\'il manque',
        }

# Sous-formulaire pour l'étape 2
class PlayerAdd2(ModelForm):
    class Meta:
        model = Player
        fields = ('size', 'birth', 'other_pos', 'agent')

# Sous-formulaire pour l'étape 3
class PlayerAdd3(ModelForm):
    class Meta:
        model = Player
        fields = ('system', 'end_contract', 'wage', 'situation', 'comment', 'foot', 'date_prop', 'move_cond', 'end_mand', 'transfermarkt', 'champ', 'phone', 'agence_id', 'potential', 'note_actuel', 'release', 'note_financ')