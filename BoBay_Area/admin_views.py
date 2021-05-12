"""
Routes and views for the admin on the application
"""

from datetime import datetime
from flask import render_template
from BoBay_Area import app

@app.route('/admin/dashboard')
def admin_dashboard():
    return render_template(
        'admin/dashboard.html',
        title='Admin Dashboard',
        year=datetime.now().year,
        message='Dashboard for the admin.'
    )
