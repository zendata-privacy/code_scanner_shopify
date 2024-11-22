# Hardcoded cookie example (Insecure)
USER_SESSION_COOKIE = "user_id=12345; name=JohnDoe; email=john.doe@example.com"

def get_user_info_from_cookie():
    print("Retrieving user info from hardcoded cookie...")
    # Parse hardcoded cookie (Insecure)
    user_info = dict(item.split("=") for item in USER_SESSION_COOKIE.split("; "))
    return user_info

user_info = get_user_info_from_cookie()
print(f"User ID: {user_info['user_id']}, Name: {user_info['name']}, Email: {user_info['email']}")
