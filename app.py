from flask import Flask, abort, request
from utils import find_modify_user

app = Flask(__name__)  # _name_ takes the name of the parent folder

users = [
    {
        "id": 1,
        "name": "Santa",
        "age": 25,
        "occupation": "Software Engineer",
        "hobbies": ["Reading", "Coding", "Gaming"],
    },
    {
        "id": 2,
        "name": "David",
        "age": 30,
        "occupation": "Data Scientist",
        "hobbies": ["Hiking", "Cooking", "Photography"],
    },
    {
        "id": 3,
        "name": "Esteban",
        "age": 22,
        "occupation": "Graphic Designer",
        "hobbies": ["Drawing", "Painting", "Traveling"],
    },
    {
        "id": 4,
        "name": "Jorge",
        "age": 35,
        "occupation": "Teacher",
        "hobbies": ["Reading", "Teaching", "Traveling"],
    },
    {
        "id": 5,
        "name": "Luis",
        "age": 28,
        "occupation": "Marketing Specialist",
        "hobbies": ["Social Media", "Content Creation", "Networking"],
    },
]


@app.errorhandler(404)
def not_found(error):
    """
    Handle the 404 error by returning a JSON response with an error message.

    Parameters:
    error (int): The HTTP status code for the error (in this case, 404).

    Returns:
    str: A JSON string containing an error message.
    """
    return {"error": error.description}, 404


@app.put("/users/<int:user_id>")
def update_user(user_id):
    """
    Update a user's details.

    Parameters:
        user_id (int): The ID of the user to be updated.

    Returns:
        None

    Raises:
        ValueError: If the user ID is not found.
    """
    global users  # Declare users as a global variable, must declare a global variable everytime I want to change it
    user_new_props = request.get_json()
    user = find_modify_user(user_id, users, user_new_props)
    if user is None:
        abort(404, f"User with ID {user_id} not found.")
    return user


@app.route("/users")
def get_users():
    """
    Returns a list of all users.

    :return: A dictionary containing the list of users.
    :rtype: dict
    """
    return {"users": users}


@app.route("/users/<int:user_id>")
def get_user(user_id):
    """
    Returns the user with the given ID

    Args:
    user_id (int): The user ID
    """

    user = find_modify_user(user_id, users)
    if user is None:
        abort(404, f"User with ID {user_id} not found.")
    return user


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8989)

# To run the app, type "python app.py" in the terminal
