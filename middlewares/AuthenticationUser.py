# -*- coding: utf-8 -*-
"""
@Auth ： 胡玉龙
@File ：JwtAuth.py
@IDE ：PyCharm
"""
from fastapi_users.jwt import decode_jwt
from starlette.authentication import AuthenticationBackend, AuthenticationError, AuthCredentials

from app.api.v1.models import UserModel


class AuthenticationUser(AuthenticationBackend):
    async def authenticate(self, request):
        if "Authorization" not in request.headers and 'cookie' not in request.headers:
            return
        if '/auth/jwt/login' in request.url.path:
            return
        try:
            if "Authorization" in request.headers:
                auth = request.headers["Authorization"]
                scheme, credentials = auth.split()
                if scheme.lower() == 'basic':
                    return
            # 'cookie' in request.headers:
            else:
                cookie = request.headers['cookie']
                scheme, credentials = cookie.split('=')
            payload = decode_jwt(credentials, 'SECRET', ['fastapi-users:auth'])
            user_id = payload.get('user_id')
            user = await UserModel.filter(id=user_id).first()
            return AuthCredentials(["authenticated"]), user
        except Exception as ex:
            raise AuthenticationError('Invalid auth credentials')
