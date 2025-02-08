from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from auth import authenticate_user, create_access_token, get_current_user
import logging

user_router = APIRouter()


# Ruta pública para autenticación y generación de token
@user_router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Ruta para autenticar al usuario y devolver un token JWT.
    """
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        logging.warning(f"Intento fallido de inicio de sesión para {form_data.username}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(data={"sub": user["username"]})
    logging.info(f"Token generado exitosamente para {user['username']}")
    return {"access_token": access_token, "token_type": "bearer"}


# Ruta protegida: obtener lista de usuarios
@user_router.get("/")
def get_users(current_user: dict = Depends(get_current_user)):
    """
    Devuelve la lista de usuarios, solo accesible con token válido.
    """
    logging.info(f"Usuario autenticado {current_user['username']} accedió a la lista de usuarios")
    return {"users": ["Alice", "Bob", "Charlie"]}


# Ruta protegida: crear un nuevo usuario
@user_router.post("/")
def create_user(user: dict, current_user: dict = Depends(get_current_user)):
    """
    Permite crear un nuevo usuario, accesible solo para usuarios autenticados.
    """
    logging.info(f"Usuario {current_user['username']} creó un nuevo usuario: {user}")
    return {"message": "Usuario creado exitosamente", "user": user}
