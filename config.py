import os
from datetime import timedelta

class Config:
    """Application configuration class"""
    # Secret key for session management and CSRF protection
    SECRET_KEY = os.environ.get('SECRET_KEY') or '24f2003480'
    
    # Database configuration - SQLite for local development, dynamically corrected for Postgres in production
    _db_url = os.environ.get('DATABASE_URL')
    if _db_url and _db_url.startswith("postgres://"):
        _db_url = _db_url.replace("postgres://", "postgresql://", 1)
    SQLALCHEMY_DATABASE_URI = _db_url or 'sqlite:///parking_app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Session configuration
    PERMANENT_SESSION_LIFETIME = timedelta(hours=2)
    
    # Admin default credentials (change in production)
    ADMIN_USERNAME = 'aakash'
    ADMIN_PASSWORD = '24f2003480'