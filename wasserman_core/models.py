from django.db import models
from django.contrib.auth.models import User
import uuid
import datetime
import re


class Coach(models.Model):
    name = models.CharField(max_length=500)
    birth =  models.DateField(null=True)
    system = models.CharField(max_length=500, null=True)
    mentality = models.CharField(max_length=500, null=True)
    personnality = models.CharField(max_length=500, null=True)
    style = models.CharField(max_length=500, null=True)
    flexibility = models.CharField(max_length=500, null=True)
    rating = models.CharField(max_length=10,default='R0')
    financial = models.CharField(max_length=10,default='R0')
    potential = models.CharField(max_length=10,default='R0')
    note_totale = models.CharField(max_length=10,null=True)
    created_by = models.CharField(max_length=150,null=True)
    date_crea = models.DateField(default=datetime.datetime.today,editable=False)
    date_mod = models.DateField(null=True)
    mod_by = models.CharField(max_length=150,null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


    
    def save(self, *args, **kwargs):
        # Fonction pour extraire la valeur numérique
        def extract_number(value):
            match = re.search(r'R(\d+)', value)
            if match:
                return float(match.group(1))
            else:
                print(f"Value '{value}' does not match expected format")  # Débogage
                return 0.0

        # Extraire les valeurs numériques
        potential_value = extract_number(self.potential)
        note_actuel_value = extract_number(self.rating)
        note_financ_value = extract_number(self.financial)

        # Calculer la moyenne
        average = (potential_value + note_actuel_value + note_financ_value) / 3
        self.note_totale = f"R{average:.2f}"  # Conserver le format 'R' avec 2 décimales

        super(Player, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Club(models.Model):
    Club = models.CharField(max_length=150,default='Inconnu')
    parent_club = models.CharField(max_length=150,default='Aucun')
    champ = models.CharField(max_length=150,default='Inconnu')
    country = models.CharField(max_length=150,default='Inconnu')
    address = models.CharField(max_length=150,default='Inconnu')
    phone = models.CharField(max_length=150,default='Inconnu')
    sponsors = models.CharField(max_length=150,default='Inconnu')
    #coach = models.ForeignKey(Coach, on_delete=models.SET_NULL, null=True,default=None)
    coach = models.CharField(max_length=150,default='Inconnu')
    actual = models.CharField(max_length=10,default='R0')
    financial = models.CharField(max_length=10,default='R0')
    rating = models.CharField(max_length=10,default='R0')
    commentaires = models.TextField()
    date_crea = models.DateField(default=datetime.datetime.today,editable=False)
    date_mod = models.DateField(default=datetime.datetime.today)
    created_by = models.CharField(max_length=150,blank=True)
    mod_by = models.CharField(max_length=150,blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


    def save(self, *args, **kwargs):
        # Fonction pour extraire la valeur numérique
        def extract_number(value):
            match = re.search(r'R(\d+)', value)
            if match:
                return float(match.group(1))
            else:
                print(f"Value '{value}' does not match expected format")  # Débogage
                return 0.0

        # Extraire les valeurs numériques
        note_actuel_value = extract_number(self.actual)
        note_financ_value = extract_number(self.financial)

        # Calculer la moyenne
        average = (note_actuel_value + note_financ_value) / 2
        self.rating = f"R{average:.2f}"  # Conserver le format 'R' avec 2 décimales

        super(Club, self).save(*args,**kwargs)


    def __str__(self):
        return self.Club



class Agency(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=225,default='Inconnu')
    country = models.CharField(max_length=150,default='Inconnu')
    city = models.CharField(max_length=150,default='Inconnu')
    notes = models.CharField(max_length=2000,default='Inconnu')
    web = models.CharField(max_length=150,default='Inconnu')
    crea_by = models.CharField(max_length=150,null=True)
    mod_by = models.CharField(max_length=150,blank=True)
    date_crea = models.DateField(default=datetime.datetime.today,editable=False)
    date_mod = models.DateField(default=datetime.datetime.today)
    mod_by  = models.CharField(max_length=150,default=User,editable=False)
    

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50,default='Inconnu')
    last_name = models.CharField(max_length=50,default='Inconnu')
    name = models.CharField(max_length=50,default='Inconnu')
    phone = models.CharField(max_length=50,default='Inconnu')
    email = models.EmailField(max_length=100,default='Inconnu')
    phone_2 = models.CharField(max_length=150,default='-')
    situation = models.CharField(max_length=1500,default='-')
    commentaires = models.CharField(max_length=1500,default='-')
    created_by = models.CharField(max_length=150,null=True)
    mod = models.CharField(max_length=150,default=User,editable=False)
    date_crea = models.DateField(default=datetime.datetime.today,editable=False)
    club_id = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True,default=None)
    agency_id = models.ForeignKey(Agency, on_delete=models.SET_NULL, null=True,default=None)

    def save(self, *args, **kwargs):

        self.last_name = self.last_name.upper()

        self.name = f"{self.last_name} - {self.first_name}".strip()

        super(Contact, self).save(*args, **kwargs)

    def __str__(self):
        return self.last_name

class Business(models.Model):
    name = models.CharField(max_length=150,default='Inconnu')
    pos_voulu = models.CharField(max_length=150,default='Inconnu')
    closing_date = models.DateField(default=datetime.datetime(9999, 12, 31))
    club_id = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True, default=uuid.uuid4)
    desc = models.CharField(max_length=250,default='-')
    stage = models.CharField(max_length=225,default='Inconnu')
    next_step = models.CharField(max_length=225,default='Attente')
    lead_source = models.CharField(max_length=50,default='Partenaire')
    date_created = models.DateField(default=datetime.datetime.today,editable=False)
    created_by = models.CharField(max_length=150,default=User,editable=False)
    mod_time = models.DateField(default=datetime.datetime.today)
    rea_for_loss = models.CharField(max_length=250,default='-')
    contact_id = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True,default=None)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def save(self, *args, **kwargs):

        self.pos_voulu = self.pos_voulu.upper()

        self.name = f"{self.pos_voulu} - {self.club_id}".strip()

        super(Business, self).save(*args, **kwargs)

    def __str__(self):
        return self.name



