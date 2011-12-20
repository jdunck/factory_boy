#!/usr/bin/python

from distutils.core import setup

# Remember to change in factory/__init__.py as well!
VERSION = '1.0.3'

setup(
    name='factory_boy_jdunck',
    version=VERSION,
    description="A test fixtures replacement based on thoughtbot's factory_girl for Ruby (originally by mark@deliciouslynerdy.com)",
    author='Jeremy Dunck',
    author_email='jdunck@gmail.com',
    url='http://github.com/jdunck/factory_boy',
    keywords=['factory_boy', 'factory', 'fixtures'],
    packages=['factory'],
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
