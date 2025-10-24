from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.auth.jwt_handler import verify_access_token

class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            token = credentials.credentials
            user_id = verify_access_token(token)
            if user_id is None:
                raise HTTPException(status_code=403, detail="Token inválido ou expirado")
            return user_id
        else:
            raise HTTPException(status_code=403, detail="Credenciais ausentes")
