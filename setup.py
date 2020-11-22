from setuptools import setup, find_packages

setup(
   name='Django Admin Edit Mode',
   version='0.1.0',
   author='Mikhail Koipish',
   author_email='mkoypish@gmail.com',
   packages=find_packages(),
   scripts=[],
   url='http://pypi.python.org/pypi/PackageName/',
   license='LICENSE.txt',
   description='An awesome package that does something',
   long_description=open('README.md').read(),
   install_requires=[
       "Django >= 1.1.1",
       "django-spurl==0.6.7"
   ],
)