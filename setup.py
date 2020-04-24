import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="moead-framework",
    version="0.0.1",
    author="Geoffrey Pruvost",
    author_email="geoffrey@pruvost.xyz",
    description="MOEA/D Framework in Python 3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/geoffreyp/moead",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)