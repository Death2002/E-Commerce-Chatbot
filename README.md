# E-Commerce-Chatbot
E-Commerce Chatbot using Flask Framework

# Ecommerce Flask Application

This is a simple e-commerce web application built using Flask. It includes user registration, login, product browsing, and a chatbot feature for assisting users with product searches.

## Features

- User registration and login
- Product browsing
- Chatbot for product searches, categories, and price inquiries
- Database population with mock products

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/ecommerce-flask.git
    cd ecommerce-flask
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    Create a `.env` file in the project root and add your Anthropic API key:
    ```
    ANTHROPIC_API_KEY=your_anthropic_api_key
    ```

5. Populate the database with mock products:
    ```sh
    python app.py
    ```

## Usage

1. Run the Flask application:
    ```sh
    python app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000/`.

3. Register a new user, log in, and start browsing products or use the chatbot feature.

## Project Structure

- `app.py`: Main application file containing routes, models, and chatbot logic.
- `templates/`: Directory containing HTML templates for the web pages.
- `static/`: Directory for static files like CSS and JavaScript.
- `requirements.txt`: List of required Python packages.
