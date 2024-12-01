from flask import Flask

app = Flask(__name__)  # _name_ takes the name of the parent folder


@app.route(
    "/"
)  # app is a decorator used to store recursive data - GET Method by default
def hello_world():
    """
        Returns 'Hello, World!' in response to a GET request to the root URL.
    gi
        This function serves as the entry point for the Flask application and
        demonstrates the basic routing capabilities of the framework.
    """
    return "Hello, World!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8989)

# To run the app, type "python app.py" in the terminal
