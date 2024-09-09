from project.library import Library
from project.user import User


class Registration:
    def add_user(self, user: User, library: Library):
        if user in library.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        library.user_records.append(user)

    def remove_user(self, user: User, library: Library):
        if user in library.user_records:
            library.user_records.remove(user)
        else:
            return f"We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library: Library):
        for u in library.user_records:
            if user_id == u.user_id and new_username != u.username:

                for u_name, data in library.rented_books.items():
                    if u_name == u.username:
                        del library.rented_books[u_name]
                        library.rented_books[new_username] = data
                u.username = new_username
                return f"Username successfully changed to: {new_username} for user id: {user_id}"
            if user_id == u.user_id and new_username == u.username:
                return f"Please check again the provided username - it should be different than the username used so far!"
        return f"There is no user with id = {user_id}!"
