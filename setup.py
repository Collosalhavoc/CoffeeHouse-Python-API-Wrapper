from distutils.core import setup

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name='coffeehouse',
    version='1.0.5',
    description='Official CoffeeHouse API Wrapper for Python',
    long_description=long_description,
    packages=['coffeehouse'],
    package_dir={
        'coffeehouse': 'coffeehouse'
    },
    author='Zi Xing',
    author_email='netkas@intellivoid.info',
    url='https://coffeehouse.intellivoid.info/',
    install_requires=[
        'requests>=2.3.0'
    ]
)
