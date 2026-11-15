# ADR 001 — Compute platform
**Status:** Accepted — implemented in the AWS prototype on 2026-11-15

**Context:** DocuWorks has a small existing application on a physical server.

**Decision:** Use EC2 for the initial migration prototype.

**Alternatives:** API Gateway + Lambda rewrite; ECS Fargate.

**Why:** Direct Linux hosting avoids unnecessary application redesign, exposes infrastructure-management concepts and fits a small workload.

**Trade-offs:** We manage the OS and runtime; a single instance is not highly available. Production patching and recovery need operating procedures.
