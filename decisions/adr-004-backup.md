# ADR 004 — Recovery strategy
**Status:** Accepted — partially implemented; restore test pending

**Context:** Manual backup on the existing physical server is an operational risk.

**Decision:** Use EBS snapshots for application-data backup and demonstrate a real restore operation. Enable S3 versioning for document objects; document retention and object recovery still need assessment.

**Implementation status (2026-11-15):** EBS snapshot `snap-0af6e7490c0fcb177` reached `completed`; S3 versioning is enabled. A restore, automated snapshot schedule and retention policy have **not** yet been demonstrated.

**Alternatives:** Manual data copies; AWS Backup managed plans.

**Why:** A snapshot exercise directly tests the ability to recover application data with limited project complexity.

**Trade-offs:** Snapshots cost money, require retention decisions, and should be created from consistent app data. S3 versioning alone does not equal independent backup.
