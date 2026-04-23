from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

# create app
app = FastAPI()

# Enable CORS for the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ensure data folder exists
os.makedirs("data/indexes", exist_ok=True)
from api.upload import router as upload_router
from api.analyze import router as analyze_router

app.include_router(analyze_router, prefix="/api")

app.include_router(upload_router, prefix="/api")

# ------------------ HEALTH CHECK ------------------

@app.get("/health")
def health():
    return {"status": "ok"}


# ------------------ ROOT ------------------

@app.get("/")
def root():
    return {"message": "Legal Lens AI Backend Running"}