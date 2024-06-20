# Smart-Waste-Management

This project implements a Smart Waste System, which monitors and manages waste bins using IoT technology. The system aims to optimize waste collection routes and improve efficiency by providing real-time data on waste bin statuses.

## Table of Content

- Introduction

- Features

- Technologies Used

- Installation

- Configuration

- Usage

- Contributing

## Technologies Used

- Python: Backend logic and data processing.

- Flask: Web framework for building the application.

- MySQL: Lightweight database for storing bin and user data.

- HTML/CSS/JavaScript: Frontend development.

- Unit Testing: Using unittest module for testing components.

## Installation

- Clone the repository:

```
git clone https://github.com/GChukwudi/Smart-Waste-Management
cd https://github.com/GChukwudi/Smart-Waste-Management
```

- Set up a virtual environment

```
python -m venv venv
source venv/bin/activate
```

- Install dependencies

```
pip install -r requirements.txt
```

## Configuration


- Database Setup:

    - Initialize the database schema:

    ```
    flask db init
    flask db migrate
    flask db upgrade
    ```

## Usage

- Run the Flask application:

```
bash
Copy code
flask run
```

The application will be accessible at http://localhost:5000.