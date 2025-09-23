# Cryo - Spécifications Detaillées
*Converted from PDF on 2025-09-23 14:12:52*

## Page 1

Spécifications détaillées
Cryo

Rev.
Prepared by
Reviewed
Date
Changes
1
John Doe

30/03/2018

Sommaire
MyCryo                                                                author : Caliatys                                                                                 1/43


![Image 1](images/image_p1_1_1.png)
*Image 1 - Page 1*

![Image 2](images/image_p1_2_2.png)
*Image 2 - Page 1*

---

## Page 2

### 1 - CONTEXTE​
4
### 2 - DESCRIPTION GÉNÉRALE DU BESOIN​
4
### 2.1 - PROFILS UTILISATEURS​
4
### 2.2 - TARIFICATION ET GESTION D’ENTREPRISE​
7
### 3 - CONNEXION​
8
### 3.1 - CONNEXION​
8
### 3.2 - MOT DE PASSE OUBLIÉ​
8
### 4 - ÉCRANS D’ACCUEIL​
9
### 4.1 - SANS CONNEXION​
9
### 4.2 - CLIENT CONNECTÉ​
9
### 4.3 - CRYO CONNECTÉ​
10
### 5 - CATALOGUE PDR​
13
### 5.1 - CATÉGORIES​
13
### 5.2 - CRÉATION COMMANDE PDR CLIENT CONNECTÉ​
14
### 5.2.1 - CHOIX DES ARTICLES​
14
### 5.2.2 - PANIER DE COMMANDE​
15
### 5.2.3 - MON ADRESSE D’EXPÉDITION​
15
### FIGURE 9 : ADRESSE D’EXPÉDITION, DERNIÈRE ÉTAPE AVANT VALIDATION DE LA DEMANDE​
16
### 5.3 - CRÉATION COMMANDE PDR SANS CONNEXION (VISITEUR)​
17
### 5.3.1 - CHOIX DES ARTICLES​
17
### 5.3.2 - PANIER DE COMMANDE​
17
### 5.3.3 - M’IDENTIFIER​
17
### 5.3.4 - MES COORDONNÉES​
17
### 6 - DEMANDES SERVICES​
18
### 6.1 - FORMULAIRES​
18
### 6.2 - CONFIRMATION DE DEMANDE​
20
### 7 - DEMANDES​
21
### 7.1 - STATUT DE DEMANDE​
21
### 7.2 - NOUVELLES DEMANDES​
22
### 7.3 - DEMANDES EN COURS​
23
### 7.3.1 - COTÉ CLIENT​
23
### 7.3.2 - CÔTÉ CRYO​
26
### 7.4 - NOTION DE DEVIS​
28
### 7.5 - DEMANDES CLÔTURÉES​
29
### 7.6 - CRÉER UNE DEMANDE POUR UN CLIENT​
29

MyCryo                                                                Author : ACME                                                                            ​
2/43


---

## Page 3

### 8 - COMMANDES PASSÉS​
29
### 9 - MES MATÉRIELS & DOCUMENTATION​
30
### 9.1 - CÔTÉ CLIENT​
30
### 9.2 - CÔTÉ CRYO​
31
### 10 - MON COMPTE​
31
### 11 - GESTION DES COMPTES​
32
### 11.1 - CRÉATION DE COMPTE CLIENT​
32
### 11.1.1 - DEMANDE DE CRÉATION PAR UN SIMPLE VISITEUR​
32
### 11.1.2 - DEMANDE DE CRÉATION PAR UN CLIENT​
33
### 11.1.3 - CRÉATION PAR UN EMPLOYÉ CRYO​
34
### 11.2 - VALIDATION DE COMPTE CLIENT​
34
### 11.3 - GESTION DES UTILISATEURS CLIENTS​
35
### 11.4 - GESTION DES UTILISATEURS CRYO​
36
### 12 - MES CONTACTS CRYO​
37
### 12.1 - CONTACT PRIVILÉGIÉ​
37
### 12. 2 - CONTACTS GÉNÉRIQUES​
38
### 13 - MESURES DE PERFORMANCES​
38
### 14 - ATTENTES DE LA PART DE CRYO​
38
### 14.1 - NOM DE DOMAINE​
38
### 14.2 - EXIGENCES INTERFACES​
39
### 14.2.1 - INTERFACES FOURNIES POUR LE DÉVELOPPEMENT​
39
### 14.2.2 - INTERFACES FOURNIES POUR L’UTILISATION DU PORTAIL MYCRYO​
39
### 14.3 - LIVRAISONS DE DONNÉES​
41
### TABLE DES FIGURES​
42

MyCryo                                                                Author : ACME                                                                            ​
3/43


---

## Page 4

1 - Contexte
La société Cryo est spécialisée dans la construction d’équipements de stockages fixes et
mobiles pour gaz liquéfiés à basse température.
Afin de développer son activité, elle souhaite mettre en place un site web EXTRANET sécurisé
destiné aux services clients . Ce portail, français/anglais portera le nom de “MyCryo ”. Un lien
vers l’extranet sera intégré sur le site institutionnel www.mycryo.com .
​
​
​
​
​
​

2 - Description générale du besoin
2.1 - Profils utilisateurs
Ce site web adaptatif et sécurisé devra disposer d’un outil de statistiques permettant de
construire des indicateurs de pilotage quant au traitement des demandes et aux
connexions.​
​

​
​
​

La page d’accueil de MyCryo est visible par tous via internet et elle est référencée dans
les moteurs de recherche. Cette page comporte :​

-​
Une présentation de la nature des produits et services accessibles via le portail
client MyCryo​
-​
Un lien permettant de revenir sur le site institutionnel www.Cryo.com/services
-​
Un lien pour que le visiteur puisse demander la création d’un compte via un
formulaire
-​
Un lien pour que le visiteur enregistré puisse se connecter (clients enregistrés sur
le site)
-​
Un lien est également proposé pour les visiteurs non authentifiés vers des
formulaires de contact afin de créer une demande de service.

Tous les utilisateurs Cryo disposent d’un compte personnel rattaché à un ou plusieurs
service (groupe d’utilisateurs). On distingue aujourd’hui 6 organisations :​
​
- Pièces de Rechange (PDR)
​
- Cryo Services (CRYS)
​
- Support Après-Vente
​
- Support Technique
​
- Support Qualité
​
- Support Commercial
​

MyCryo                                                                Author : ACME                                                                            ​
4/43


---

## Page 5

Les utilisateurs Cryo ont une visibilité sur les demandes créées dans le portail MyCryo
liée à leur service.

