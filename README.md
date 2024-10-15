# Flask Calculator API

This is a simple calculator API built with Flask.

## Usage

The API supports four operations: add, subtract, multiply, and divide.

Use the following format to make requests:

```
https://your-vercel-url.vercel.app/<operation>/<number1>/<number2>
```

Example:
```
https://your-vercel-url.vercel.app/add/5/3
```

This will return:
```json
{
  "status": 200,
  "result": 8
}
```

## Local Development

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run the app: `flask run`

## Running Tests

Run `pytest` in the project root directory.

## Deployment

This app is configured for deployment on Vercel. Follow the Vercel documentation to deploy your Flask app.