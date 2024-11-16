from flask import Flask, render_template, request
from models import db, Product, Contact

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize db with the app
db.init_app(app)

# Ensure the tables are created before the first request
@app.before_first_request
def create_tables():
    with app.app_context():  # Ensure you are in the app context
        db.create_all()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        product_name = request.form.get('product_name')
        repository_name = request.form.get('repository_name')
        product = Product.query.filter(
            (Product.product_name == product_name) | 
            (Product.repository_name == repository_name)
        ).first()
        if not product:
            return render_template('search.html', error="Product not found")
        poc = Contact.query.get(product.poc_id)
        return render_template('search.html', result=poc)
    return render_template('search.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        product_name = request.form['product_name']
        repository_name = request.form['repository_name']
        new_contact = Contact(
            first_name=request.form['first_name'],
            last_name=request.form['last_name'],
            email=request.form['email'],
            chat_username=request.form['chat_username'],
            location=request.form['location'],
            title=request.form['title']
        )
        db.session.add(new_contact)
        db.session.commit()
        new_product = Product(
            product_name=product_name,
            repository_name=repository_name,
            poc_id=new_contact.id
        )
        db.session.add(new_product)
        db.session.commit()
        return render_template('add.html', success=True)
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)
