import ollama
from .config import settings
import logging

logger = logging.getLogger(__name__)

class Brain:
    def __init__(self):
        self.client = ollama.Client(host=settings.OLLAMA_BASE_URL)
        self.model = settings.MODEL_NAME

    def check_health(self):
        """Verify Ollama Local Inference connectivity."""
        try:
            # list models to check connection
            response = self.client.list()
            # The ollama-python library returns an object with a 'models' attribute
            # where each model object has a 'model' attribute for its name.
            model_names = [m.model for m in response.models]
            
            if self.model in model_names or f"{self.model}:latest" in model_names:
                logger.info(f"✅ Brain (Ollama) is Thinking with {self.model}!")
                return True, "Online"
            else:
                available = ", ".join(model_names[:3])
                logger.warning(f"⚠️ Brain (Ollama) Online, but {self.model} not found. Available: {available}")
                return True, f"Model {self.model} not found. Available: {available}"
        except Exception as e:
            logger.error(f"❌ Brain Error: {e}")
            return False, str(e)

    def generate(self, prompt: str, system_prompt: str = ""):
        """Simple inference wrapper."""
        try:
            messages = []
            if system_prompt:
                messages.append({'role': 'system', 'content': system_prompt})
            messages.append({'role': 'user', 'content': prompt})
            
            response = self.client.chat(model=self.model, messages=messages)
            return response['message']['content']
        except Exception as e:
            logger.error(f"❌ Inference Error: {e}")
            return None

brain = Brain()
