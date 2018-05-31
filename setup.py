from setuptools import setup, find_packages

setup(
    # Application name:
    name="dibyojyoti-master-thesis-CASXmi-python",

    # Version number (initial):
    version="0.1.1",

    # Application author details:
    author="dibyojyoti sanyal",
    author_email="dibyojyoticemk@gmail.com",

    # Packages
    packages=find_packages(),

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="https://git.ukp.informatik.tu-darmstadt.de/dibyojyoti/UIMAAS_Thesis_Dibyo/tree/master/python",

    #
    # license="LICENSE.txt",
    description="CAS API python.",
    test_suite="tests",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[
        "lxml",
    ]
)