​
Il existe 8 types de demandes :
-​
Maintenance, Expertise & Réparation
-​
Formation
-​
Audits de parc et intervention
-​
Garanties et réclamations
-​
Documentation et information technique
-​
Pièce de rechange spécifique
-​
Pièce de rechange catalogue
-​
Autres demandes

​
Il y a trois types de visibilités sur les demandes :
-​
Leader : les services leader d’un type de demande reçoivent directement les
nouvelles demande de ce type afin de les traiter
-​
Contributeur : un contributeur voit les demandes qui lui sont affectées en tant que
contributeur, en plus de son périmètre par défaut. Tous les utilisateurs Cryo
peuvent être ajoutés à une demande en tant que contributeurs, peu importe leur
service.
-​
Accès : les services ayant “accès” à des types de demandes peuvent voir toutes
les demandes en cours à titre observateur. Ils n’ont pas de droit de modification
tant qu’ils ne sont pas rajoutés comme contributeurs des demandes.

Equipes
Cryo

Types de
demande
Cryo
Services
### (CRYS)
Service
qualité
Service
technique
Service
PDR
Service
commercial
Service
SAV
Maintenance,
Expertise &
Réparation
Leader
Accès
Accès

Accès
Accès
Formation
Leader
Accès
Accès

Accès

MyCryo                                                                Author : ACME                                                                            ​
5/43


---

## Page 6

Audits de parc et
intervention
Leader
Accès
Accès

Accès

Garanties et
réclamations

Leader
Accès

Accès
Accès
Documentation et
information
technique

Accès
Leader

Accès
Accès
Pièce de rechange
spécifique

Accès
Accès
Leader
Accès

Pièce de rechange
catalogue

Accès
Accès
Leader
Accès

Autres demandes
Equipe
leader à
remplir
par Cryo
Accès
Accès

Accès
Accès
​
Figure 1 : Tableau de répartition des types de demandes et des visibilités
associées

Les utilisateurs de Cryo sont répartis ainsi :
●​ Employé Cryo
●​ Responsable d’équipe, il gère le dispatch des demandes
●​ Super administrateur, il a accès à toutes les équipes et s’occupe du maintien du
portail :
○​ Création d’un nouvel utilisateur Cryo
○​ Validation de création d’un compte client (pour une demande émanant
d’un client)
○​ Import manuel des photos, pictogrammes
○​ Import manuel des prix catalogues et autres fichiers à mettre à jour
manuellement
○​ MAJ du panneau d’accueil
​

Tous les utilisateurs Cryo peuvent créer un utilisateur client. Il est automatiquement
validé.
​

Les utilisateurs client de Cryo sont répartis ainsi :
●​ Lecteur = personne non authentifiée qui a la possibilité d'effectuer une demande
(les prix ne sont pas affichés pour une demande de PDR par exemple)
●​ Créateur = personne maintenant authentifiée qui peut effectuer une demande

MyCryo                                                                Author : ACME                                                                            ​
6/43


---

## Page 7

●​ Modérateur = principalement responsable de site qui gère la création de compte
pour plusieurs utilisateurs, il peut modifier le droit des employés de son
entreprise : créateur ou modérateur

2.2 - Tarification et gestion d’entreprise
​
Les entreprises ne sont pas gérées dans MyCryo : les informations remontent de BaaN
et les clients MyCryo sont rattachés manuellement par Cryo, lors de la validation de leur
compte, à une entreprise déjà existante dans BaaN. Chaque compte client est rattaché à
une entreprise qui est elle même liée à un niveau de tarification dans BaaN ce qui défini
les tarifs du catalogue.​
​
​
​
​

​
Figure 2 : Principe des tarifications associées aux comptes client
​
​
​
​
​
​

​
Si un client fait parti d’une entreprise non connue de Cryo et donc inconnue dans la base
de données BaaN, l’entreprise du client dans MyCryo sera “inconnu”. Le client n’aura
pas accès aux tarifs dans le catalogue tant qu’il ne sera pas assigné à une entreprise
remontant de BaaN. ​ ​
​

​
Info process Cryo : prévoir, pour toute demande de création de compte de la part d’une
entreprise inconnue dans BaaN, de suivre les étapes suivantes : 1/ création de
l’entreprise dans BaaN, 2/ temps de remontée de BaaN vers MyCryo, 3/ validation de la
demande de création client et rattachement à la bonne entreprise.​
​

3 - Connexion
3.1 - Connexion
Chaque utilisateur a accès à une page de connexion composée :
-​
D’une adresse mail
-​
D’un mot de passe

MyCryo                                                                Author : ACME                                                                            ​
7/43


![Image 3](images/image_p7_1_3.png)
*Image 3 - Page 7*

---

## Page 8

3.2 - Mot de passe oublié
Les utilisateurs (client et Cryo) ont la possibilité de changer de mot de passe en cas
d’oubli.
Pour cela ils doivent saisir leur adresse mail.  Un email leur sera envoyé avec le lien vers
une page de changement de mot de passe.

Figure 3 : Écran de connexion
4 - Écrans d’accueil
4.1 - Sans connexion
Les lecteurs ont :
-​
Accès au catalogue de pièce de rechange sans prix
-​
Accès aux formulaires de demandes de service
-​
Accès à création de compte ou à la connexion
-​
Une bannière avec photo et du texte affiché par Cryo

MyCryo                                                                Author : ACME                                                                            ​
8/43


![Image 4](images/image_p8_1_4.png)
*Image 4 - Page 8*

![Image 5](images/image_p8_2_5.png)
*Image 5 - Page 8*

---

## Page 9

4.2 - Client connecté

Figure 4 : Écran d’accueil d’un client connecté
Les clients connectés ont :
-​
Accès au catalogue de pièces de rechange avec les prix relatifs au tarif qui -
leur a été attribué
-​
Accès aux demandes de service
-​
Accès aux commandes passées, demandes en cours, assets dans mon parc
-​
Une bannière avec photo et du texte affiché par Cryo
-​
Accès au caddie
-​
Menu client :
-​
Commandes passées
-​
Demandes en cours

MyCryo                                                                Author : ACME                                                                            ​
9/43


![Image 6](images/image_p9_1_6.png)
*Image 6 - Page 9*

![Image 7](images/image_p9_2_7.png)
*Image 7 - Page 9*

---

## Page 10

-​
Mes coordonnées
-​
Mes adresses de livraison
-​
Gestion de mes utilisateurs (si modérateur)
-​
Mes contacts Cryo

