# TP2 - Analyse d'algorithmes
## 3-Coloration (probleme NP-complet)

**Auteurs:** Achille GRAVOUIL Elias CUZEAU
**Cours:** INFO003 - M2

---

## Structure

```
main.py          -> Programme principal (appels via match)
graph.py         -> Classe Graph
src/             -> Fonctions principales
util/            -> Generateurs de graphes
```

---

## Utilisation

```bash
python main.py biparti util/graph.dimacs
python main.py 3col util/graph.dimacs
python main.py verifier util/graph.dimacs 0,1,2
```

---

## Section 1 : 2-Coloration

### Complexite de l'algorithme ?

**O(V + E)** avec V = sommets, E = aretes

Pourquoi :
- On parcourt chaque sommet une fois avec BFS -> O(V)
- On regarde chaque arete une fois -> O(E)
- Total : O(V + E)

Le temps reel correspond bien a cette complexite. C'est lineaire, on ne peut pas faire mieux car il faut lire tout le graphe.

---

## Section 2 : 3-Coloration

### Question 1 : Verification

**O(V + E)** (polynomiale)

Pourquoi :
- On verifie chaque sommet a une couleur valide -> O(V)
- On verifie chaque arete ne relie pas 2 sommets de meme couleur -> O(E)

C'est polynomial donc 3-Col est dans NP (on peut verifier une solution rapidement).

### Question 3 : Complexite du backtracking ?

**O(3^V)** dans le pire cas

Pourquoi :
- Pour chaque sommet, on teste 3 couleurs
- On a V sommets
- Donc au max 3 x 3 x ... x 3 = 3^V possibilites

C'est exponentiel, ce qui est normal car 3-Col est NP-complet. En pratique, le backtracking coupe souvent des branches tot quand il detecte un conflit.

**Memoire : O(V)** car la recursion va au max a profondeur V.
