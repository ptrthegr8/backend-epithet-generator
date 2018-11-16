"""
This module handles logic for loading environment variables, instantiating
Flask, and returning an app instance of Flask for use throughout the package.
"""


def configure_app():
    """
    This function loads environment variables, instantiates Flask,
    and returns an instance of Flask.
    """
    import os

    import dotenv
    from flask import Flask

    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
    dotenv.load_dotenv(os.path.join(PROJECT_ROOT, '.env'))
    app = Flask(__name__)
    return app


app = configure_app()
