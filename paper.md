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
    affiliation: "1, 2" 
  - name: Bilel Derbel
    affiliation: "1, 2" 
  - name: Arnaud Liefooghe
    affiliation: "1, 2" 
affiliations:
  - name: Univ. Lille, CNRS, Centrale Lille, UMR 9189 CRIStAL, F-59000 Lille, France
    index: 1
  - name: Inria Lille - Nord Europe
    index: 2

date: 1 December 2020
bibliography: paper.bib

# Optional fields if submitting to a AAS journal too, see this blog post:
# https://blog.joss.theoj.org/2018/12/a-new-collaboration-with-aas-publishing
# aas-doi: 10.3847/xxxxx <- update this with the DOI from AAS once you know it.
# aas-journal: Astrophysical Journal <- The name of the AAS journal.
---

# Summary

The Multi-objective evolutionary algorithm based on decomposition (MOEA/D) is a general-purpose 
algorithm framework [@moead]. It decomposes a multi-objective optimization problem into a number of 
single-objective optimization sub-problems and then uses an evolutionary process to optimize these 
sub-problems simultaneously and cooperatively. MOEA/D is a state-of-art algorithm in aggregation-based 
approaches for multi-objective optimization.

The goal of the *moead-framework* python package is to provide a modular framework for researchers who 
are working on variants of MOEA/D.


# Motivation

The first version of MOEA/D and its most famous variants [@moead_de; @moead_dra] are implemented in recent multi-objective 
optimization software such as pymoo [@pymoo], pygmo [@pygmo] and jMetal [@jmetal]. These software bring a lot of algorithms and problems but 
don't allow us to test and analyse in detail each algorithms. 
The modular R package MOEADr [@Campelo_2020] allows to use each components of MOEA/D with some variants but is not enough flexible 
to add, remove or update the behavior of these components. 

With this python package, we want to bring the modularity of the MOEADr package by using the flexibility of Python to 
allow users to update the behavior of MOEA/D components in their research works to propose new variants without 
be limited by the software. For example, the paper "On the Combined Impact of Population Size 
and Sub-problem Selection in MOEA/D" [@gpruvost_evocop2020] uses this package to add a new component 
in MOEA/D (the sub-problem selection strategy) and the paper 
"Surrogate-assisted Multi-objective Combinatorial Optimization based on Decomposition and Walsh Basis" [@gpruvost_gecco2020] uses 
the package to rewrite the offspring_generator component to implement a new framework to walsh surrogates
with multi-objective optimization and decomposition technics.


# Documentation

The documentation is available online : [https://moead-framework.github.io/documentation/](https://moead-framework.github.io/documentation/html/index.html). 

A [full example](https://moead-framework.github.io/documentation/html/examples.html) 
and [all components](https://moead-framework.github.io/documentation/html/documentation.html) are described.
[Two tutorials](https://moead-framework.github.io/documentation/html/tuto.html) are available 
to test your own problems and implement your own variants of MOEA/D.


# Acknowledgements

This work was supported by the French national research agency(ANR-16-CE23-0013-01) 
and the Research Grants Council of HongKong (RGC Project No. A-CityU101/16).


# References