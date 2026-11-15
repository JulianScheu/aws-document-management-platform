# ADR 001 — Compute platform
**Status:** Proposed

**Context:** DocuWorks has a small existing Linux-based application on a physical server.

**Decision:** Use EC2 for the initial migration prototype.

**Alternatives:** API Gateway + Lambda rewrite; ECS Fargate.

**Why:** Direct Linux hosting avoids unnecessary application redesign, exposes infrastructure-management concepts and fits a small workload.

**Trade-offs:** We manage the OS and runtime; a single instance is not highly available. Production patching and recovery need operating procedures.
