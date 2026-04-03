from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):
    # Memory: Neo4j
    NEO4J_URI: str = "bolt://localhost:7687"
    NEO4J_USER: str = "neo4j"
    NEO4J_PASSWORD: str = "mirofish_maa"

    # Brain: Ollama
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    MODEL_NAME: str = "llama3.2:latest"

    # Swarm: MiroFish-Offline
    SIMULATION_MAX_AGENTS: int = 100
    SIMULATION_SEED_PATH: str = "./context_vault/blueprints"
    REPORT_AGENT_NAME: str = "Sentinel"

    # Backend Ops
    API_PORT: int = 8000
    API_HOST: str = "0.0.0.0"
    DEBUG: bool = True
    LOG_LEVEL: str = "info"

    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(__file__), "../../.env"),
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()
