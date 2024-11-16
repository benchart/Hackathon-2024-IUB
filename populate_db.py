from models import db, Product, Contact
from app import app

with app.app_context():
    db.create_all()
    contact = Contact(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        chat_username="johndoe",
        location="Lucerne, CH",
        title="Security Engineer"
    )
    db.session.add(contact)
    db.session.commit()

    product = Product(
        product_name="SecurityScan",
        repository_name="sec-scan-repo",
        poc_id=contact.id
    )
    db.session.add(product)
    db.session.commit()