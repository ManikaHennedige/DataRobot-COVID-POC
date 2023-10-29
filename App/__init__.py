"""
The flask application package.
"""

from flask import Flask
import tensorflow as tf

import os, sys


app = Flask(__name__)


# route to the hrnet log files and weights
phase1_model = tf.keras.models.load_model("App/models/phase-1.h5")

basedir = os.path.abspath(os.path.dirname(__file__))



import App.routes