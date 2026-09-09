---
noteId: "94c4eb90ac3a11f1b84419318db76634"
tags: []

---

# TP Déploiement

Ce projet met en place une pipeline CI/CD avec GitHub Actions, Docker, Docker Hub et une VM Azure.

## Fonctionnement du pipeline

À chaque `push` sur la branche `main`, GitHub Actions lance automatiquement :

```text
Push sur main
      ↓
Tests unitaires
      ↓
Tests E2E
      ↓
Build de l'image Docker
      ↓
Push sur Docker Hub
      ↓
Déploiement SSH sur la VM
      ↓
Test /health
```

Si un test échoue, les étapes suivantes ne sont pas exécutées.

## Déclenchement

Le déploiement est entièrement automatique à chaque push sur `main`.

```yaml
on:
  push:
    branches:
      - main
```

Aucune action manuelle n'est nécessaire après le push.

## Choix techniques

L'application utilise **Python / Flask**, les tests sont réalisés avec **pytest** et l'application est conteneurisée avec **Docker**.

Flask écoute sur le port `8080` dans le conteneur. Sur la VM, nous avons choisi le port `8087`, car plusieurs autres ports étaient déjà utilisés par les applications des autres étudiants.

```text
VM :8087 -> Conteneur :8080 -> Flask :8080
```

L'image est envoyée sur **Docker Hub**, puis récupérée automatiquement sur la VM via SSH.

Les identifiants Docker Hub et SSH sont stockés dans les **GitHub Secrets** et ne sont pas présents directement dans le dépôt.

Le déploiement est idempotent : le conteneur `mra-app` existant est supprimé avant de recréer la nouvelle version.

L'application est vérifiée avec :

```text
GET /health
```

Le service fonctionne bien directement sur la VM avec le port `8087`. En revanche, il n'est pas accessible depuis l'extérieur car la configuration réseau / pare-feu de la VM ne permet pas l'ouverture de ce port vers Internet.


© 2026 Abdoullah Mujeebur Rahaman