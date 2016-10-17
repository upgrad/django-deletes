import os
from setuptools import find_packages, setup

#with open(os.path.join(os.path.dirname(__file__), 'djangodeletes/README.rst')) as readme:
#    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='djangodeletes',
    version='0.6',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',  # example license
    description='A fully functional soft deletes (logical deletes) for django.',
    long_description='A fully functional soft deletes for django',
    url='https://github.com/upgrad/django-deletes',
    author='Ankit Mittal',
    author_email='ankit@upgrad.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.9',  
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
