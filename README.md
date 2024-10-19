# Flask Calculator API

This project is a simple Flask-based Calculator API that performs basic arithmetic operations. It's currently deployed on Vercel at: [https://lab-2-git-homework-o-git-main-amel-feddags-projects.vercel.app/](https://lab-2-git-homework-o-git-main-amel-feddags-projects.vercel.app/)

## Repository Structure

```
project/
├── app/
│   ├── __init__.py    # Flask app initialization
│   ├── calculator.py  # Arithmetic operation functions
│   └── routes.py      # API route definitions
├── tests/
│   └── test_calculator.py  # Unit tests for calculator functions
├── .gitignore         # Specifies intentionally untracked files to ignore
├── main.py            # Entry point for the Flask application
├── requirements.txt   # List of Python package dependencies
└── vercel.json        # Configuration file for Vercel deployment
```

## Setup and Installation

### Cloning the Repository

1. Open a terminal or command prompt.
2. Navigate to your desired parent directory:
   ```
   # Windows
   cd C:\Users\YourUsername\Desktop\SoftwareEngineering\Labs\Lab_2_Git

   # Linux/macOS
   cd ~/Desktop/SoftwareEngineering/Labs/Lab_2_Git
   ```
3. Clone the repository:
   ```
   git clone https://github.com/your-username/your-repo-name.git Homework
   ```
4. Navigate into the project directory:
   ```
   cd Homework
   ```

### Setting Up the Environment

1. Create a virtual environment:
   ```
   # Windows
   python -m venv venv

   # Linux/macOS
   python3 -m venv venv
   ```

2. Activate the virtual environment:
   ```
   # Windows
   venv\Scripts\activate

   # Linux/macOS
   source venv/bin/activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running Locally

1. Ensure your virtual environment is activated.
2. Run the Flask application:
   ```
   python main.py
   ```
3. The server should start running on `http://127.0.0.1:5000/`
4. Test the API using a web browser or a tool like curl or Postman:
   - Example URL: `http://127.0.0.1:5000/add/5/3`
   - Available operations: add, subtract, multiply, divide

## Deploying to Your Own Vercel Account

To deploy this project to your own Vercel account, follow these steps:

Alternatively, you can set up automatic deployments:

1. Go to your Vercel dashboard ([https://vercel.com/dashboard](https://vercel.com/dashboard))
2. Click "Import Project"
3. Choose "From Git Repository"
4. Select your forked GitHub repository
5. Configure your project settings (Vercel should auto-detect that it's a Python project)
6. Click "Deploy"

Now, whenever you push changes to your GitHub repository, Vercel will automatically deploy your updates.

Or you could Also follow these steps from your command line but the automatic deployment is better:

1. Fork this repository to your GitHub account.

2. Sign up for a Vercel account at [https://vercel.com](https://vercel.com) if you haven't already.

3. Install the Vercel CLI:
   ```
   npm install -g vercel
   ```

4. Log in to Vercel through the CLI:
   ```
   vercel login
   ```

5. Clone your forked repository:
   ```
   git clone https://github.com/your-username/your-forked-repo.git
   cd your-forked-repo
   ```

6. Deploy to Vercel:
   ```
   vercel
   ```
   Follow the prompts. When asked about the project settings, you can usually accept the defaults.

7. Once deployed, Vercel will provide you with a URL where your app is live.



## Usage

The API supports four operations: add, subtract, multiply, and divide.

URL Format: `https://your-vercel-url.com/<operation>/<number1>/<number2>`

Example: 
- Addition: `https://your-vercel-url.com/add/5/3`
- Subtraction: `https://your-vercel-url.com/subtract/10/4`
- Multiplication: `https://your-vercel-url.com/multiply/6/7`
- Division: `https://your-vercel-url.com/divide/15/3`

The API returns a JSON response with the following format:
```json
{
  "status": 200,
  "result": 8
}
```

## Testing

To run the unit tests:

1. Ensure your virtual environment is activated.
2. Run the tests using pytest:
   ```
   pytest
   ```


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
