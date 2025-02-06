from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Server configuration
SERVER_URL = 'localhost'
PORT = '8900'
ENV = 'dev'

# Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
