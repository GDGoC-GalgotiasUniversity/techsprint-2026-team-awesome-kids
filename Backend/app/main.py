# app/main.py

from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from app.api.v1.endpoints import auth, bots, api_keys, users, oauth, recruiter
from app.core.config import settings
from app.api.v1.endpoints import agora  # <-- 1. IMPORT THE NEW ROUTER

app = FastAPI(
    title="TwinlyAI API",
    description="API for the TwinlyAI SaaS application.",
    version="0.1.0"
)

app.add_middleware(
    SessionMiddleware,
    secret_key=settings.SESSION_SECRET_KEY
)

# --- FIX: Updated CORS Middleware ---
origins = [
    "http://localhost:3000",
    "http://localhost:3001",
    "http://127.0.0.1:3000",
    "http://localhost:8000", # Backend itself (Swagger UI)
    "https://twinly-ai-frontend.vercel.app",
    "https://twinly-ai.vercel.app"
    # Add your ngrok URL here if you are using one, e.g.:
    # "https://your-frontend.ngrok-free.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Router Setup
api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(bots.router, prefix="/bots", tags=["bots"])
api_router.include_router(api_keys.router, prefix="/api-keys", tags=["api-keys"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(oauth.router, prefix="/oauth", tags=["oauth"])
api_router.include_router(recruiter.router, prefix="/recruiter", tags=["recruiter"])
api_router.include_router(agora.router, prefix="/agora", tags=["agora"]) # <-- 2. ADD THE NEW ROUTER

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to TwinlyAI API"}