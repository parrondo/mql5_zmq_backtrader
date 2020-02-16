"""
Top-level package for mql5_zmq_backtrader.
Project developed to work as a server for Python trading community. It is based on ZeroMQ sockets and uses JSON format to communicate messages. It is a python library for the ZeroMQ API within backtrader framework. It allows rapid trading algo development. For details of API behavior, please see the online API document.
"""

__author__ = """R. Martin Parrondo"""
__version__ = '0.1.0'

from .mt5store import *
from .mt5broker import *
from .mt5data import *
