"""Meta service for curriculum metadata operations."""

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from somaai.contracts.meta import GradeResponse, SubjectResponse, TopicResponse
from somaai.db.models import Grade, Subject, Topic


class MetaService:
    """Service for curriculum metadata operations.

    Provides access to grades, subjects, and topics data
    from the Rwanda Education Board curriculum.
    """

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_grades(self) -> list[GradeResponse]:
        """Get all available grade levels.
        Returns:
            List of grades (P1-P6, S1-S6) with display names
        Order:
            Returns grades in ascending order (P1, P2, ..., S6)
        """
        result = await self.session.execute(select(Grade).order_by(Grade.display_order))
        grades = result.scalars().all()

        return [
            GradeResponse(
                id=g.id, name=g.name, display_order=g.display_order, level=g.level
            )
            for g in grades
        ]

    async def get_subjects(
        self,
        grade: str | None = None,
    ) -> list[SubjectResponse]:
        """Get subjects available for a grade.

        Args:
            grade: Grade ID to filter by (optional)

        Returns:
            List of subjects available for the grade
            Returns all subjects if grade is None
        """
        query = select(Subject).order_by(Subject.display_order)

        # NOTE:
        # Subjeect are global for MVP
        # Grade-based filtering can be added post-MVP if needed.
        result = await self.session.execute(query)
        subjects = result.scalars().all()

        return [
            SubjectResponse(
                id=s.id, name=s.name, display_order=s.display_order, icon=s.icon
            )
            for s in subjects
        ]

    async def get_topics(
        self,
        grade: str,
        subject: str,
    ) -> list[TopicResponse]:
        """Get topics for a grade and subject combination.

        Args:
            grade: Grade ID (required)
            subject: Subject ID (required)

        Returns:
            List of topics as a tree structure (with children)

        Structure:
            Topics are hierarchical - main topics contain sub-topics
        """
        result = await self.session.execute(
            select(Topic)
            .where(Topic.grade == grade, Topic.subject == subject)
            .order_by(Topic.created_at)
        )
        topics = result.scalars().all()

        return [
            TopicResponse(
                topic_id=t.id,
                title=t.title,
                grade=t.grade,
                subject=t.subject,
                doc_id=t.doc_id,
                page_start=t.page_start,
                page_end=t.page_end,
                path=t.path or [],
                document_count=1 if t.doc_id else 0,
            )
            for t in topics
        ]

    async def get_topic_by_id(self, topic_id: str) -> TopicResponse | None:
        """Get a single topic by ID.

        Args:
            topic_id: Topic ID

        Returns:
            Topic details or None if not found
        """
        result = await self.session.execute(select(Topic).where(Topic.id == topic_id))
        topic = result.scalar_one_or_none()

        if not topic:
            return None
        return TopicResponse(
            topic_id=topic.id,
            title=topic.title,
            grade=topic.grade,
            subject=topic.subject,
            doc_id=topic.doc_id,
            page_start=topic.page_start,
            page_end=topic.page_end,
            path=topic.path or [],
            document_count=1 if topic.doc_id else 0,
        )

    async def get_topics_by_ids(
        self,
        topic_ids: list[str],
    ) -> list[TopicResponse]:
        """Get multiple topics by IDs.

        Args:
            topic_ids: List of topic IDs

        Returns:
            List of topics (in same order as input IDs)
        """
        if not topic_ids:
            return []

        result = await self.session.execute(
            select(Topic).where(Topic.id.in_(topic_ids))
        )
        topics = result.scalars().all()

        topic_map = {t.id: t for t in topics}

        ordered_topics = [topic_map[tid] for tid in topic_ids if tid in topic_map]
        return [
            TopicResponse(
                topic_id=t.id,
                title=t.title,
                grade=t.grade,
                subject=t.subject,
                doc_id=t.doc_id,
                page_start=t.page_start,
                page_end=t.page_end,
                path=t.path or [],
                document_count=1 if t.doc_id else 0,
            )
            for t in ordered_topics
        ]
