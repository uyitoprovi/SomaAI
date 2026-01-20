"""Users module service."""


class UserService:
    """User service."""

    async def get_user(self, user_id: str) -> dict:
        """Get a user by ID."""
        return {"id": user_id}