Pour afficher les pages “comme les voient les clients”, Cryo créera un compte générique
Cryo par entreprise.
4.3 - Cryo connecté

Les employés Cryo connectés ont accès à un accueil permettant de rechercher un client
ou une organisation. Ils ont également accès au catalogue sans prix et aux demandes
de services. En effet, les employés Cryo ne sont pas affectés à une entreprise, ils n’ont
donc pas de tarif associé mais peuvent guider les clients en ayant accès au catalogue.

Les employés Cryo n’ont pas de dashboard. Ils accèdent directement aux demandes
en cours pour lesquelles ils sont leaders ou collaborateurs. Ils peuvent à l’aide d’un filtre
voir la liste de toutes les demandes en cours liées à leur service.

Les responsables de services et les super administrateurs ont accès à un
dashboard.
Ils ont accès à 4 informations, le nombre total (toutes demandes et toutes équipes
confondues) sur les 30 derniers jours glissant :
-​
De nouvelles demandes
-​
De demandes en cours
-​
De demandes clôturées commandées
-​
De demandes clôturées perdues
Ces chiffres permettent d’avoir une vision globale à l’instant t des derniers 30 jours
glissants de l’activité de toute l’entreprise.

Ils ont également accès au nombre sur les 30 derniers jours glissants des demandes :
-​
“En cours de traitement”, il s’agit des demandes ayant le statut “En cours de
traitement”
-​
“Dormantes”, il s’agit des demandes ayant le statut “En cours de traitement” et
n’ayant pas été modifiées depuis les 15 derniers jours. Ce chiffre est cliquable et
dirige vers la liste des demandes dormantes.
-​
“Clôturées/Commandées”, il s’agit des demandes ayant le statut “Clôturé” et pour
lesquelles un BC a été joint par Cryo à l’endroit réservé à cet effet
-​
“Clôturées/Perdues”, il s’agit des demandes ayant le statut “Clôturé” et pour
lesquelles aucun BC a été joint par Cryo à l’endroit réservé à cet effet

MyCryo                                                                Author : ACME                                                                            ​
10/43


---

## Page 11

-​
“Temps moyen de réponse” il s’agit de la moyenne du temps écoulé entre le
statut “Demande clôturée” et l’ouverture de la demande.

Les responsables de services n’ont accès qu’aux chiffres concernant les types de
demandes pour lesquels ils sont responsables, les super administrateurs ont accès aux
chiffres de tous les types de demandes.

Le graphique dynamique comprend l’historique des 12 derniers mois glissants avec le
choix de visualisation des 8 types de demandes (cf Figure 1) avec le choix des 5 statuts
possibles :
-​
Nouvelle demande
-​
En cours de traitement
-​
Clôturée Commandée
-​
Clôturée Perdue
-​
En attente
Les statuts sont sélectionnables à l’aide de 5 checkboxs, les types de demandes sont
sélectionnables avec des checkboxs situées dans une drop-down liste.

Les super administrateurs ont en plus accès  :
-​
Au nombre de demandes de création de compte (bouton cliquable qui dirige vers
la liste des demandes de création de compte)
-​
Au nombre de comptes Cryo actifs
-​
A un bouton “Analytics” qui est un lien vers Google Analytics
-​
A un bouton “Export” qui permet d’exporter sous forme excel toutes les données
du graphique représentant les demandes de l’années écoulée (12 mois glissants)
en une seule fois.

MyCryo                                                                Author : ACME                                                                            ​
11/43


![Image 8](images/image_p11_1_8.png)
*Image 8 - Page 11*

![Image 9](images/image_p11_2_9.png)
*Image 9 - Page 11*

![Image 10](images/image_p11_3_10.png)
*Image 10 - Page 11*

---

## Page 12

Figure 5 : Dashboard super administrateur (gauche), dashboard responsable CRYS (droite)
L’UX de ces deux écrans est susceptible de changer.
​

​
Le menu Cryo comprend :
●​ Pour les employés Cryo :
-​
Gestion des utilisateurs clients

●​ Pour les responsables de service :
-​
Gestion des utilisateurs clients
-​
Gestion des utilisateurs Cryo (de leur service)

●​ Pour les super administrateurs :
-​
Editer le bandeau d’accueil (photo et texte qui apparaissent sur la page
d’accueil des clients ou des visiteurs) : visible uniquement par les super
administrateurs
-​
Importer des données (photos ou pictogrammes des familles de produits,
import du catalogue PDR standard): visible uniquement par les super
administrateurs
-​
Gestion des utilisateurs clients
-​
Gestion des utilisateurs Cryo
-​
Historique des comptes refusés

MyCryo                                                                Author : ACME                                                                            ​
12/43


---

## Page 13

Pour accéder au dashboard (si responsable ou super administrateur), aux demandes ou
au catalogue, les utilisateurs cliquent sur les options proposées dans le bandeau
supérieur du portail (texte ou pictogrammes)

5 - Catalogue PdR
5.1 - Catégories
Le catalogue est composé d’une liste de catégorie avec photo et libellé. Chaque
catégorie est composée d’une liste de pièces de rechange détaillée.

Figure 6 : Catégories du catalogue
5.2 - Création commande PdR client connecté
5.2.1 - Choix des articles
Un utilisateur peut rechercher un produit par son nom ou par sa référence.
Chaque produit de la liste est composé : d’une référence produit, d’une
désignation (libellé, taille, fournisseur), d’une disponibilité (“En stock”, “Sur

MyCryo                                                                Author : ACME                                                                            ​
13/43


![Image 11](images/image_p13_1_11.png)
*Image 11 - Page 13*

![Image 12](images/image_p13_2_12.png)
*Image 12 - Page 13*

---

## Page 14

commande”, “Disponible sous XX jours”), d’un prix unitaire. Le visiteur peut
choisir la quantité à commander de chaque article et ajouté ces article au panier
avec le bouton “Ajouter au panier”.

Ajouter un article au panier créé une alerte avec une bulle et un numéro sur
l’icône panier.

Recherche pour les PDR : barre de recherche et drop-down list pour les
fournisseurs et sous-catégories.

Figure 7 : Liste des articles du catalogue dans une catégorie
5.2.2 - Panier de commande
Le panier est composé de la liste des produits commandés : Désignation (libellé,
taille, fournisseur), disponibilité (“En stock”, “Sur commande”, “Disponible sous
XX jours”), prix unitaire, quantité et du prix total par produit si l’utilisateur
commande une quantité supérieure à 1 du produit.
Le client a accès au montant total du panier.
Il peut retourner au catalogue ou passer à l’étape suivante.

