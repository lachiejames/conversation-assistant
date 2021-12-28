from pathlib import Path
from setuptools import find_packages, setup

ROOT_DIRECTORY = Path(__file__).parent
__version__ = "0.3.0"


setup(
    name="conversation_assistant",
    version=__version__,
    description="Suggests messages to respond with based on your conversation history",
    url="https://pypi.org/project/conversation_assistant/",
    packages=find_packages(),
)
