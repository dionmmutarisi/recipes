"""
app.py

Flask server for the Chikafu app. Handles recipe idea display
"""

from flask import Flask, request, jsonify, Response, render_template
from chikafu.chikafu import get_recipe
from dotenv import load_dotenv
import requests
import os


load_dotenv()

# Create Flask object 
app = Flask(__name__,     
            static_folder  ="../frontend/static",      
            static_url_path="/static"                        
)


app.chikafu = get_recipe()

@app.route('/')
def index() -> str:
    """
    Render the index page.
    """

    return render_template('index.html')


@app.route("/health", methods=["GET"])
def health_check() -> Tuple[str, int]:
    """
    This endpoint checks if the backend server is running or not.
    Returns:
        Tuple[str, int]: A tuple containing a mesage indicating the server status and HTTP status code.
    """

    return 'OK', 200

@app.route("chikafu/recipes", methods=['GET'])

def get_generated_recipe() -> Response:
    """
    Generates a recipe using Gemini API.

    Returns:
        Response: JSON containing results.

        
    """

    try:
        idea = get_recipe()
        return jsonify(idea), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    