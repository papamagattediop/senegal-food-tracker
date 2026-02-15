"""Application settings and configuration."""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Database configuration
DATABASE = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': int(os.getenv('DB_PORT', 5432)),
    'name': os.getenv('DB_NAME', 'senegal_food_tracker'),
    'user': os.getenv('DB_USER', 'postgres'),
    'password': os.getenv('DB_PASSWORD', ''),
}

# Scraping configuration
SCRAPING = {
    'user_agent': os.getenv('USER_AGENT', 'Mozilla/5.0'),
    'delay': int(os.getenv('SCRAPING_DELAY', 2)),
    'max_retries': int(os.getenv('MAX_RETRIES', 3)),
}

# Logging configuration
LOGGING = {
    'level': os.getenv('LOG_LEVEL', 'INFO'),
    'file': os.getenv('LOG_FILE', 'logs/app.log'),
}

# Data directories
DATA_DIR = BASE_DIR / 'data'
RAW_DATA_DIR = DATA_DIR / 'raw'
PROCESSED_DATA_DIR = DATA_DIR / 'processed'
EXTERNAL_DATA_DIR = DATA_DIR / 'external'

# Logs directory
LOGS_DIR = BASE_DIR / 'logs'

# Dashboard configuration
DASHBOARD = {
    'port': int(os.getenv('DASHBOARD_PORT', 8501)),
    'host': os.getenv('DASHBOARD_HOST', 'localhost'),
}
