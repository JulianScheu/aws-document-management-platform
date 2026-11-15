# ADR 003 — Administration and access
**Status:** Proposed

**Context:** Administrative access and customer documents must not be publicly exposed.

**Decision:** No inbound security-group rules in the initial Terraform deployment. Use AWS Systems Manager Session Manager for administration; instance IAM role for scoped S3 access; S3 Block Public Access and encryption.

**Alternatives:** Public SSH; static access keys in files; public S3 bucket.

**Why:** Reduce credential exposure and unintended network access.

**Trade-offs:** SSM permissions and connectivity must work. This is an administrative prototype path, **not an employee-facing authentication and HTTPS design**; the latter must be solved before claiming production suitability.
