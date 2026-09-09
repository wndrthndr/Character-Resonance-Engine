from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.character import router as character_router
from api.question import router as question_router
from api.quiz import router as quiz_router


app = FastAPI(
    title="Character Resonance Engine",
    version="2.0.0",
    description="Adaptive Character Recommendation Engine"
)


# ==========================================================
# CORS
# ==========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # Change this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==========================================================
# ROUTERS
# ==========================================================

app.include_router(character_router)
app.include_router(question_router)
app.include_router(quiz_router)


# ==========================================================
# ROOT
# ==========================================================

@app.get("/")
def root():
    return {
        "message": "Character Resonance Engine API",
        "version": "2.0.0",
        "status": "running"
    }


# ==========================================================
# HEALTH CHECK
# ==========================================================

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


# ==========================================================
# RUN
# ==========================================================
if __name__ == "__main__":
    import os
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000)),
        reload=False
    )
