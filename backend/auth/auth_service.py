from models.user import User
from auth.security import hash_password, verify_password, create_access_token

def register_user(db, username, password, role):
    existing_user = db.query(User).filter(User.username == username).first()
    if existing_user:
        return False  

    user = User(
        username=username,
        password=hash_password(password),
        role=role
    )
    db.add(user)
    db.commit()
    return True

def authenticate_user(db, username, password):
    user = db.query(User).filter(User.username == username).first()
    if user and verify_password(password, user.password):
        return create_access_token(username)
    return None