from flask import Flask, request, render_template_string

app = Flask(__name__)

# Route to display the search form
@app.route('/')
def index():
    return render_template_string(open('home.html').read())  # Serve the HTML form

# Route to handle the search logic
@app.route('/search', methods=['GET'])
def search():
    # Get the 'query' parameter from the URL (search input)
    query = request.args.get('query')
   
    if query:
        # Here, you can process the 'query' variable as needed
        return f'You searched for: {query}'  # Return the search query back to the user
    else:
        return 'No search query provided.'

if __name__ == '__main__':
    app.run(debug=True)