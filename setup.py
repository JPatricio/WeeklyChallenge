from setuptools import setup

# reading long description from file
with open('DESCRIPTION.txt') as file:
    long_description = file.read()

# specify requirements of your package here
REQUIREMENTS = []

# some more details
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Personal',
    'Topic :: CLI',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
]

# calling the setup function
setup(name='jls',
      version='0.1.0',
      description='My custom implementation of the ls command',
      long_description=long_description,
      url='https://github.com/JPatricio/jls',
      author='Joao Patricio',
      author_email='canas.joao@gmail.com',
      license='MIT',
      packages=['jls'],
      classifiers=CLASSIFIERS,
      install_requires=REQUIREMENTS,
      keywords='ls cli macos'
      )
