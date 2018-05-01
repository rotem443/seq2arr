from setuptools import setup, find_packages

setup(
    name="arr2seq",
    version="0.1.0",

    description=("Convert array 2 sequence usefull for preproccessing datasets",),

    author="Rotem bar",
    author_email="rotem4432@gmail.com",

    packages=find_packages('src'),
    package_dir={'': 'src'},

    install_requires=[
        'numpy',
    ],
)
