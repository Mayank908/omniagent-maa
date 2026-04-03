from neo4j import GraphDatabase
from .config import settings
import logging

logger = logging.getLogger(__name__)

class Memory:
    def __init__(self):
        self._driver = None
        self._uri = settings.NEO4J_URI
        self._user = settings.NEO4J_USER
        self._password = settings.NEO4J_PASSWORD

    def connect(self):
        try:
            self._driver = GraphDatabase.driver(self._uri, auth=(self._user, self._password))
            # Verify connectivity
            self._driver.verify_connectivity()
            logger.info("✅ Memory (Neo4j) is Pulsing!")
            return True
        except Exception as e:
            logger.error(f"❌ Memory Error: {e}")
            return False

    def close(self):
        if self._driver:
            self._driver.close()

    def run_query(self, query, parameters=None):
        if not self._driver:
            if not self.connect():
                return None
        
        with self._driver.session() as session:
            result = session.run(query, parameters)
            return [record.data() for record in result]

memory = Memory()
