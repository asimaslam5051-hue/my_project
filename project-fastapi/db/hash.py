from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash:
    @staticmethod
    def bcrypt_password(password: str) -> str:
         password = password[:72]
         return pwd_context.hash(password)

    @staticmethod
    def verify(hashed_password: str, plain_password: str) -> bool:
         password = plain_password[:72]
         return pwd_context.verify(password, hashed_password)
