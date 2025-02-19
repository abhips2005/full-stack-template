from fastapi import APIRouter
from api.routes import status  # Add your core routes

api_router = APIRouter()
api_router.include_router(status.router)
# Add your core routes here
