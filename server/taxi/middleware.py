from urllib.parse import parse_qs

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.db import close_old_connections
from channels.auth import AuthMiddleware, AuthMiddlewareStack, UserLazyObject
from channels.db import database_sync_to_async
from channels.sessions import CookieMiddleware, SessionMiddleware
from rest_framework_simplejwt.tokens import AccessToken

User = get_user_model()

@database_sync_to_async
def get_user(scope):
  print("this is scope", scope)
  close_old_connections()
  query_string = parse_qs(scope['query_string'].decode())
  token = query_string.get('token')
  if not token:
    return AnonymousUser()

  try:
    access_token = AccessToken(token[0])
    print('access_token', access_token)
    user = User.objects.get(id=access_token['id'])
  except Exception as exc:
    return AnonymousUser()

  return user if user.is_active else AnonymousUser()

class TokenAuthMiddleware(AuthMiddleware):
  async def resolve_scope(self, scope):
    print('new scope', scope)
    scope['user']._wrapped = await get_user(scope)


def TokenAuthMiddlewareStack(inner):
  return CookieMiddleware(SessionMiddleware(TokenAuthMiddleware(inner)))