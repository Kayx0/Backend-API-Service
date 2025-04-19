#Backend-API-Service

from flask import Flask, jsonify **Import the Flask class and jsonify function from the flask package**

app = Flask(__name__) **This line starts our Flask app**

@app.route('/api/packages', methods=['GET'])   **This route will run when someone visits '/api/packages'**
def get_packages():  **When someone accesses that link, the get_packages() function runs**
    packages = [   **A simple list of travel packages like destination, price, and duration**
    
        {
            "destination": "Zamboanga del Sur",
            "price": 500,
            "duration": "3 days"
        },
        {
            "destination": "Japan",
            "price": 20000,
            "duration": "1 week"
        },
    ]

    return jsonify(packages)   **This sends the list back to the user in JSON format, which can be easily read by websites or mobile apps**

if __name__ == '__main__':    **This makes sure the app only runs when we open this file directly**
    app.run(debug=True)   **debug=True allows us to see detailed error messages while developing**


    ** How the integration was done **
    -> I used Flask to build a simple web API.
    -> The API is connected to a specific URL: /api/packages. An example, run the code in terminal of the VSCODE then type 'python api.py (python filename)'. Then, it will display the route.
    -> When visiting the link, Flask runs the function that returns a list of travel packages.
    -> We will then return the data using jsonify, which makes it easy for other programs or users to access the information.

    ** Choice of language and why **
    -> Language used: Python
      Why?
    -> Python is simple and beginner-friendly.
    -> Flask is a lightweight framework that makes it easy to build web apps and APIs with just a few lines of code.
    ->Perfect for small projects, practice, or when you're learning how web backends work.
