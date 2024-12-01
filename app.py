from flask import Flask, render_template

app = Flask(__name__)  # _name_ takes the name of the parent folder


@app.route(
    "/"
)  # app is a decorator used to store recursive data - GET Method by default
def home():
    """
        Returns 'Hello, World!' in response to a GET request to the root URL.
    gi
        This function serves as the entry point for the Flask application and
        demonstrates the basic routing capabilities of the framework.
    """
    return render_template("home.html", my_name="santa")


@app.route("/about")
def about():
    """
    Returns the content of the 'about.html' template in response to a GET request to the '/about' URL.

    This function demonstrates how to render a template using Flask's `render_template` function.
    The 'about.html' template is located in the 'templates' directory of the application.
    """
    return render_template("about.html", about_text="lorem ipsum")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8989)

# To run the app, type "python app.py" in the terminal
