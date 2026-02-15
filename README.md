# 🛒 Tracker de Prix Alimentaires — Sénégal

**Système automatisé de monitoring des prix alimentaires et de conformité réglementaire**

---

## 📋 Contexte

Au Sénégal, l'alimentation représente **43,2% de l'Indice Harmonisé des Prix à la Consommation (IHPC)**, avec des disparités marquées entre zones urbaines (39% à Dakar) et rurales (68%). Pour une famille moyenne de 4 personnes, cela correspond à un budget mensuel de **80 000 à 120 000 FCFA**.

Face à cette réalité, le gouvernement sénégalais a publié l'**arrêté n°09852 du 24 juin 2024** portant administration de prix plafonds sur 6 produits de première nécessité, mobilisant **53,4 milliards FCFA de subventions**.

**Problématique** : Aucun outil public ne permet actuellement de vérifier l'application effective de ces prix administrés sur le terrain. Les consommateurs ne peuvent pas comparer facilement les prix pratiqués aux prix officiels, identifier les plateformes conformes, ou détecter les promotions.

Ce projet répond à ce besoin de **transparence** en créant un système automatisé de monitoring des prix alimentaires à partir des plateformes e-commerce sénégalaises.

---

## 🎯 Objectifs

### Objectif principal
Développer un **système automatisé de monitoring des prix alimentaires** capable de :
- Comparer en temps réel les prix e-commerce avec les prix administrés
- Catégoriser automatiquement les produits selon leur conformité réglementaire
- Fournir une visualisation interactive accessible aux consommateurs et régulateurs

### Objectifs spécifiques

#### 📊 Techniques
- Scraper quotidiennement **6 plateformes e-commerce** (Auchan.sn, Sakanal.sn, Tongtong, Senboutique, Niokobok, Sooretul)
- Extraire les **prix officiels** depuis les sites gouvernementaux
- Collecter les données pour **14 denrées prioritaires** couvrant 70-75% du budget alimentaire
- Stocker l'historique dans une base MySQL avec horodatage

#### 🎨 Visualisation
- Dashboard interactif **Plotly Dash** avec 3 vues :
  - **Tableau de conformité** avec badges colorés 🟢🟡🔴
  - **Évolution temporelle** des prix par produit
  - **Comparaison inter-plateformes**

#### 🔄 Automatisation
- Exécution quotidienne automatisée via **Cron** (02h)
- Pipeline complet : extraction → nettoyage → catégorisation → stockage → visualisation

#### 📈 Impact social
- **Consommateurs** : Vérification prix + optimisation pouvoir d'achat
- **Autorités** : Monitoring effectivité des politiques tarifaires
- **Transparence** : Accès public à l'information en temps réel

---

## 🏗️ Architecture du Projet

### Stack Technologique
- **Web Scraping** : Scrapy, BeautifulSoup4
- **Base de données** : MySQL
- **Visualisation** : Plotly Dash
- **Orchestration** : Cron / Airflow
- **Tests** : Pytest

### Structure des dossiers

```
senegal-food-tracker/
│
├── docs/                  # 📄 Documentation (CDC, rapports)
├── config/                # ⚙️ Configuration (BDD, settings)
├── scrapers/              # 🕷️ Scripts extraction par site
├── models/                # 📊 Modèles de données
├── pipeline/              # 🔄 Traitement (nettoyage, catégorisation)
├── dashboard/             # 📈 Interface Dash
├── sql/                   # 🗄️ Schéma MySQL
├── tests/                 # ✅ Tests unitaires
├── utils/                 # 🛠️ Logger + helpers
├── data/                  # 💾 Données brutes/traitées
├── logs/                  # 📝 Fichiers logs
├── scripts/               # ▶️ Scripts exécution
└── notebooks/             # 📓 Exploration Jupyter
```
  
### 14 Denrées suivies

**Niveau 1 (MVP)** :
- Riz brisé, Huile végétale, Sucre, Farine, Lait poudre, Concentré tomate

**Niveau 2 (Extension)** :
- Oignon, Poisson conserves, Pâte arachide, Bouillon cube, Mil, Pâtes, Poulet, Pomme de terre

---
  
---

## 👥 Équipe

**Analystes Statisticiens**

- **Papa Magatte Diop**
- **Marc Mare**
- **Ndeye Aissatou Cisse**
- **Aissatou Gueye**
- **Pape Mamadou Badji**

*Projet académique — Web Scraping 2026*

---
  
## 📄 Licence

Ce projet est développé dans un cadre académique.

---
  
---

**Dernière mise à jour** : Février 2026
