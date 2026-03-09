from fastapi import Depends
from auth.auth_service import get_current_user

@router.get("/me")
def get_me(current_user = Depends(get_current_user)):
    return current_user