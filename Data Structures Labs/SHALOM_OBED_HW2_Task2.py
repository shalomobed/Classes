import hashlib

password_table = {}

#HASHING A PASSWORD using SHA-256
def hash_password(password):
    #SHA-256 will be changed to .sha256
    return hashlib.sha256(password.encode()).hexdigest()

#STORING PASSWORD
def save_password(username, password):
    if username in password_table:
        return f"Error: Username: '{username} is already taken.'"
    
    hashed = hash_password(password)
    password_table[username] = hashed
    return f"Password saved for user: {username}"

#COMPARING PASSWORDS
def compare_password(username, password):
    if username not in password_table:
        return f"Error: Username '{username} not found."
    
    hashed_input = hash_password(password)
    return hashed_input == password_table[username]

#CHANGING PASSWORDS (only if they provide their current password correctly)
def change_password(username, old_password, new_password):
    if username not in password_table:
        return f"Error: Username '{username} not found."
    
    if not compare_password(username, old_password):
        return "Error: Incorrect current password."
    
    password_table[username] = hash_password(new_password)
    return f"Password changed successfully for user: {username}"

#Sample Codes
print(save_password("user1", "mypassword123"))
print(save_password("user1", "newpassword456"))
print(save_password("user2", "securepassword456"))
print(compare_password("user1", "mypassword123"))
print(compare_password("user1", "wrongpassword"))
print(compare_password("user3", "any_password"))
