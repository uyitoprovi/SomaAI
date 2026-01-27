import pytest
from httpx import AsyncClient


class TestMetaEndpoints:
    """Test cases for /api/v1/meta endpoints."""

    @pytest.mark.asyncio
    async def test_get_grades_returns_list(self, client: AsyncClient):
        response = await client.get("/api/v1/meta/grades")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    @pytest.mark.asyncio
    async def test_get_grades_contains_expected_fields(self, client: AsyncClient):
        response = await client.get("/api/v1/meta/grades")
        grades = response.json()
        if grades:
            grade = grades[0]
            assert "id" in grade
            assert "name" in grade
            assert "display_order" in grade
            assert "level" in grade

    @pytest.mark.asyncio
    async def test_get_subjects_without_grade(self, client: AsyncClient):
        response = await client.get("/api/v1/meta/subjects")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    @pytest.mark.asyncio
    async def test_get_subjects_with_grade_filter(self, client: AsyncClient):
        response = await client.get("/api/v1/meta/subjects?grade=P1")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    @pytest.mark.asyncio
    async def test_get_topics_requires_grade_and_subject(self, client: AsyncClient):
        response = await client.get("/api/v1/meta/topics")
        assert response.status_code == 422  # missing params

    @pytest.mark.asyncio
    async def test_get_topics_returns_list(self, client: AsyncClient):
        response = await client.get("/api/v1/meta/topics?grade=P1&subject=Mathematics")
        assert response.status_code == 200
        topics = response.json()
        assert isinstance(topics, list)
        if topics:
            t = topics[0]
            assert "topic_id" in t
            assert "title" in t
            assert "grade" in t
            assert "subject" in t
