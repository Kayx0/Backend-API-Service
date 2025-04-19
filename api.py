from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/packages', methods=['GET'])
def get_packages():
    packages = [
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

    return jsonify(packages)

if __name__ == '__main__':
    app.run(debug=True)