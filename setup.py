#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="R. Martin Parrondo",
    author_email='audreyr@example.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Project developed to work as a server for Python trading community. It is based on ZeroMQ sockets and uses JSON format to communicate messages. It is a python library for the ZeroMQ API within backtrader framework. It allows rapid trading algo development. For details of API behavior, please see the online API document.",
    entry_points={
        'console_scripts': [
            'mql5_zmq_backtrader=mql5_zmq_backtrader.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='mql5_zmq_backtrader',
    name='mql5_zmq_backtrader',
    packages=find_packages(include=['mql5_zmq_backtrader', 'mql5_zmq_backtrader.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/parrondo/mql5_zmq_backtrader',
    version='0.1.0',
    zip_safe=False,
)
