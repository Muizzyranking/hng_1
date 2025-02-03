# Number Classification API

This is a simple Flask-based API that classifies numbers based on mathematical properties and provides fun facts about the number.

### Features

- Accepts a number via a query parameter.
- Returns JSON with the number's classification, such as whether it's prime, perfect, or Armstrong, along with the sum of its digits.
- Provides a fun fact about the number fetched from the Numbers API.

## API Endpoint

### `GET /api/classify-number?number=<number>`

This endpoint takes a `number` as a query parameter and returns a JSON response with the following fields:

#### Success Response (200 OK)

```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

#### Error Response (400 Bad Request)

If the input is not a valid integer:

```json

{
    "number": "alphabet",
    "error": true
}
```

### Requirements

- Python 3.7+
- Flask
- Flask-CORS
- Requests

#### Setup

    Clone the repository:

```bash
git clone https://github.com/muizzyranking/number-classification-api.git
cd number-classification-api
```

#### Install the required dependencies

```bash
pip install -r requirements.txt
```

#### Running the API

To start the API locally, run the following command:

```bash
python app.py
```

The API will be available at <http://localhost:5000>.
Testing the API

To test the API, you can use any HTTP client like curl, Postman, or simply navigate to:

<http://localhost:5000/api/classify-number?number=371>

You can replace 371 with any other number you'd like to test.
Example using curl:

curl <http://localhost:5000/api/classify-number?number=371>
