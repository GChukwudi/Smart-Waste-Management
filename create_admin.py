from app import create_app, db, bcrypt
from app.models import User

# Create the Flask application object
app = create_app()

# Use the application context
with app.app_context():
    # Define the admin user's credentials
    username = 'admin'
    email = 'g.chukwudi@alustudent.com'
    password = 'verify1234'

    # Check if the admin user already exists
    existing_admin = User.query.filter_by(email=email).first()

    if not existing_admin:
        # Hash the password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Create the admin user
        admin_user = User(username=username, email=email, password=hashed_password, role='admin')

        # Add the admin user to the session and commit to the database
        db.session.add(admin_user)
        db.session.commit()

        print('Admin user created successfully.')
    else:
        print('Admin user already exists.')
