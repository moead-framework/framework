---
title: 'Moead-framework : a modular MOEA/D python framework'
tags:
  - Python
  - optimization
  - Multi-objective
  - moead
  - framework
authors:
  - name: Geoffrey Pruvost
    affiliation: "1" 
  - name: Bilel Derbel
    affiliation: "1" 
  - name: Arnaud Liefooghe
    affiliation: "1" 
affiliations:
  - name: Univ. Lille, CNRS, Inria, Centrale Lille, UMR 9189 CRIStAL, F-59000 Lille, France
    index: 1


date: 1 December 2020
bibliography: paper.bib

# Optional fields if submitting to a AAS journal too, see this blog post:
# https://blog.joss.theoj.org/2018/12/a-new-collaboration-with-aas-publishing
# aas-doi: 10.3847/xxxxx <- update this with the DOI from AAS once you know it.
# aas-journal: Astrophysical Journal <- The name of the AAS journal.
---

# Summary

The Multi-Objective Evolutionary Algorithm based on Decomposition (MOEA/D) is a general-purpose algorithm 
for approximating the Pareto set of multi-objective optimization problems [@moead]. It decomposes the original 
multi-objective problem into a number of 
single-objective optimization sub-problems and then uses an evolutionary process to optimize these 
sub-problems simultaneously and cooperatively. MOEA/D is a state-of-the-art algorithm in aggregation-based 
approaches for multi-objective optimization.

The goal of the *moead-framework* python package is to provide a modular framework for scientists and 
researchers interested in experimenting with MOEA/D and its numerous variants.


# Statement of Need

The MOEA/D algorithm is now considered as a framework. MOEA/D is the basis of many variants that improve or 
add new components to improve MOEA/D performance.
The first version of MOEA/D and its most famous variants [@moead_de; @moead_dra] are implemented in recent multi-objective 
optimization software such as pymoo [@pymoo], pygmo [@pygmo] and jMetal [@jmetal]. These implementations offer 
many state-of-the-art algorithms, visualization tools or parallelization abstraction, but they are not modular 
enough to test easily all MOEA/D components.
The modular R package MOEADr [@Campelo_2020] focuses on MOEA/D and allows the definition of different variants for 
each component of MOEA/D. While some modular frameworks already exist in Python for evolutionary algorithms 
such as DEAP [@DEAP_JMLR2012] or ModEA [@vanrijn2016], these do not (easily) support implementing MOEA/D variants. 
Instead, they focus mostly on single-objective optimization and CMA-ES variants respectively.

With the *moead-framework* package, we aim to provide the modularity of the MOEADr package by 
using the flexibility of Python. Indeed, we want to allow the user to update the behavior of MOEA/D 
components in their research works without being limited by the package itself. 
The package is focused on a modular architecture for easily adding, updating or testing the components of 
MOEA/D and for customizing how components interact with each other. Indeed, in contrast with other existing implementations, 
*moead-framework* does not limit the users with a limited number of components available as parameters (8 components are available 
in MOEADr). Users can easily restructure the 10 existing components of the *moead-framework* and include new ones to easily add new features without 
altering existing components. Components are not only customizable with parameters as with MOEADr, but in fact they can be added
with the inheritance mechanism on the main run() method of each algorithm.

For example, the *moead-framework* package was used for creating novel sub-problem selection strategies and 
analyzing them [@gpruvost_evocop2020], and for rewriting the component used to generate 
new candidate (offspring) solutions with a variant based on Walsh surrogates [@gpruvost_gecco2020].

| Software          | Can add a new algorithm | Can modify the components of the algorithms in a modular way | Can add components to algorithms |
|-------------------|-------------------------|--------------------------------------------------------------|----------------------------------|
| *moead-framework* | yes                     | yes                                                          | yes                              |
| MOEADr            | yes                     | yes                                                          | no                               |
| pymoo             | yes                     | no                                                           | no                               |
| pygmo             | yes                     | no                                                           | no                               |
| jMetal            | yes                     | no                                                           | no  


# Documentation

The documentation is available at the following URL: 
[moead-framework.github.io/framework/](https://moead-framework.github.io/framework/html/index.html).

A [complete example](https://moead-framework.github.io/framework/html/examples.html) and 
[all components](https://moead-framework.github.io/framework/html/api.html) are described in details.
[Two tutorials](https://moead-framework.github.io/framework/html/tuto.html) are made available for the user 
to experiment with their own multi-objective optimization problem and to implement their own MOEA/D variants.


# Acknowledgements

This work was supported by the French national research agency(ANR-16-CE23-0013-01) 
and the Research Grants Council of HongKong (RGC Project No. A-CityU101/16).


# References