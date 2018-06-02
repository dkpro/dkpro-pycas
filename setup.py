from setuptools import setup, find_packages

setup(
    # Application name:
    name="DKPro PyCAS",

    # Version number (initial):
    version="0.1.1a",

    # Application author details:
    author="DKPro PyCAS Team",
    author_email="dkpro-core-user@googlegroups.com",

    # Packages
    packages=find_packages(),

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="https://github.com/dkpro/dkpro-pycas",

    #
    license='Apache License 2.0',
    description="UIMA CAS XMI API for Python.",
    test_suite="tests",

    # long_description=open("README.txt").read(),

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries'
    ],

    # Dependent packages (distributions)
    install_requires=[
        "lxml",
    ]
)
