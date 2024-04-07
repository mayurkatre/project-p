URL Shortener README
Introduction
This repository contains a Python script for a simple URL shortener web application. The application uses Flask as the web framework, SQLite for database storage, and inline HTML/CSS for the frontend.

Features
Shortens long URLs into unique alphanumeric codes.
Stores original URLs and their corresponding short codes in a SQLite database.
Provides a simple interface for users to input URLs and obtain shortened versions.
Redirects users to the original URLs when they access the shortened ones.
Installation
Ensure you have Python installed on your system.
Install Flask using pip:
Copy code
pip install Flask
Clone this repository:
bash
Copy code
git clone https://github.com/mayurkatre/url-shortener.git
Navigate to the project directory:
bash
Copy code
cd url-shortener
Usage
Run the Python script:
Copy code
python app.py
Open a web browser and go to http://localhost:5000/.
Enter a URL you want to shorten and click the "Shorten" button.
Copy the shortened URL provided.
Paste the shortened URL into the browser address bar to be redirected to the original URL.
Code Explanation
Imports and Initialization: The code imports necessary modules and initializes the Flask application.
Helper Functions: Functions to generate short codes, create the database, shorten URLs, and retrieve original URLs from the database.
Routing: Defines URL routes for different functionalities of the application.
HTML and CSS: HTML and CSS code included as multi-line strings directly within the Python code.
Main Execution: Calls the create_database() function and runs the Flask application.
Contributing
Contributions are welcome! Feel free to open issues or pull requests for any improvements or bug fixes.
