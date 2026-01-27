"""Meta endpoints for curriculum metadata."""

from fastapi import APIRouter, Query, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from somaai.db.session import get_session
from somaai.modules.meta.service import MetaService
from somaai.contracts.meta import GradeResponse, SubjectResponse, TopicResponse

router = APIRouter(prefix="/meta", tags=["meta"])


@router.get("/grades", response_model=list[GradeResponse])
async def get_grades(session: AsyncSession = Depends(get_session)):
    """Get all available grade levels.

    Returns list of grades (P1–P6 for primary, S1–S6 for secondary)
    with display names and sort order.
    """
    service = MetaService(session)
    return await service.get_grades()


@router.get("/subjects", response_model=list[SubjectResponse])
async def get_subjects(
    grade: str | None = Query(None, description="Filter by grade ID"),
    session: AsyncSession = Depends(get_session),
):
    """Get available subjects.

    Optionally filter by grade level.
    Returns all subjects if no grade specified.
    """
    service = MetaService(session)
    return await service.get_subjects(grade)


@router.get("/topics", response_model=list[TopicResponse])
async def get_topics(
    grade: str = Query(..., description="Grade ID (required)"),
    subject: str = Query(..., description="Subject ID (required)"),
    session: AsyncSession = Depends(get_session),
):
    """Get topics for a grade and subject.

    Returns hierarchical topic tree for curriculum navigation.
    Topics include document count for availability indication.
    """
    service = MetaService(session)
    return await service.get_topics(grade, subject)
