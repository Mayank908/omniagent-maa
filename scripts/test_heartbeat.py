import os
import sys
import asyncio
from neo4j import GraphDatabase
import ollama
from dotenv import load_dotenv

# Load Environment from backend/.env.example if .env is missing
load_dotenv(os.path.join(os.path.dirname(__file__), '../backend/.env'))

def test_memory():
    """Verify Neo4j Graph Database connectivity."""
    print("🧠 Testing Memory (Neo4j)...")
    uri = os.getenv("NEO4J_URI", "bolt://localhost:7687")
    user = os.getenv("NEO4J_USER", "neo4j")
    pwd = os.getenv("NEO4J_PASSWORD", "mirofish_maa")
    
    try:
        driver = GraphDatabase.driver(uri, auth=(user, pwd))
        with driver.session() as session:
            session.run("MERGE (n:System {name: 'OmniAgent', status: 'Online'})")
        print("✅ Memory (Neo4j) is Pulsing!")
        return True
    except Exception as e:
        print(f"❌ Memory Error: {e}")
        return False

def test_brain():
    """Verify Ollama Local Inference connectivity."""
    print("🤖 Testing Brain (Ollama)...")
    model = os.getenv("MODEL_NAME", "llama3.2:latest")
    
    try:
        response = ollama.chat(model=model, messages=[
            {'role': 'user', 'content': 'Say Hello Project MAA in one sentence.'}
        ])
        print(f"✅ Brain (Ollama) Thinking: {response['message']['content']}")
        return True
    except Exception as e:
        print(f"❌ Brain Error: {e}")
        return False

def main():
    print("🚀 --- Project MAA Heartbeat Test --- 🚀")
    m_ok = test_memory()
    b_ok = test_brain()
    
    if m_ok and b_ok:
        print("\n🏆 STATUS: FULLY ONLINE (Zero-Error Infrastructure Verified)")
    else:
        print("\n⚠️ STATUS: CRITICAL FAILURE (Check your Mainframe logs)")
        sys.exit(1)

if __name__ == "__main__":
    main()
