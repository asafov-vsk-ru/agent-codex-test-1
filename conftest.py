import os
import pytest

from dotenv import load_dotenv

load_dotenv()


# pytest_plugins = [
#    'fixtures.page'
# ]


@pytest.fixture(autouse=True, scope="session")
def init_environment():
    host = os.getenv("BASE_HOST")
    api_token = os.getenv("API_TOKEN")
