# 🧠 Sentiment Analysis — Amazon Product Reviews

> **Prompt Engineering appliqué à la classification de sentiments sur des avis clients Amazon**

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-412991?style=for-the-badge&logo=openai&logoColor=white)
![HuggingFace](https://img.shields.io/badge/Dataset-Amazon_Polarity-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)

*Exploration des stratégies Zero-Shot · Few-Shot · Chain-of-Thought avec GPT-4o*

---

## 📋 Table des matières

- [Vue d'ensemble](#-vue-densemble)
- [Structure du projet](#-structure-du-projet)
- [Installation](#️-installation)
- [Dataset](#-dataset)
- [Méthodologie](#-méthodologie)
- [Résultats](#-résultats)
- [Références](#-références)

---

## 🎯 Vue d'ensemble

Ce projet applique des techniques de **Prompt Engineering** à l'analyse de sentiments sur des avis clients Amazon. Nous évaluons trois stratégies de prompting avec **GPT-4o** pour classifier les avis en **positif** ou **négatif**, et mesurons les performances via le **score micro-F1** sur plusieurs runs.

Ce travail s'inscrit dans le cadre des **Systèmes Multi-Agents**, où des agents spécialisés peuvent être orchestrés avec des prompts optimisés pour des tâches NLP spécifiques.

---

## 📁 Structure du Projet

```
sentiments_analysis/
├── sa.ipynb              # Notebook principal
├── main.py               # Script Python principal
├── requirements.txt      # Dépendances Python
├── .gitignore
└── README.md
```

---

## 🛠️ Installation

```bash
# 1. Cloner le repository
git clone https://github.com/awabenzekry/sentiment_analysis.git
cd sentiment_analysis

# 2. Créer un environnement virtuel
python -m venv .venv
source .venv/bin/activate        # Linux / macOS
.venv\Scripts\activate           # Windows

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Configurer les variables d'environnement
# Créer un fichier .env avec :
OPENAI_API_KEY=sk-...

# 5. Lancer Jupyter
jupyter notebook sa.ipynb
```

---

## 📊 Dataset

### Amazon Polarity

Le dataset `amazon_polarity` (HuggingFace) contient des avis clients Amazon annotés :

| Caractéristique | Valeur |
|----------------|--------|
| Taille train | 3 600 000 avis |
| Taille test | 400 000 avis |
| Classes | positive / negative |
| Équilibre | 50% / 50% |
| Colonnes | `label`, `title`, `content` |

**Pourquoi Amazon plutôt qu'IMDB ?**

| | IMDB | Amazon Polarity |
|-|------|----------------|
| Domaine | Critique cinéma | Avis produits |
| Langage | Nuancé, complexe | Direct, concret |
| Mots-clés | Moins marqués | `broken`, `love it`, `waste`... |
| Taille | 25 000 | 3 600 000 |

---

## 🔬 Méthodologie

### Pipeline général

```
Dataset Amazon Polarity
        │
        ├──► Examples Pool (80%) ──► Few-Shot Examples ──┐
        │                                                  │
        └──► Gold Examples (20 avis fixes) ◄──────────────┤
                                                           │
                                              evaluate_prompt()
                                                           │
                                              Micro F1-Score
```

### Prompt 1 — Zero-Shot

Aucun exemple fourni, instruction directe :

```
Classify the sentiment of Amazon product reviews as 'positive' or 'negative'.
Amazon reviews will be delimited by triple backticks.
Answer only 'positive' or 'negative'. Do not explain your answer.
```

### Prompt 2 — Few-Shot

8 exemples équilibrés (4 positifs + 4 négatifs) organisés aléatoirement pour éviter :
- Le **biais de l'étiquette majoritaire**
- Le **biais de récence**

### Prompt 3 — Chain-of-Thought (CoT)

Ajout d'instructions de raisonnement étape par étape :

```
Instructions:
1. Carefully read the review and identify key sentiment signals.
2. Consider strong indicator words (excellent, broken, love, terrible, waste...)
3. Consider the overall tone and context.
4. Estimate the probability of the review being positive.
```

---

## 🏆 Résultats

### Évaluation sur 20 Gold Examples

| Stratégie | Micro F1-Score |
|-----------|---------------|
| Zero-Shot | — |
| Few-Shot | — |
| CoT | — |

### Analyse de Stabilité — 10 Runs

| Métrique | Few-Shot | CoT |
|---------|---------|-----|
| F1 Moyen | — | — |
| Std | — | — |
| Stabilité | ✅ | ✅ |

### Conclusions

- Le langage Amazon est plus **direct** → meilleure performance Zero-Shot vs IMDB
- Les mots-clés forts facilitent la classification pour le LLM
- Le **CoT** améliore l'interprétabilité sans sacrifier les performances
- La stabilité sur 10 runs confirme la robustesse des stratégies

---

## 📚 Références

- [LangChain Documentation](https://docs.langchain.com/)
- [OpenAI API Reference](https://platform.openai.com/docs)
- [Amazon Polarity Dataset — HuggingFace](https://huggingface.co/datasets/amazon_polarity)
- [scikit-learn F1-Score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html)

---

**👩‍💻 Auteure : Awa Aimée Benzekry**  
**📅 2025/2026 · 🎓 HESTIM **
