from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .routers import auth, workouts, routines

app = FastAPI()

Base.metadata.create_all(bind=engine)

#update CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health_check():
    return { "Health check": "Complete" }

app.include_router(auth.router)
app.include_router(workouts.router)
app.include_router(routines.router)