MyCryo                                                                Author : ACME                                                                            ​
14/43


![Image 13](images/image_p14_1_13.png)
*Image 13 - Page 14*

![Image 14](images/image_p14_2_14.png)
*Image 14 - Page 14*

---

## Page 15

Le prix de livraison n’est pas calculé car actuellement, aucun accord avec des
transporteurs ne permet d’estimer le prix de livraison.
Figure 8 : Panier de commande, client connecté
5.2.3 - Mon adresse d’expédition
L’utilisateur peut choisir son adresse principale (elle est automatiquement
renseignée et est l’adresse postale de son entreprise). Il peut également ajouter
une adresse en renseignant les informations suivantes :
-​
Nom de mon adresse
-​
Adresse
-​
Complément d’adresse
-​
Ville
-​
Code postal
-​
Numéro de téléphone
Mais il peut aussi choisir parmi la liste des adresses de livraison qu’il a déjà
ajoutées. Ces adresses sont liées au client et non à l’entreprise.

L’utilisateur a toujours accès au montant total de son panier.

Lorsque la commande est confirmée, une demande est créée côté Cryo et côté
client puis un mail est envoyé au client. Les prix enregistrés dans la demande
sont fixes.

MyCryo                                                                Author : ACME                                                                            ​
15/43


![Image 15](images/image_p15_1_15.png)
*Image 15 - Page 15*

![Image 16](images/image_p15_2_16.png)
*Image 16 - Page 15*

---

## Page 16

Le panier du client est conservé 30 jours.

MyCryo                                                                Author : ACME                                                                            ​
16/43


---

## Page 17

Figure 9 : Adresse d’expédition, dernière étape avant validation de la demande

5.3 - Création commande PdR sans connexion (visiteur)
5.3.1 - Choix des articles
Un utilisateur peut rechercher un produit par son nom ou par une référence.
Chaque produit de la liste est composé : d’une référence produit, d’une
désignation (libellé, taille, fournisseur), d’une disponibilité (“En stock”, “Sur
commande”, “Disponible sous XX jours”)
Le visiteur peut choisir la quantité à commander de chaque article et ajouté ces
article au panier avec le bouton “Ajouter au panier”.

Ajouter un article au panier créé une alerte avec une bulle et un numéro sur
l’icône panier.

MyCryo                                                                Author : ACME                                                                            ​
17/43


![Image 17](images/image_p17_1_17.png)
*Image 17 - Page 17*

---

## Page 18

Les visiteurs/lecteurs n’ont pas accès aux prix des pièces de rechange.

5.3.2 - Panier de commande
Le panier est composé de la liste des produits commandés : Désignation (libellé,
taille, fournisseur), disponibilité (“En stock”, “Sur commande”, “Disponible sous
XX jours”), quantité.
Il est possible de retourner au catalogue ou de passer à l’étape suivante.
5.3.3 - M’identifier
Le visiteur a la possibilité de se connecter s’il est déjà client et possède un
compte MyCryo ou bien il peut continuer la commande sans compte.
5.3.4 - Mes coordonnées
Si le visiteur continue sans connexion, il a accès à une page de coordonnées où
il doit renseigner les informations suivantes avant de pouvoir continuer la
commande :
-​
Nom
-​
Prénom
-​
Téléphone
-​
Adresse mail
-​
Entreprise
-​
Fonction

​
​
Adresse d’expédition :
-​
Nom de l’adresse
-​
Adresse
-​
Complément d’adresse
-​
Ville
-​
Code postal
-​
Numéro de téléphone
-​
Checkbox : “Créer un compte via mes informations”

La confirmation de la demande engendre la création d’une demande côté Cryo et
envoie mail au client.

MyCryo                                                                Author : ACME                                                                            ​
18/43


---

## Page 19

6 - Demandes Services
Les clients ont accès à la liste des services proposés par MyCryo.
6.1 - Formulaires
Les formulaires sont les suivants :
-​
Maintenance, Expertise & Réparation
-​
Formation
-​
Audits de parc et intervention
-​
Garanties et réclamations
-​
Documentation et information technique
-​
PDR Pièce de rechange
-​
Autres demandes

Figure 10 : Liste des formulaires

Différentes rubriques/étapes sont renseignées par formulaire.

MyCryo                                                                Author : ACME                                                                            ​
19/43


![Image 18](images/image_p19_1_18.png)
*Image 18 - Page 19*

![Image 19](images/image_p19_2_19.png)
*Image 19 - Page 19*

---

## Page 20

Si le client est non connecté (un visiteur/lecteur), il doit renseigner les coordonnées
suivantes :
-​
Prénom
-​
Nom
-​
Nom d’entreprise
-​
Fonction
-​
Adresse​

-​
Code Postal
-​
Ville
-​
Pays
-​
Téléphone
-​
Mail
Le visiteur a un espace commentaire libre dans lequel il peut noter toute sorte de
remarque.
Il n’y a pas d’édition de formulaire possible.

​
​

Figure 11 : Informations identitaires demandées en fin de formulaire si le client n’est pas
connecté

MyCryo                                                                Author : ACME                                                                            ​
20/43


![Image 20](images/image_p20_1_20.png)
*Image 20 - Page 20*

![Image 21](images/image_p20_2_21.png)
*Image 21 - Page 20*

---

## Page 21

Les clients ont la possibilité d’ajouter une pièce jointe au formulaire.
Si le formulaire concerne un matériel, le client peut choisir les matériels qui font l’objet
d’une demande parmi une drop-down liste qui comprend ses matériels. L’accès à la
documentation des matériels se fait dans une autre section (“Mes matériels”)

Un employé Cryo a la possibilité de remplir un formulaire pour un de ses clients. A la fin
du formulaire, il devra alors remplir le nom du client concerné.
6.2 - Confirmation de demande
La confirmation de création de demande, soit la validation d’un formulaire engendre la
création d’une demande côté client et côté Cryo.
​
Une popup apparaît côté client pour lui confirmer la création de la demande.
7 - Demandes
Toute commande de PdR, ou création d’une demande service (formulaire) engendre la création
d’une demande.
Une demande est liée à un client et porte une référence unique, générée automatiquement par
le portail MyCryo.

MyCryo                                                                Author : ACME                                                                            ​
21/43


![Image 22](images/image_p21_1_22.png)
*Image 22 - Page 21*

![Image 23](images/image_p21_2_23.png)
*Image 23 - Page 21*

---

## Page 22

