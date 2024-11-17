from flask import Flask, request, jsonify , render_template
from databaseAPI import addContactEntry, addRepoEntry, addProductEntry, removeEntry , searchDB, __getCurrentID__
import json

app = Flask(__name__)

def validate_fields(data, required_fields):
    """Validate required fields in JSON payload."""
    missing = [field for field in required_fields if field not in data]
    if missing:
        raise ValueError(f"Missing required fields: {', '.join(missing)}")

@app.route('/add-contact', methods=['POST'])
def add_contact():
    try:
        #Please input your userID
        #if(getPositionByID(data['id'] != 'Admin')):
        #    return jsonify({
        #    "status": "error",
        #    "message": "You do not have the authority to alter the database."
        #}), 400

        data = request.get_json()
        required_fields = ['firstName', 'lastName', 'email', 'username', 'location', 'position']
        validate_fields(data, required_fields)

        entryFieldsList = [
            data['firstName'] + ' ' + data['lastName'],
            data['email'],
            data['username'],
            data['location'],
            data['position']
        ]

        #Add the contact to the database with the specificed data
        addContactEntry(entryFieldsList)
        if(data['repositoryName'] != None):
            add_Repo(__getCurrentID__(), data['repositoryName'])
        if(data['productName'] != None):
            add_Product(__getCurrentID__(), data['productName'])

        return jsonify({
            "status": "success",
            "message": "Contact added successfully!",
            "firstName": data['firstName'],
            "lastName": data['lastName']
        })

    except ValueError as ve:
        return jsonify({
            "status": "error",
            "message": f"Validation error: {str(ve)}"
        }), 400

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Failed to add contact. Error: {str(e)}"
        }), 400

@app.route('/add-repo', methods=['POST'])
def add_Repo():
    try:
        data = request.get_json()
        required_fields = ['user_id', 'repo_name']
        validate_fields(data, required_fields)

        entryfieldsList = [
            data['user_id'],
            data['repo_name']
        ]

        #Adds the corresponding repo entry
        addRepoEntry(entryfieldsList)

        return jsonify({
            "status": "success",
            "message": "Repository link added successfully!",
            "Repository name": data['repo_name']
        })

    except ValueError as ve:
        return jsonify({
            "status": "error",
            "message": f"Validation error: {str(ve)}"
        }), 400

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Failed to add repository. Error: {str(e)}"
        }), 400


@app.route('/add-product', methods=['POST'])
def add_Product():
    try:
        data = request.get_json()
        required_fields = ['user_id', 'product_name']
        validate_fields(data, required_fields)

        entryfieldsList = [
            data['user_id'],
            data['product_name']
        ]

        #Adds the product using the specified information
        addProductEntry(entryfieldsList)

        return jsonify({
            "status": "success",
            "message": "Product link added successfully!",
            "Product name": data['product_name']
        })

    except ValueError as ve:
        return jsonify({
            "status": "error",
            "message": f"Validation error: {str(ve)}"
        }), 400

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Failed to add product. Error: {str(e)}"
        }), 400


def validate_id(data):
    """Validate the presence of 'id' in the request payload."""
    if 'id' not in data:
        raise ValueError("Missing required field: 'id'")

@app.route('/remove-entry', methods=['DELETE'])
def remove_entry():
    try:
        data = request.get_json()
        validate_id(data)

        # Call the removeEntry function with the provided ID
        removeEntry(data['id'])

        return jsonify({
            "status": "success",
            "message": f"Contact with ID {data['id']} has been successfully removed."
        })

    except ValueError as ve:
        return jsonify({
            "status": "error",
            "message": f"Validation error: {str(ve)}"
        }), 400

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Failed to remove entry. Error: {str(e)}"
        }), 500

@app.route('/search', methods=['GET'])
def search():
    try:
        # Get the query parameter from the request
        query = request.args.get('query')
        if not query:
            raise ValueError("Missing query parameter")

        # Call the searchDB function to get user data
        userArray = searchDB(query)

        # Render the HTML template and pass the userArray to it
        return render_template('search_results.html', users=userArray)

    except ValueError as ve:
        return jsonify({
            "status": "error",
            "message": f"Validation error: {str(ve)}"
        }), 400

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Failed to fetch search results. Error: {str(e)}"
        }), 500

if __name__ == "__main__":
    app.run(debug=True)