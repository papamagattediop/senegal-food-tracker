"""Script to run scrapers."""
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from utils.logger import setup_logger

logger = setup_logger()


def main():
    """Main execution function."""
    logger.info("Starting scraping process...")

    # TODO: Implement scraper execution logic

    logger.info("Scraping process completed.")


if __name__ == "__main__":
    main()
