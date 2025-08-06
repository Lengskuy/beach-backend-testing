from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import beach_routes

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://beach-frontend-testing.onrender.com"],  # change to specific domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(
    beach_routes.router, 
    prefix="/beaches",
    tags=["Beaches"]
)

@app.get("/")
def root():
    return {"message": "Beach Monitoring API"}
