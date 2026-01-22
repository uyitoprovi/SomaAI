# SomaAI — MVP Scope (Frozen)

This file defines the frozen MVP scope for SomaAI.
Anything not listed here is considered **post-MVP** and should not be implemented without approval.

---

## ✅ MVP Endpoints

### Meta (Shared)
- [ ] GET /api/v1/meta/grades — list grades (sorted by display_order)
- [ ] GET /api/v1/meta/subjects — list subjects (sorted by display_order)

### Student
- [ ] GET /api/v1/student/profile
- [ ] GET /api/v1/student/courses
- [ ] GET /api/v1/student/lessons
- [ ] POST /api/v1/student/answers

### Teacher
- [ ] GET /api/v1/teacher/profile
- [ ] POST /api/v1/teacher/content
- [ ] GET /api/v1/teacher/students
- [ ] GET /api/v1/teacher/analytics

---

## 🚫 Explicitly Out of Scope (Post-MVP)

The following must NOT be worked on during MVP unless explicitly approved:

- Semantic cache / vector databases
- Request tracing / observability
- Authentication & authorization (JWT, OAuth, RBAC)
- Google Drive or external storage integrations
- Advanced AI orchestration or agents
- Billing, subscriptions, payments

---

## 📦 Post-MVP (Planned)

These will be considered after MVP is stable:

- Semantic caching for AI responses
- Tracing & performance monitoring
- Auth with roles (student / teacher / admin)
- GDrive / S3 integrations
- Advanced analytics dashboards

---

## 🧭 Why This Exists

- Prevents contributors from building random features
- Keeps PRs focused and reviewable
- Ensures MVP ships fast
- Makes onboarding contributors easier

Any change to this file requires maintainer approval.
