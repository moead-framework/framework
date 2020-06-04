# MOEA/D Framework

![Python application](https://github.com/geoffreyp/moead/workflows/Python%20application/badge.svg?branch=master)


# Install

Create a virtual environment with [conda](https://docs.conda.io/en/latest/miniconda.html) or [virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)

To install : 

    pip install moead-framework
    

# For developers 

## build : 

The package is build with a github action. If you want to create manually a new package : 

    python3 setup.py sdist bdist_wheel
 
    python3 -m twine upload dist/*
