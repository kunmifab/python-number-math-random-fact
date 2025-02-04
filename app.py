from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return jsonify({'message': 'Hello, World!'})

@app.route('/api/classify-number')
def classify_number():
    number = request.args.get('number', type=int)
    if number is None:
        return jsonify({'number': 'alphabet', "error": True}), 400

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    # Determine if the number is perfect
    def is_perfect(n):
        return n == sum(i for i in range(1, n) if n % i == 0)

    # Determine if the number is an Armstrong number
    def is_armstrong(n):
        digits = [int(d) for d in str(n)]
        return n == sum(d**len(digits) for d in digits)

    # Calculate the digit sum
    digit_sum = sum(int(d) for d in str(number))

    # Fetch a fun fact from the Numbers API
    fun_fact_response = requests.get(f"http://numbersapi.com/{number}/math")
    fun_fact = fun_fact_response.text if fun_fact_response.status_code == 200 else "No fun fact available."

    # Determine properties
    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    if number % 2 != 0:
        properties.append("odd")
    else:
        properties.append("even")

    response = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact
    }

    return jsonify(response), 200
if __name__ == '__main__':
    app.run(debug=True)