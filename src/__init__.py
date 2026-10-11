"""qanoon-rag: Arabic legal Q&A over the Egyptian Civil Code, with article citations."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("qanoon-rag")
except PackageNotFoundError:  # running from source without installing
    __version__ = "0.0.0"
