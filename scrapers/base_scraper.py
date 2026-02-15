"""Base scraper class with common functionality."""
from abc import ABC, abstractmethod
import requests
from bs4 import BeautifulSoup
import time
from loguru import logger


class BaseScraper(ABC):
    """Abstract base class for all scrapers."""

    def __init__(self, base_url, user_agent=None, delay=2):
        """
        Initialize the scraper.

        Args:
            base_url: Base URL for the website
            user_agent: User agent string
            delay: Delay between requests in seconds
        """
        self.base_url = base_url
        self.delay = delay
        self.headers = {
            'User-Agent': user_agent or 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        self.session = requests.Session()

    def fetch_page(self, url):
        """
        Fetch a page and return BeautifulSoup object.

        Args:
            url: URL to fetch

        Returns:
            BeautifulSoup object or None if error
        """
        try:
            time.sleep(self.delay)
            response = self.session.get(url, headers=self.headers, timeout=30)
            response.raise_for_status()
            return BeautifulSoup(response.content, 'html.parser')
        except Exception as e:
            logger.error(f"Error fetching {url}: {e}")
            return None

    @abstractmethod
    def scrape(self):
        """Main scraping method to be implemented by subclasses."""
        pass

    @abstractmethod
    def parse(self, soup):
        """Parse the page content."""
        pass
