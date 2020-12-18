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

The Multi-objective evolutionary algorithm based on decomposition (MOEA/D) is a general-purpose algorithm 
for approximating the Pareto set of multi-objective optimization problems [@moead]. It decomposes the original 
multi-objective problem into a number of 
single-objective optimization sub-problems and then uses an evolutionary process to optimize these 
sub-problems simultaneously and cooperatively. MOEA/D is a state-of-art algorithm in aggregation-based 
approaches for multi-objective optimization.

The goal of the *moead-framework* python package is to provide a modular framework for scientists and 
researchers interested in experimenting with MOEA/D and its numerous variants.


# Statement of Need

The MOEA/D algorithm is now considered as a framework. MOEA/D is the basis of many variants that improve or 
add new components to improve MOEA/D performance.
The first version of MOEA/D and its most famous variants [@moead_de; @moead_dra] are implemented in recent multi-objective 
optimization software such as pymoo [@pymoo], pygmo [@pygmo] and jMetal [@jmetal]. These software offer 
many state-of-art algorithms, visualization tools or parallelization abstraction but they do not enable to test 
and analyse in detail the behavior of components implemented in each algorithm.
The modular R package MOEADr [@Campelo_2020] focuses on MOEA/D and allows to define different variants for 
each component of MOEA/D. 

With the *moead-framework* package, we aim at bringing the modularity of the MOEADr package by 
using the flexibility of Python in order to allow the user to update the behavior of MOEA/D 
components in their research works, and to propose new variants without being limited by the software. 
The package is focused on a modular architecture for easily adding, updating or testing the components of 
MOEA/D and for customizing how components interact with each other.

For example, the *moead-framework* package was used for creating novel sub-problem selection strategies and 
analyzing them [@gpruvost_gecco2020], and for rewriting the component used to generate 
new candidate (offspring) solutions with a variant based on Walsh surrogates [@gpruvost_gecco2020].


# Documentation

The documentation is available at the following URL: 
[moead-framework.github.io/documentation/](https://moead-framework.github.io/documentation/html/index.html).

A [complete example](https://moead-framework.github.io/documentation/html/examples.html) and 
[all components](https://moead-framework.github.io/documentation/html/documentation.html) are described in details,
and [two tutorials](https://moead-framework.github.io/documentation/html/tuto.html) are made available for the user 
to experiment with his/her own multi-objective optimization problem and to implement his/her own MOEA/D variants.


# Acknowledgements

This work was supported by the French national research agency(ANR-16-CE23-0013-01) 
and the Research Grants Council of HongKong (RGC Project No. A-CityU101/16).


# References