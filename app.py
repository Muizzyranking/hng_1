import requests
from flask import Flask, jsonify, request
from flask_caching import Cache
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
cache = Cache(app, config={"CACHE_TYPE": "simple"})


@cache.memoize(3600)
def get_fun_fact(number):
    try:
        response = requests.get(
            f"http://numbersapi.com/{number}/math?json", timeout=3
        )
        return response.json().get("text", "No fun fact available")
    except requests.exceptions.RequestException:
        return "Could not fetch fun fact."


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_even(n):
    return n % 2 == 0


def is_odd(n):
    return n % 2 != 0


def isArmstrong(num):
    k = len(str(num))
    sum = 0
    n = num
    while n > 0:
        ld = n % 10
        sum += ld**k
        n = n // 10
    return sum == num


def properties(n):
    properties = []
    if isArmstrong(n):
        properties.append("armstrong")
    properties.append("even" if is_even(n) else "odd")
    return properties


def digit_sum(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum


def is_perfect(n):
    res = 0
    for i in range(1, n):
        if n % i == 0:
            res = res + i
    if res == n:
        return True
    else:
        return False


@app.route("/")
def hello():
    return jsonify({"message": "Hello, World!"})


@app.route("/api/classify_number", methods=["GET"])
def classify_number():
    param = request.args.get("number")
    if not param:
        return (
            jsonify(
                {
                    "error": True,
                    "number": "alphabet",
                    "message": "Missing number parameter",
                }
            ),
            400,
        )
    try:
        number = int(param)
    except ValueError:
        return (
            jsonify(
                {
                    "error": True,
                    "number": "alphabet",
                }
            ),
            400,
        )
    return (
        jsonify(
            {
                "number": number,
                "is_prime": is_prime(number),
                "is_perfect": is_perfect(number),
                "properties": properties(number),
                "digit_sum": digit_sum(number),
                "fun_fact": get_fun_fact(number),
            }
        ),
        200,
    )


if __name__ == "__main__":
    print(app.url_map)
    app.run(host="0.0.0.0", port=5000, debug=True)
