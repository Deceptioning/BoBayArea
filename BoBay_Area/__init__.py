"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

from BoBay_Area import views
from BoBay_Area import admin_views

"""import BoBay_Area.views"""

if __name__ == "__main__":
    app.run()

