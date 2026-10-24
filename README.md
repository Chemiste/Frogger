# Frogger - Projet Python

Projet d'apprentissage du développement en Python : un jeu inspiré de **Frogger**, réalisé avec les bibliothèques **pygame** et **pygame_gui**.

## 🎮 Le jeu

- **Commandes** : les quatre flèches du clavier. À chaque appui, la grenouille saute d'une case dans la direction choisie, avec une animation de saut.
- **But** : traverser les rangées de véhicules (voitures et camions) et atteindre l'un des 5 emplacements libres en haut de l'écran.
- **Mort** : toucher un véhicule, entrer dans la rangée du haut ailleurs que dans un emplacement, ou entrer dans un emplacement déjà occupé. La grenouille retourne alors au départ et le joueur perd une vie (3 vies au départ).
- **Score** : 10 points par saut vers le haut, 50 points par emplacement rempli, 1000 points quand les 5 emplacements sont remplis.
- **Limite actuelle** : quand il n'y a plus de vie, le jeu s'arrête de réagir (l'écran de fin de partie n'est pas encore réalisé).

## 📁 Structure du projet

Le projet suit le standard de l'écosystème Python (Src Layout) pour une meilleure organisation et une séparation propre entre le code source, les tests et les fichiers de configuration :

```text
Frogger/
├── .venv/                  # Environnement virtuel Python isolé (à ne pas versionner)
├── src/
│   └── frogger/            # Package principal
│       ├── main.py         # Point d'entrée : boucle de jeu
│       ├── config.py       # Constantes du jeu (grille, tailles, vies, scores, DEBUG)
│       ├── level_config.py # Description des rangées de véhicules
│       ├── graphics.py     # Fonctions communes d'affichage (chargement d'image, debug)
│       ├── entities/       # Ce qui apparaît à l'écran : grenouille, véhicules, goals, icône de vie
│       ├── enums/          # Énumérations : directions, résultat d'une collision, type de véhicule
│       ├── hud/            # Affichage et état du joueur : vies et score
│       ├── rows/           # Rangées : véhicules (Row) et emplacements du haut (RowGoal)
│       └── assets/         # Images (grenouille, véhicules, décors)
├── tests/                  # Tests unitaires (vides pour le moment)
├── requirements.txt        # Dépendances Python du projet
├── ruff.toml               # Configuration de l'analyse de code (Ruff)
├── AMELIORATIONS.md        # Suivi des améliorations restantes du code existant
└── README.md               # Documentation du projet
```

---

## 🛠️ Configuration de l'environnement de développement (Fedora)

### 1. Création de l'environnement virtuel
L'environnement virtuel doit impérativement être créé à la racine du projet (dans `Frogger/`) :
```bash
python -m venv .venv
```

Pour l'activer :
```bash
source .venv/bin/activate
```

### 2. Installation des packages Python
Une fois les dépendances système installées et l'environnement virtuel activé :
```bash
pip install -r requirements.txt
```
---

## ▶️ Lancer le jeu

Depuis la racine du projet (dans `Frogger/`), avec l'environnement virtuel activé :
```bash
python -m src.frogger.main
```

---

## ⚙️ Configuration du jeu

- `src/frogger/config.py` : taille de la grille (`COLS`, `ROWS`, `CELL_SIZE`), nombre de vies, points, nombre de goals, tailles de la grenouille... Passez `DEBUG = True` pour afficher les rectangles de collision.
- `src/frogger/level_config.py` : les rangées de véhicules (sens de circulation et type de véhicule pour chaque rangée).

---

## 🧹 Qualité du code

Le projet utilise **Ruff** pour repérer les erreurs, les problèmes de nommage et de style. La configuration est dans `ruff.toml`. Ruff n'est pas dans `requirements.txt` : à installer dans l'environnement virtuel si besoin.
```bash
pip install ruff
ruff check src      # signale les problèmes
ruff format src     # reformate le code
```
