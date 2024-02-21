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
class PlayerAdd1(forms.ModelForm):
    class Meta:
        model = Player
        fields = ('last_name', 'first_name', 'birth', 'position', 'other_pos', 'club_id', 'foot', 'size')
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
        fields = ('system','end_contract', 'wage','situation','comment','move_cond', 'end_mand')
        labels = {
             'system':'Formation',
             'end_contract':'Fin de Contrat',
             'wage':'Salaire',
             'situation':'Situation',
             'comment':'Commentaires',
             'move_cond':'Condition Départ',
             'end_mand':'Fin du Mandat'
        }

        widgets = {
            'end_contract': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

        help_texts = {'comment':'Décrivez le joueur en mots clés, ex:\'Créatif, Rapide, Finisseur...\'',
                      'situation':'Inconnu ou Dispo pour un prêt/transfert',
                      'system':'4-4-2;4-3-3...',
                      'end_contract':'Mettre 31/12/1899 si vous ne connaissez pas la date de fin',
                      'move_cond':'Ajoutez des précisions sur un potentiel départ si vous en possédez'}

# Sous-formulaire pour l'étape 3
class PlayerAdd3(ModelForm):
    class Meta:
        model = Player
        fields = ( 'transfermarkt', 'phone', 'agence_id', 'potential', 'note_actuel', 'note_financ', 'release')

        widgets = {
            'phone': forms.NumberInput(attrs={'class': 'form-control'})
        }

        help_texts = {'agence_id':'Cliquez sur \'Agence\' et rajoutez la si l\'agence du joueur manque.'}

        labels = {
             'phone':'Telephone',
             'agence_id':'Agence',
             'potential':'Note Potentielle',
             'note_actuel':'Note Actuelle',
             'note_financ':'Note Financière',
             'release':'Clause Libératoire'
        }