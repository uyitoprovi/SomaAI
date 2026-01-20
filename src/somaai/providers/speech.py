# TODO: implement storage provider - V2

"""Speech provider."""


class SpeechProvider:
    """Speech provider interface (for future use)."""

    async def transcribe(self, audio_data: bytes) -> str:
        """Transcribe audio to text."""
        return ""

    async def synthesize(self, text: str) -> bytes:
        """Synthesize text to audio."""
        return b""