class Scout(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    agency = models.ForeignKey(Agency, on_delete=models.SET_NULL, null=True,default=0)
    date = models.DateField(default=datetime.datetime.today)

    def __str__(self):
        return self.last_name


class Player(models.Model):
    name = models.CharField(max_length=500,default='-')
    position = models.CharField(max_length=50,default='Inconnu')
    club_id = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True)
    created_time =  models.DateField(default=datetime.datetime.today,editable=False)
    modified_time =  models.DateField(default=datetime.datetime.today)
    last_name =  models.CharField(max_length=50,null=True)
    first_name =  models.CharField(max_length=50,null=True)
    potential =  models.CharField(max_length=10,default='R0')
    size = models.CharField(max_length=3,default=175)
    birth =  models.DateField(null=True)
    other_pos = models.CharField(max_length=500,default=position)
    contact = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True, blank=True)
    system = models.CharField(max_length=500,default='Inconnu')
    end_contract = models.DateField(null=True,blank=True)
    wage = models.CharField(max_length=100,default='Inconnu')
    situation = models.CharField(max_length=500,default='Inconnu')
    comment = models.CharField(max_length=2000,default='Inconnu')
    foot = models.CharField(max_length=500,default='Inconnu')
    date_prop = models.DateField(null=True,blank=True)
    move_cond = models.CharField(max_length=500,default='-')
    end_mand = models.DateField(null=True,blank=True)
    transfermarkt = models.CharField(max_length=1000, default='transfermarkt.fr')
    champ = models.CharField(max_length=500,default='Inconnu')
    phone = models.CharField(max_length=10000,default= 612456789)
    agence_id = models.ForeignKey(Agency, on_delete=models.SET_NULL, null=True, blank=True)
    note_actuel = models.CharField(max_length=10,default='R0')
    release = models.CharField(max_length=500,default='Inconnu')
    note_financ = models.CharField(max_length=10,default='R0')
    note_tot = models.CharField(max_length=5,default='R0',editable=False)
    mod_by = models.CharField(max_length=150,blank=True)
    created_by = models.CharField(max_length=150,blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


    @property
    def age(self):
        current_date = datetime.date.today()
        birth_date = self.birth
        age = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))
        return age
    
    def save(self, *args, **kwargs):
        # Fonction pour extraire la valeur numérique
        def extract_number(value):
            match = re.search(r'R(\d+)', value)
            if match:
                return float(match.group(1))
            else:
                print(f"Value '{value}' does not match expected format")  # Débogage
                return 0.0

        # Extraire les valeurs numériques
        potential_value = extract_number(self.potential)
        note_actuel_value = extract_number(self.note_actuel)
        note_financ_value = extract_number(self.note_financ)

        # Calculer la moyenne
        average = (potential_value + note_actuel_value + note_financ_value) / 3
        self.note_tot = f"R{average:.2f}"  # Conserver le format 'R' avec 2 décimales

        self.last_name = self.last_name.upper()
        
        # Concaténer first_name et last_name en majuscules, puis affecter le résultat à name
        self.name = f"{self.last_name} {self.first_name}".strip()

        super(Player, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
class Report(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    pour = models.TextField(null=True)
    contre = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True)
    competition = models.CharField(max_length=500,default='-')
    poste =  models.CharField(max_length=500,default='-')
    date = models.DateField(default=datetime.datetime.today)
    note_actuelle = models.CharField(max_length=5,default='R0')
    note_potentielle = models.CharField(max_length=5,default='R0')
    created_by = models.CharField(max_length=150,blank=True)
    commentaires = models.TextField()

    @property
    def match(self):
        pour = self.player.club_id
        matche = f"A joué au poste de {self.poste} / {pour} contre {self.contre} en {self.competition} / {self.date}"
        return matche

    def save(self, *args, **kwargs):

        def extract_number(value):
            match = re.search(r'R(\d+)', value)
            if match:
                return float(match.group(1))
            else:
                print(f"Value '{value}' does not match expected format")  # Débogage
                return 0.0
        
        super().save(*args, **kwargs)
        # Calculer la moyenne des notes et mettre à jour la note du joueur
        joueur = self.player
        rapports_joueur = Report.objects.filter(player=joueur)
        if rapports_joueur.exists():
            notes_actuelles = sum(extract_number(rapport.note_actuelle) for rapport in rapports_joueur)
            moyenne_notes_joueur = notes_actuelles / len(rapports_joueur)
            joueur.note_actuel = f"R{moyenne_notes_joueur:.2f}" 
            notes_potentielles = sum(extract_number(rapport.note_potentielle) for rapport in rapports_joueur)
            moyenne_pot_joueur = notes_potentielles / len(rapports_joueur)
            joueur.potential = f"R{moyenne_pot_joueur:.2f}"
            note_fin = extract_number(joueur.note_financ)
            average = (extract_number(joueur.potential) + extract_number(joueur.note_actuel) + note_fin) / 3
            joueur.note_tot = f"R{average:.2f}"
            joueur.save()

class InfoMercato(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    created_by = models.CharField(max_length=150,blank=True)
    date = models.DateField(default=datetime.datetime.today)
    info = models.TextField()
    nature = models.CharField(max_length=250,blank=True)

class BusiTargets(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    player = models.ForeignKey(Player,null=True,on_delete=models.SET_NULL)
    created_by = models.CharField(max_length=150,blank=True)



