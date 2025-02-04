# HNG API

This is a simple API that returns my registered email, the current datetime in ISO 8601 format, and the GitHub URL of the project. It is designed to demonstrate basic API functionality using Python and Flask.

## Table of Contents
- [Setup Instructions](#setup-instructions)
- [API Documentation](#api-documentation)
- [Example Usage](#example-usage)
- [Backlink](#backlink)

---

## Setup Instructions

Follow these steps to set up and run the project locally.

### Prerequisites
- Python 3.x installed on your system.
- Git installed (optional, for version control).

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   ```

2. **Navigate to the Project Folder**:
   ```bash
   cd your-repo
   ```

3. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   ```

4. **Activate the Virtual Environment**:
   ```bash
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

5. **Install Dependencies**:
   Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

6. **Run the API**:
   Start the Flask development server:
   ```bash
   python app.py
   ```

7. **Access the API**:
   Access the API at `http://127.0.0.1:5000/`

## API Documentation

### Endpoint
- **Method**: `GET`
- **URL**: `/api/classify-number`

### Request Parameters
- **number**: The number to classify (passed as a query parameter).

### Request/Response Format

#### Successful Response (200 OK)
The API returns a JSON response with the following fields:
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
If the input is invalid, the API returns a JSON response with the following fields:
```json
{
    "number": "alphabet",
    "error": true
}
```

## Example Usage

To use the API, you can make a GET request to the `/api/classify-number` endpoint with a query parameter. Here's an example using `curl`:

```bash
curl "http://127.0.0.1:5000/api/classify-number?number=371"
```

## Backlink

For more information on hiring Python developers, visit [HNG Tech](https://hng.tech/hire/python-developers).





