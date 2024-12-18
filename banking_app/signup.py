# signup.py - Placeholder for signup functionality
import csv

def password_check(password):
    
    count = 0
    if len(password) > 8:
        count += 1
        return True
    if any(char.isupper() for char in password):
        count += 1
        return True
    if any(char.islower() for char in password):
        count += 1
        return True
    if any(char.isdigit() for char in password):
        count += 1
        return True
    
    if count == 4:
        print("Valid")
        return True
    else:
        raise ValueError("Password incorrect somehow")
    
def username_check(username):
    with open('database.csv', 'r') as csv_file:
        database_reader = csv.DictReader(csv_file)
        
        for row in database_reader:
            if username == row['username']:
                raise ValueError("Username already exsists")
            else:
                return True

def signup(username, password, email):
    """
    Handles the user signup process by validating the provided username, password, and email.

    Instructions for Implementation:
    1. **Input Validation**:
        - Ensure that all fields (`username`, `password`, `email`) are non-empty strings.
        - If any field is empty, raise a `ValueError`.
        - Validate that the `email` follows the correct format (e.g., using a regular expression for email validation).
        - Ensure the `password` meets minimum security criteria (e.g., at least 8 characters long, contains a mix of uppercase, lowercase, and digits).
        - If the `password` is weak (e.g., a simple password like "123"), raise a `ValueError`.

    2. **Username Uniqueness Check**:
        - Check if the `username` already exists in the user database.
        - If the `username` is already taken, raise a `ValueError`.

    3. **Create New User**:
        - If all validations pass and the username is unique, create a new user with the provided `username`, `password`, and `email`.
        - The `password` should be securely hashed before storing it (if using password hashing).
        - Add the new user to the user database.

    4. **Edge Cases**:
        - Handle cases where any of the input fields are empty.
        - Handle invalid email formats using proper regular expression checks.
        - Handle cases where the `username` is already taken.
        - Ensure that weak passwords (e.g., less than 8 characters or easily guessable) are rejected.

    Parameters:
    - `username` (str): The desired username for the new user.
    - `password` (str): The password chosen by the user.
    - `email` (str): The email address provided by the user.

    Returns:
    - bool: `True` if the signup is successful, otherwise raises a `ValueError` for invalid input.
    """

    
    special_char = "!@#$%^&*()?/|<>,.:;~`'"
    if username.isspace() or password.isspace():
        raise ValueError("Username or Password cannot be empty")

    for char in special_char:
        if char in username:
            raise ValueError("Username cannot contain special characters")
        
    email_stuff = "gmail yahoo @ .com"
    if any(char not in email for char in email_stuff):
        raise ValueError("Email is in incorrect format")
    
    with open('database.csv', 'w') as csv_file:
        field_names = ['username','password','email','account_id','balance']
        database_writer = csv.DictWriter(csv_file,fieldnames=field_names)      
          
        database_writer.writerow({'username':username, 'password':password, 'email':email,'account_id': 'example','balance':'example'})

print(signup('OnaOnline', 'Zwan30n@', 'onasihle123@gmail.com'))