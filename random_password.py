import random
import string


"""Generate random password with letters, numbers, and special characters.  
    Use for reseting password procedure.  """

def random_password(password_length):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(password_length))

