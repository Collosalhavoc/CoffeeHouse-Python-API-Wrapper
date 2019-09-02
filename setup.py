from distutils.core import setup

setup(
    name='coffeehouse',
    version='1.0.2',
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
