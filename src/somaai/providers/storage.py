
# TODO: implement storage provider - V2

"""Storage provider."""

from typing import BinaryIO


class StorageProvider:
    """Storage provider interface."""

    async def upload(self, file: BinaryIO, path: str) -> str:
        """Upload a file."""
        return path

    async def download(self, path: str) -> bytes:
        """Download a file."""
        return b""

    async def delete(self, path: str) -> None:
        """Delete a file."""
        pass
