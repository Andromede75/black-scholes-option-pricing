Black-Scholes Option Pricing Model

Ce projet implémente le modèle de Black-Scholes pour calculer les prix des options européennes de type call et put. Il vise à fournir une démonstration pratique de la modélisation des options et à faciliter la compréhension des concepts clés liés aux marchés financiers.

Fonctionnalités

Calcul du prix d'une option call européenne.

Calcul du prix d'une option put européenne.

Visualisation des prix des options en fonction du prix de l'action.

Support de plusieurs paramètres :

Prix de l’action actuelle.

Prix d’exercice.

Temps jusqu’à l’échéance.

Taux d’intérêt sans risque.

Volatilité de l’action.

Installation

Cloner le dépôt GitHub :

git clone https://github.com/Andromede75/black-scholes-option-pricing.git
cd black-scholes-option-pricing

Créer un environnement virtuel (recommandé) :

python -m venv env
source env/bin/activate  # Sur Linux/Mac
env\Scripts\activate  # Sur Windows

Installer les dépendances :

pip install -r requirements.txt

Utilisation

Exécuter le script principal :

python "Black Scholes Option Pricing.py"

Lors de l'exécution, le script :

Affiche les prix des options call et put dans la console.

Génère des graphiques montrant l’évolution des prix des options en fonction du prix de l’action.

Exemples de résultats

Résultats affichés dans la console

Black-Scholes Call Option Price: 10.45
Black-Scholes Put Option Price: 5.57

Graphique généré



Explications techniques

Le modèle de Black-Scholes repose sur les hypothèses suivantes :

Le marché est frictionless (pas de coûts de transaction ni de taxes).

Il est possible de vendre à découvert sans restriction.

Il n’y a pas de paiements de dividendes pendant la durée de vie de l’option.

Le taux d’intérêt sans risque et la volatilité sont constants.

Les formules utilisées pour les options européennes de type call et put sont les suivantes :

Formule pour une option call

Où :

Formule pour une option put

Améliorations possibles

Ajout du calcul des Greeks : Delta, Gamma, Theta, Vega, Rho.

Support des options américaines (via des méthodes numériques comme les arbres binomiaux).

Interface utilisateur interactive avec Streamlit.

Auteurs

Mathieu Derville – GitHub

Licence

Ce projet est sous licence MIT - voir le fichier LICENSE pour plus de détails.

Références

Documentation officielle de NumPy

Documentation officielle de SciPy

Black-Scholes Model - Investopedia
