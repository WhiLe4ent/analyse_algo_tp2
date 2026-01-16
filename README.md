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
# Section 1 : Test biparti (2-coloration)
python main.py biparti graphs/graph.dimacs

# Section 2 : 3-coloration
python main.py 3col graphs/graph.dimacs
python main.py verifier graphs/graph.dimacs 0,1,2

# Section 3.1-3.2 : Clique et EnsInd via SAT-solver
python util/CliqueFromPycosat.py graphs/graph.dimacs 3 [-v]
python util/EnsIndFromPycosat.py graphs/graph.dimacs 2 [-v]

# Section 3.3 : 3CouvertureParCliques
python main.py 3couv graphs/graph.dimacs
```

---

## Section 1 : 2-Coloration

### Complexite de l'algorithme ?

**O(V^2)** avec V = sommets

Pourquoi :
- On parcourt chaque sommet une fois avec BFS -> O(V)
- Pour chaque sommet, on parcourt tous les V sommets pour trouver les voisins (matrice d'adjacence) -> O(V)
- Total : O(V^2)

Note : avec une liste d'adjacence, ce serait O(V + E). Mais notre implementation utilise une matrice d'adjacence, donc la recherche des voisins est en O(V) par sommet.

---

## Section 2 : 3-Coloration

### Question 1 : Verification

**O(V^2)** (polynomiale)

Pourquoi :
- On verifie chaque sommet a une couleur valide -> O(V)
- On parcourt la matrice d'adjacence pour verifier les aretes -> O(V^2)

C'est polynomial donc 3-Col est dans NP (on peut verifier une solution rapidement).

### Question 3 : Complexite du backtracking ?

**O(3^V)** dans le pire cas

Pourquoi :
- Pour chaque sommet, on teste 3 couleurs
- On a V sommets
- Donc au max 3 x 3 x ... x 3 = 3^V possibilites

C'est exponentiel, ce qui est normal car 3-Col est NP-complet. En pratique, le backtracking coupe souvent des branches tot quand il detecte un conflit.

**Memoire : O(V)** car la recursion va au max a profondeur V.

---

## Section 3 : SAT-solver et reductions

### Section 3.1-3.2 : EnsInd via SAT-solver

Le probleme Ensemble Independant (EnsInd) est l'oppose de Clique :
- **Clique** : trouver k sommets tous connectes entre eux
- **EnsInd** : trouver k sommets sans aucune arete entre eux

Implementation dans `util/EnsIndFromPycosat.py` :
- Adaptation minimale de `CliqueFromPycosat.py`
- Seule difference : on ajoute la contrainte `[-u, -v]` quand il Y A une arete (au lieu de quand il n'y en a pas)

### Section 3.3 : 3CouvertureParCliques via reduction a 3Col

**Probleme** : Peut-on couvrir tous les sommets d'un graphe G avec 3 cliques ?

**Observation cle** : Dans une 3-coloration, les sommets de meme couleur forment un ensemble independant. Or, un ensemble independant dans G est une clique dans le graphe complementaire G'.

**Reduction** : `3CouvertureParCliques(G) <=> 3Col(G')`

ou G' est le graphe complementaire de G (arete dans G' ssi pas d'arete dans G).

**Consequence** : Si 3Col est NP-complet, alors 3CouvertureParCliques est aussi NP-complet (reduction polynomiale).
