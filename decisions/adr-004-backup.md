# ADR 004 — Recovery strategy
**Status:** Proposed

**Context:** Manual backup on the existing physical server is an operational risk.

**Decision:** Demonstrate EBS snapshot creation and at least one real restore operation; enable S3 versioning, define document retention and test object recovery if feasible.

**Alternatives:** Manual data copies; AWS Backup managed plans.

**Why:** A snapshot exercise directly tests the ability to recover application data with limited project complexity.

**Trade-offs:** Snapshots cost money, require retention decisions, and should be created from consistent app data. S3 versioning alone does not equal independent backup.