Figure 12 : Liste des demandes vue par un responsable de service Cryo

7.1 - Statut de demande
Une demande a un statut qui peut être changé par Cryo :

-​
Demande enregistrée : Indique que la demande a été reçue par Cryo. Créé une
popup côté client lorsqu’il valide une commande ou demande de service afin de
le prévenir de la prise en charge.
​
​
​
Afficher : Nouvelle demande
-​
Demande en cours de traitement : Indique que la demande a été prise en
charge par Cryo. Ce changement de statut s’effectue automatiquement quand un
utilisateur Responsable d’équipe Cryo affecte un employé de son équipe à cette
demande. Envoie un mail au client pour le prévenir.
​
​
​
Afficher : En cours de traitement
-​
Demande clôturée  : Indique que la demande est clôturée par le leader. Envoie
automatiquement un mail au client
​
​
​
Afficher : Clôturée
-​
Demande en attente : La commande est pour une raison diverse en attente.
L’utilisation de ce statut est manuelle.. Pas de mail ni de notification automatique.
​
​
​
Afficher : En attente
Les relances se feront manuellement en utilisant soit la messagerie interne du portail,
soit la messagerie conventionnelle ou tout autre moyen de communication (téléphone).
7.2 - Nouvelles demandes
Chaque responsable de service Cryo reçoit toutes les demandes liées à son secteur
dans l’onglet “Nouvelles demandes”. ​
​
​
​
​
​
​
​
​

C’est le responsable de service qui attribue une demande à une de ses employés.​

Il existe 5 familles de services comprenant les différents formulaires et les demandes
sont attribuées aux services de la manière suivante :

Services
Maintenance, Expertise & Réparation
Cryo Services (CRYS)
Formation
Cryo Services (CRYS)

MyCryo                                                                Author : ACME                                                                            ​
22/43


---

## Page 23

Audits de parc et intervention
Cryo Services (CRYS)
Garanties et Réclamations
Garanties et réclamations
Service qualité
Documentation et Information techniques
Documentation et information technique
Service technique
PDR
Pièce de rechange spécifique
Service PDR
Autres demandes
Autres demandes
Equipe à remplir par Cryo

Ces 5 familles sont listées dans l’accueil client. Seul Services comprend 3 formulaires,
une page avec ces 3 formulaires est donc proposée au client s’il clique sur le lien
Services de l’accueil.
Le lien “Services” situé dans la barre du menu supérieur renvoie à la liste de tous les
formulaires.
7.3 - Demandes en cours
7.3.1 - Coté client
Un client a accès aux demandes de son organisation et aux demandes qu’il a
faites. Par défaut seules ses demandes sont affichées. Il peut à l’aide d’un filtre
afficher toutes les demandes de son organisation.

Un client peut rechercher un matériel ou une référence de demande.
Il a accès à la liste des demandes en cours de son organisation uniquement.

Chaque demande dans la liste comprend :
-​
Référence
-​
Type de demande
-​
Interlocuteur (Employé Cryo affecté à cette demande : leader)
-​
Demandeur
-​
Entreprise demandeur
-​
Nombre de commentaires et de pièces jointes
-​
Date de création

MyCryo                                                                Author : ACME                                                                            ​
23/43


---

## Page 24

-​
Statut de la demande
-​
Date du changement de statut
-​
Adresse de livraison renseignée

Figure 13 : Liste des demandes en cours côté client

MyCryo                                                                Author : ACME                                                                            ​
24/43


![Image 24](images/image_p24_1_24.png)
*Image 24 - Page 24*

---

## Page 25

Détail d’une demande :
-​
Récapitulatif des pièces jointes (si devis ou bon de commande, message
et PJ en couleur) possibilité de supprimer une pièce jointe
-​
Coordonnées du demandeur et du contact Cryo
-​
Possibilité d’échanger par message avec le contact Cryo. Possibilité de
joindre une pièce jointe.
-​
Historique des messages échangés
-​
Date de création
-​
Date de dernière modification (ajout de message notamment)

Figure 14 : Détail d'une commande de pièce de rechange faites par le catalogue côté client
(gauche) Détail d’une demande faites via un formulaire côté client (droite)

MyCryo                                                                Author : ACME                                                                            ​
25/43


![Image 25](images/image_p25_1_25.png)
*Image 25 - Page 25*

![Image 26](images/image_p25_2_26.png)
*Image 26 - Page 25*

---

## Page 26

Si la demande concerne une commande de PdR : Résumé du panier avec prix et
détail de la commande
Si la demande concerne une demande de service : Objet de la demande et
résumé du formulaire
​
​
​

A chaque réponse par message de la part de Cryo, un mail est envoyé au client
pour le prévenir. Le mail contient les 20 premiers caractères du messages suivis
de “...” et d’un lien menant à MyCryo afin de l’inviter à consulter le message
entier.
Dans la liste des demandes, à chaque nouveau message reçu la carte de la
demande concernée est repérée à l’aide d’un flag bleu et d’une bulle bleue qui
s’affiche dans le menu du client.

Notion d’avis lors de la clôture d’une demande :

Attentes de précisions de la part de Cryo avant le 6 avril 2018.

A la clôture d’une demande, le client peut donner son avis sur la prestation.
Formulaire simple de 3 questions maximum à champ texte libre plus une notation
sur 5 ou 10 de la prestation en général ou liée à une question précise.
Récupération de ces avis côté Cryo sous forme d'export en fichier XLS à partir du
dashboard.
Les données extraites seront :
-​
Numéro client (de BaaN soit l’entreprise)
-​
Adresse mail du client
-​
Numéro de demande
-​
Type de demande
-​
Leader de la demande
-​
Date de l’avis
-​
Réponses de l’avis (note et commentaire)

7.3.2 - Côté Cryo
C’est la page d’accueil des employés Cryo.
Un employé Cryo a accès aux demandes de son service et aux demandes
auxquelles il est assigné en tant que leader ou collaborateur. Par défaut seules
les demandes dont il est leader et collaborateur sont affichées. Mais il peut à
l’aide d’un filtre afficher toutes les demandes de son service, c’est-à-dire pour
lesquelles son service est leader ou collaborateur.

MyCryo                                                                Author : ACME                                                                            ​
26/43


---

## Page 27

Les utilisateurs Cryo ont accès aux mêmes informations que côté client avec des
informations supplémentaires :
-​
Liste des contributeurs
-​
Possibilité d’ajouter ou de modifier un contributeurs
-​
Échanges entre tous les contributeurs/Collaborateurs de la demande
-​
Résumé des pièces jointes avec le client et entre collaborateurs,
possibilité de supprimer une pièce jointe
-​
Possibilité de changer le statut de la demande

