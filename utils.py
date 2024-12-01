from constants import valid_user_fields


def find_modify_user(user_id, users, user_new_props=None):
    """
    Finds a user by their ID in the provided list of users. If an update dictionary is provided, will update the User

    Args:
        user_id (int): The ID of the user to find.
        users (list): A list of dictionaries containing user information.

    Returns:
        dict or None: The user dictionary if found, otherwise None.
    """
    for user in users:
        if user["id"] == user_id:
            if user_new_props is not None and all(
                keys in valid_user_fields for keys in user_new_props
            ):
                # user.update(user_new_props)
                user.update((k, v) for k, v in user_new_props.items())
            return user

    return None
