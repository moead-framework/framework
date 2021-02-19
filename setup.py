import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="moead-framework",
    version="0.5.9.1",
    author="Geoffrey Pruvost",
    author_email="geoffrey@pruvost.xyz",
    description="MOEA/D Framework in Python 3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/moead-framework/framework",
    packages=setuptools.find_packages(),
    install_requires=['numpy'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)