from loguru import logger
import sys

logger.remove()

logger.add(
    sys.stdout,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
           "<level>{level}</level> | "
           "<cyan>{name}</cyan>:<cyan>{function}</cyan> - {message}",
    level="INFO"
)

logger.add(
    "logs/app.log",
    rotation="1 MB",
    level="INFO"
)