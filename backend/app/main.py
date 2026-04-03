from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
from dotenv import load_dotenv

# Import Core Components
from .core.memory import memory
from .core.brain import brain
from .core.config import settings

app = FastAPI(
    title="OmniAgent (MAA) | The Swarm Intelligence Factory",
    description="High-performance multi-agent orchestration platform.",
    version="0.1.0"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "project": "OmniAgent (MAA)",
        "status": "Online",
        "engine": "MiroFish-Offline",
        "philosophy": "Plan, Simulate, Observe"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint to verify infrastructure."""
    m_ok = memory.connect()
    b_ok, b_status = brain.check_health()
    
    return {
        "status": "Alive" if (m_ok and b_ok) else "Partially Online",
        "memory": "Connected" if m_ok else "Disconnected (Neo4j)",
        "brain": b_status
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.API_HOST, port=settings.API_PORT, reload=settings.DEBUG)