MyCryo                                                                Author : ACME                                                                            ​
27/43


---

## Page 28

Figure 15 : Détail d'une commande de pièce de rechange côté Cryo

MyCryo                                                                Author : ACME                                                                            ​
28/43


![Image 27](images/image_p28_1_27.png)
*Image 27 - Page 28*

![Image 28](images/image_p28_2_28.png)
*Image 28 - Page 28*

![Image 29](images/image_p28_3_29.png)
*Image 29 - Page 28*

---

## Page 29

Mail : Lors d’échanges entre collaborateurs, un mail est envoyé à tous les
collaborateurs afin de les prévenir qu’un message leur a été envoyé. L’adresse
d’expédition est une adresse Cryo NoReply.
Les mails peuvent être désactivés dans la partie notification du profil.

Lors de la clôture d’une demande : un champ texte apparaît afin de renseigner le
numéro de commande client de BaaN. Possibilité d’ajouter une pièce jointe par le
collaborateur qui clôt la demande afin d’ajouter le bon de commande. Cette pièce
jointe bon de commande est d’une couleur différente dans la liste des PJ.

Changement de leader : un responsable d’équipe pourra remplacer le leader d’un
ticket associé à son équipe. Le nouveau leader fait partie de l’équipe
7.4 - Notion de devis
Lorsque le contact Cryo communique via les messages dans demandes en cours avec
le client, il a la possibilité de joindre une pièce jointe et de la notifier comme devis en
cochant une checkbox. Le message contenant cette pièce jointe devis sera alors de
couleur différente tout comme la pièce jointe dans le résumé.
Toute négociation de devis se gère dans BaaN. La pièce jointe attachée par Cryo est le
reflet de la négociation menée.
Figure 16 : Checkbox devis disponible côté Cryo lors d'échange avec le client dans une
demande

MyCryo                                                                Author : ACME                                                                            ​
29/43


![Image 30](images/image_p29_1_30.png)
*Image 30 - Page 29*

---

## Page 30

7.5 - Demandes clôturées
Liste de toutes les demandes (PdR ou de service) clôturées qui ont été faites dans le
portail MyCryo.
7.6 - Créer une demande pour un client
Cryo peut créer une demande pour un de ses clients.
Pour cela il a accès à la liste des formulaires, il renseigne le client qui doit
obligatoirement être déjà client de MyCryo à la fin du formulaire à l’aide d’un champ de
recherche.

8 - Commandes passées
Recherche par référence, numéro OV
Liste des commandes de PdR, de matériel passées :
-​
Pour la société mère (1003) : toutes les commandes liées à 1003
-​
Pour les sociétés filles (1003-1, 1003-2, …) : on affiche toutes les commandes liées à
1003
-​
La raison est que les données des commandes passées sont associées dans BaaN aux
entreprises mères et qu’on ne peut pas les récupérer au société fille.

Informations remontées de BaaN:
-​
Type de commande
-​
Numéro OV
-​
Numéro de projet
-​
Date de commande
-​
Quantité commandée
-​
Quantité livrée
-​
Date d’expédition

Si la demande est créée dans MyCryo et que le lien avec le numéro de commande de BaaN est
ajouté manuellement lors de la clôture de la demande alors les utilisateurs peuvent avoir accès
à la demande qui a été clôturée dans le portail MyCryo.

MyCryo                                                                Author : ACME                                                                            ​
30/43


---

## Page 31

Figure 17 : Liste des commandes passées

9 - Mes matériels & documentation
Les matériels (Matériel fixe MF ou matériel de transport MT) sont récupérés de BaaN à l’aide
des commandes. L’information client connue das BaaN est celle de l’entreprise mère.
9.1 - Côté client
Liste des matériels de chaque entreprise mère accessible. Seule l’entreprise mère voit la
liste de ses matériels peu importe dans quelle entreprise fille il se trouve.

Ecran intermédiaire avec :
-​
Mes matériels fixes (Photo et/ou cadre avec label)
-​
Mes matériels transportables (Photo et/ou cadre avec label)

MyCryo                                                                Author : ACME                                                                            ​
31/43


![Image 31](images/image_p31_1_31.png)
*Image 31 - Page 31*

![Image 32](images/image_p31_2_32.png)
*Image 32 - Page 31*

---

## Page 32

Puis dans chaque catégorie, chaque ligne de la liste comprend :
-​
Type de matériel
-​
Référence matériel
-​
Année
-​
Immatriculation
-​
Description
-​
Liste des pièces jointes liées à ce matériel qui correspondent à la
documentation liée à ce matériel spécifique

9.2 - Côté Cryo
Cryo a accès à la liste entière de tous les matériels qui ont été vendus.
Une fonction de recherche permet de trouver les matériels d’un client en particulier ou
d’une référence de matériel.
Chaque matériel est unique et lié à une entreprise. Ce numéro unique est remonté via
interface.
Possibilité d’ajouter/de supprimer des pièces jointes à un matériel particulier, cela
correspond à la documentation. Au cas où deux matériels MF1 et MF2 auraient la même
documentation, il faudrait attacher la documentation manuellement à chacun des
matériels

MyCryo                                                                Author : ACME                                                                            ​
32/43


![Image 33](images/image_p32_1_33.png)
*Image 33 - Page 32*

![Image 34](images/image_p32_2_34.png)
*Image 34 - Page 32*

---

## Page 33

10 - Mon compte
Coté client les champs suivant sont modifiables :
-​
Nom
-​
Poste
-​
Email
-​
Mot de passe
-​
Numéro de téléphone

Chaque utilisateur peut réinitialiser son mot de passe.
​

Chaque utilisateur (Cryo et client) peut modifier ses préférences quant aux notifications par
email.

Figure 18 : "Mon compte" côté client

MyCryo                                                                Author : ACME                                                                            ​
33/43


![Image 35](images/image_p33_1_35.png)
*Image 35 - Page 33*

![Image 36](images/image_p33_2_36.png)
*Image 36 - Page 33*

---

## Page 34

11 - Gestion des comptes​
Le super administrateur de MyCryo peut ajouter, modifier ou suspendre des comptes utilisateurs
ou employés Cryo.​
​

