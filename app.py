#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: demo.py
Author: harri
Email:
Description: Main entrance  .
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to My Watchlist!'