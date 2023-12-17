import os

LOG_DIR = os.path.join("logs")
os.makedirs(LOG_DIR, exist_ok=True)
LOG_PATH = os.path.join(LOG_DIR, "api.log")
