from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import recipes

app = FastAPI()

# CORS middleware (allow frontend requests)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(recipes.router)
