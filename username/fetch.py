from flask import Flask
import getpass

app = Flask(__name__)

@app.route("/")
def home():
    username = getpass.getuser()  # Fetch the OS-level logged-in user

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Welcome Page</title>
        <style>
            body {{
                background-color: #f0f8ff;
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .container {{
                text-align: center;
                padding: 40px;
                background-color: #ffffff;
                box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
                border-radius: 15px;
            }}
            h2 {{
                color: #333333;
                font-size: 2em;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Hello, {username}!</h2>
        </div>
    </body>
    </html>
    """
    return html_content

if __name__ == "__main__":
    app.run(debug=True)