11.1 - Création de compte client
Il y a 3 différentes façons de demander la création d’un compte client :
11.1.1 - Demande de création par un simple visiteur
Les visiteurs peuvent faire une demande de création de compte en remplissant
un formulaire comprenant les champs suivants :
-​
Nom
-​
Prénom
-​
Société
-​
Fonction
-​
Adresse
-​
Ville
-​
Code Postal
-​
Téléphone
-​
Mobile
-​
Email
​
Tous les champs sont libres : textfields
L’utilisateur valide ensuite sa demande de création de compte qui est envoyée à
Cryo.
Cryo peut alors valider cette demande d’inscription, un email est envoyé au client
avec un lien vers l’initialisation du mot de passe
L’administrateur Cryo qui valide la demande affecte l’entreprise à l’aide du code
client qu’il récupère de BaaN. L’entreprise est renseignée automatiquement
lorsque l’on renseigne le code client.

11.1.2 - Demande de création par un client
Un client qui a le rôle de modérateur a le droit de créer un compte pour un de ses
employés.
Il a accès au même formulaire de demande d’inscription que les visiteurs mais
l’entreprise et son adresse sont déjà renseignées et ne sont pas modifiables.
Il doit alors renseigner les champs suivants :

MyCryo                                                                Author : ACME                                                                            ​
34/43


---

## Page 35

-​
Nom
-​
Prénom
-​
Fonction
-​
Téléphone
-​
Mobile
-​
Email
Le processus de validation de compte est le même, un employé Cryo doit valider
la demande de création de compte, mais le mail du demandeur sera renseigné.

Figure 19 : Demande création de compte par un visiteur/lecteur
11.1.3 - Création par un employé Cryo
Un employé Cryo a la possibilité de créer un compte pour un client. Le formulaire
est le même que pour la validation d’une demande de création de compte.
Le compte sera alors validé automatiquement et le client recevra directement un
mail pour initialiser son mot de passe.

11.2 - Validation de compte client
Cryo reçoit toutes les demandes de création de compte.
La liste de toutes les demandes comprend :

MyCryo                                                                Author : ACME                                                                            ​
35/43


![Image 37](images/image_p35_1_37.png)
*Image 37 - Page 35*

![Image 38](images/image_p35_2_38.png)
*Image 38 - Page 35*

---

## Page 36

-​
Le demandeur (visiteur ou adresse mail du client demandeur)
-​
Le nom
-​
Le  prénom
-​
L’entreprise
-​
La fonction
-​
La date de demande

Les administrateurs Cryo peuvent alors valider ou supprimer une demande d’inscription.
Pour valider une demande d’inscription il faut renseigner le code client correspondant à
l’entreprise donnée par le client. Pour trouver la bonne entreprise, l’employé Cryo s’aide
du champ texte “Entreprise” qu’a renseigné le client ainsi que de l’adresse.
L'entreprise et l’adresse du client du client sont alors liées à l’aide du code client qu’il
récupère de BaaN.
Lors de la validation les administrateurs ont aussi la possibilité de modifier chaque
champs de la demande.
Un email est ensuite envoyé au client avec un lien vers l’initialisation de son mot de
passe.
11.3 - Gestion des utilisateurs clients

Figure 20 : Validation d'un compte client côté Cryo

Cryo peut :
-​
Rechercher un client
-​
Accéder à la liste des clients et la possibilité de modifier les champs suivants :
-​
Nom
-​
Prénom

MyCryo                                                                Author : ACME                                                                            ​
36/43


![Image 39](images/image_p36_1_39.png)
*Image 39 - Page 36*

![Image 40](images/image_p36_2_40.png)
*Image 40 - Page 36*

---

## Page 37

-​
Entreprise
-​
Date de création​

-​
Accéder à la liste de clients dont la demande de création de compte n’a pas été
validée mais supprimée.
-​
Modifier la fiche d’un client et modifier ses droits : créateur ou modérateur

11.4 - Gestion des utilisateurs Cryo
​

Figure 21 : Gestion des utilisateurs Cryo

​
Un responsable Cryo peut :
-​
Rechercher un utilisateur Cryo
-​
Accéder à la liste des utilisateurs de son service et la possibilité de
modifier les champs suivants :
-​
Mail

MyCryo                                                                Author : ACME                                                                            ​
37/43


![Image 41](images/image_p37_1_41.png)
*Image 41 - Page 37*

![Image 42](images/image_p37_2_42.png)
*Image 42 - Page 37*

---

## Page 38

-​
Nom
-​
Prénom
-​
Statut (“Actif” ou “Inactif”)

Seul le super administrateur peut créer un compte administrateur en assignant
l’administrateur à une équipe (cf 2. Description générale du besoin - Profil utilisateur
-Cryo) et au droit “Employé”, “Responsable” ou “Super administrateur”. Un mail est
envoyé au nouvel utilisateur pour qu’il initialise son mot de passe.
Il est le seul à pouvoir éditer les droits, l’équipe de l’utilisateur et à le mettre “actif” ou
“inactif”.

Figure 22 : Ajout d’un utilisateur Cryo par un super administrateur

12 - Mes contacts Cryo
Les clients ont accès à un onglet “Contact” qui leur permet de trouver les informations
nécessaires pour contacter un employé Cryo. Il y a deux types de contacts :​

MyCryo                                                                Author : ACME                                                                            ​
38/43


![Image 43](images/image_p38_1_43.png)
*Image 43 - Page 38*

![Image 44](images/image_p38_2_44.png)
*Image 44 - Page 38*

---

## Page 39

12.1 - Contact privilégié
C’est un contact dynamique. Il comprend l’employé Cryo responsable d’une/des
demandes faites par le client :
-​ Nom
-​ Fonction
-​ Téléphone fixe + portable
-​ Mail
Le contact est remonté automatiquement de BaaN. Il est lié à l’entreprise du client.

### 12. 2 - Contacts génériques
Les contacts génériques sont une liste de contacts Cryo à contacter en fonction des
activités :
●​ Nom
●​ Fonction
●​ Téléphone fixe + portable
●​ Mail
Ces contacts ne sont pas dynamiques, la liste doit être fournie par MyCryo. Ex :
Responsable pièces de rechange, responsable SAV, etc ..

13 - Mesures de performances​

Des indicateurs de performances seront mesurés sur la fréquentation et l’efficacité du site via
Google Analytics mais l’efficacité sera calculée en plus. C’est le taux de conversion de visiteurs
en utilisateurs, ou le rapport entre les visiteurs ayant effectués une action (par ex. une demande
de création de compte, une demande d’information, un devis, ...) et le nombre total de visiteurs

