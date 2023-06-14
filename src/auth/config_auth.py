from fastapi_users import FastAPIUsers
from fastapi_users.authentication import CookieTransport, JWTStrategy, AuthenticationBackend
from config import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY
from auth.models import User
from auth.manager import get_user_manager

SECRET = SECRET_KEY

cookie_transport = CookieTransport(cookie_name="test_app_file_csv",  cookie_max_age=ACCESS_TOKEN_EXPIRE_MINUTES)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=ACCESS_TOKEN_EXPIRE_MINUTES)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)
