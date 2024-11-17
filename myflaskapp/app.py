from flask import Flask, request, jsonify
from databaseAPI import addEntry  # Import the addEntry function from databaseAPI.py
from sqlalchemy import create_engine, text
import json

app = Flask(__name__)

@app.route('/add-contact', methods=['POST'])
def add_contact():
    try:
        # Get the JSON data from the POST request
        data = request.get_json()

        # Prepare the data to be passed to the addEntry function
        entryFieldsList = [
            data['firstName'],
            data['lastName'],
            data['email'],
            data['username'],
            data['location'],
            data['position'],
            data['productName'],
            data['repositoryName']
        ]

        # Call the addEntry function to add the contact to the database
        addEntry(entryFieldsList)

        return jsonify({
            "status": "success",
            "message": "Contact added successfully!",
            "firstName": data['firstName'],
            "lastName": data['lastName']
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Failed to add contact. Error: {str(e)}"
        }), 400

if __name__ == "__main__":
    app.run(debug=True)