14 - Attentes de la part de Cryo
14.1 - Nom de domaine
Cryo s’engage à fournir à ACME un nom de domaine pour la plateforme MyCryo et qui
permettra l’envoi de mail avec une adresse de Cryo.

MyCryo                                                                Author : ACME                                                                            ​
39/43


---

## Page 40

Ex : MyCryo.com

14.2 - Exigences interfaces​ ​

14.2.1 - Interfaces fournies pour le développement
Ces interfaces servent à comprendre les données pour démarrer les
développements
Cryo s’engage à fournir à ACME des interfaces propres et complètes en fichiers
CSV. Chaque table comprend les titres des colonnes fixes et sont
compréhensibles. Et chaque colonne
Chaque donnée est au bon format, dans la bonne colonne et dans la bonne
ligne.

Figure 23 : Exemple de l’interface client sous format XLS avec le type des données (à titre
d’exemple)

Les données exploitées seront uniquement celles présentes dans les écrans UX
et dans ces spécifications.

14.2.2 - Interfaces fournies pour l’utilisation du portail MyCryo
Ces interfaces servent à intégrer les données au portail, une fois les
développements effectués
Cryo s’engage à fournir à ACME des interfaces propres et complètes en fichiers
CSV plat. Chaque table comprend les titres des colonnes fixes et sont

MyCryo                                                                Author : ACME                                                                            ​
40/43


![Image 45](images/image_p40_1_45.png)
*Image 45 - Page 40*

---

## Page 41

compréhensibles. Chaque donnée est au bon format, dans la bonne colonne et
dans la bonne ligne.
​
​
​

Interface
Première
intégration
Initialisation
Mise à jour quotidienne
Commentaires
Stock
Fichier complet
Fichier complet
Les stocks ne peuvent pas être
“null” (soit une valeur vide). Ils
doivent contenir un 0
numérique si il n’y a pas de
stock
Clients
Fichier complet
Fichier complet

Historique de
commande
Fichier complet
Uniquement commandes
modifiées et nouvelles
Opération faite lors de l’import :
mise à jour ou ajout
Liste de
matériels
Fichier complet
Uniquement matériels
modifiés et nouveaux
Opération faite lors de l’import :
mise à jour ou ajout
Fichiers
manuels
(Catalogue,
tarif)
Fichier complet
Fichier complet
Rajouter une colonne avec
valeur = SUPPR pour les
produits à supprimer

A rediscuter : veut-on supprimer des commandes ou des matériels ? Dans le cas positif,
modifier l’import.

Pour l’interface client, il y a un fichier clients_meres et un fichier clients_filles ayant le
même format (nom de colonnes, type de données). L’adresse récupérée en tant
qu’adresse principale sera :
-​
pour les entreprises filles l’adresse de livraison
-​
pour les entreprises mères l’adresse postale

Chaque ligne avec un identifiant unique doit être unique, pas de doublons (ex : une
seule ligne pour un client qui a un unique numéro client).

MyCryo                                                                Author : ACME                                                                            ​
41/43


---

## Page 42

14.3 - Livraisons de données ​
​
​

Le délai de développement est de 18 semaines, sous réserve de disponibilité des
informations complètes et finalisées à la date indiquée ci-dessous.

Cryo s’engage ainsi à fournir à ACME :

Livrable
Date de livraison
attendue
Les interfaces de BaaN avec au moins 40 lignes de données pour
chaque table pour aider au développement de la base de données
MyCryo

06 Avril 2018
La liste des contacts de la page « Mes contacts Cryo »
06 Avril 2018
Le wording des emails et des écrans à envoyer en tant que
notification et le groupe de la notification (pour désactiver les
notifications mails par groupe)
Scope :
-​
Pages et mails liés à la connexion, mot de passe perdu
-​
Pages et mails liés à la créations de comptes (clients, Cryo)
-​
Pages et mails liés à la gestion des utilisateurs (clients et
Cryo)
06 Avril 2018
Les images/pictogrammes des catégories de PdR en bonne qualité

16 Avril 2018
Le wording des emails et des écrans à envoyer en tant que
notification et le groupe de la notification (pour désactiver les
notifications mails par groupe)
Scope :
-​
Catalogue
-​
Services
-​
Demandes
-​
Mon profil
-​
Mes commandes
-​
Mes matériels
16 Avril 2018
Un rappel sur le listing des mails : définir pour les emails, les caractéristiques suivantes

MyCryo                                                                Author : ACME                                                                            ​
42/43


---

## Page 43

-​
Cas d’envoi (création de compte, ajout d’un collaborateur, changement de statut, ...)
-​
Envoyé par
-​
Reçu par
-​
Type de notification (groupement des mails en “types de notification” pour pouvoir
désactiver ces envois de mails par type (si souhaité))
-​
Objet du mail
-​
Contenu du mail​

Table des figures

Figure 1 : Tableau de répartition des types de demandes et des visibilités associées​
6
Figure 2 : Principe des tarifications associées aux comptes client​
7
Figure 3 : Écran de connexion​
8
Figure 4 : Écran d’accueil d’un client connecté​
9
Figure 5 : Dashboard super administrateur (gauche), dashboard responsable CRYS (droite)​ 12
Figure 6 : Catégories du catalogue​
13
Figure 7 : Liste des articles du catalogue dans une catégorie​
14
Figure 8 : Panier de commande, client connecté​
15
Figure 9 : Adresse d’expédition, dernière étape avant validation de la demande​
16
Figure 10 : Liste des formulaires​
19
Figure 11 : Informations identitaires demandées en fin de formulaire si le client n’est pas
connecté​
20
Figure 12 : Liste des demandes vue par un responsable de service Cryo​
21
Figure 13 : Liste des demandes en cours côté client​
24
Figure 14 : Détail d'une commande de pièce de rechange faites par le catalogue côté client
(gauche) Détail d’une demande faites via un formulaire côté client (droite)​
25
Figure 15 : Détail d'une commande de pièce de rechange côté Cryo​
27
Figure 16 : Checkbox devis disponible côté Cryo lors d'échange avec le client dans une
demande​
28
Figure 17 : Liste des commandes passées​
30
Figure 18 : "Mon compte" côté client​
32
Figure 19 : Demande création de compte par un visiteur/lecteur​
34
Figure 20 : Validation d'un compte client côté Cryo​
35
Figure 21 : Gestion des utilisateurs Cryo​
36
Figure 22 : Edition d’un utilisateur Cryo par un super administrateur​
37
Figure 23 : Exemple de l’interface client sous format XLS avec le type des données​
39

MyCryo                                                                Author : ACME                                                                            ​
43/43


---
