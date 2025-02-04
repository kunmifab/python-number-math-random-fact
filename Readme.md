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
- **URL**: `/`

### Request/Response Format
The API returns a JSON response with the following fields:
```json
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/yourusername/your-repo"
}
```

## Example Usage

To use the API, you can make a GET request to the root URL. Here's an example using `curl`:

```bash
curl http://127.0.0.1:5000/
```

## Backlink

For more information on hiring Python developers, visit [HNG Tech](https://hng.tech/hire/python-developers).





