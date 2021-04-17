
from fastapi import APIRouter
from apps.models import User
router = APIRouter()


@router.get("/")
def read_root():
    users = User.objects.last()
    user_name = 'Guest'
    if users:
        user_name = users.username
    return {"Hello": user_name}
