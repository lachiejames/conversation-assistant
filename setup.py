from pathlib import Path
from setuptools import find_packages, setup

ROOT_DIRECTORY = Path(__file__).parent
__version__ = "0.3.2"


setup(
    name="conversation_assistant",
    version=__version__,
    description="Suggests messages for a user to respond with based upon their conversation history",
    packages=find_packages(),
)
