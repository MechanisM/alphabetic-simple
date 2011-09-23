### -*- coding: utf-8 -*- ####################################################
"""
Configuration file used by setuptools. It creates 'egg', install all dependencies.
"""

import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

#Dependencies - python eggs
install_requires = [
        'setuptools',
        'Django',
        'django-native-tags',
]

#Execute function to handle setuptools functionality
setup(name="alphabetic-simple",
    version="0.2",
    description="Alphabetic template tag to filter django queryset",
    long_description=read('README'),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    author='Arpaso',
    author_email='arvid@arpaso.com',
    url='http://github.com/Arpaso/alphabetic-simple.git',
    classifiers=(
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
    ),
)
