# ADR 002 — Separate storage responsibilities
**Status:** Proposed

**Context:** The original platform stores application data and documents on one machine.

**Decision:** S3 for uploaded document objects; separate gp3 EBS data volume for application-specific persistent data.

**Alternatives:** Keep everything on root EBS; EFS; RDS for structured app data.

**Why:** S3 documents survive instance replacement. EBS provides straightforward block storage for a low-throughput single-server application.

**Trade-offs:** EBS is AZ-specific and needs a deliberate mount/restore process. S3 object versioning is not a complete backup strategy.
