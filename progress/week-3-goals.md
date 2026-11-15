# Week 3 goals and current status

**Last updated: 2026-11-15.** This is an interim status, not a completed Week 3 submission.

| Goal | Status |
| --- | --- |
| Linux application environment | **Done manually** — Amazon Linux 2023, Python 3.12 |
| Deploy functioning sample app | **Done** — Flask with Gunicorn/systemd, accessible via SSM port forwarding |
| Persistent application data | **Done** — SQLite at `/data/docuworks/docuworks.db` on 8 GB XFS EBS |
| Document storage and workflow | **Done** — private S3, upload, download, search, status changes |
| Restart and data persistence test | **Done** — EBS remounted from `/etc/fstab`; SQLite and S3 content verified |
| Application restart/auto-start | **Partial** — service enabled and running; reboot auto-start still to verify |
| EBS backup | **Snapshot created and completed** — `snap-0af6e7490c0fcb177` |
| Actual restore and EC2 replacement test | **Open** |
| Basic monitoring and logging | **Partial** — systemd journal checked; CloudWatch/metrics open |
| Updated final architecture diagram | **Open** |
| Automated infrastructure + application provisioning | **Partial** — Terraform creates cloud resources; Linux setup remains manual |

## Next actions
1. Restore SQLite from the completed EBS snapshot to a separate volume and verify records.
2. Add CloudWatch metrics/logging with cost-aware configuration.
3. Automate the EC2 software, EBS mount and systemd deployment to make rebuilds reproducible.
4. Supplement the existing four screenshots with recovery and monitoring evidence; update final architecture using AWS icons, evaluate security/cost, finish DCI review materials.

**Scope limitation:** No public staff-facing app endpoint/authentication exists. The SSM tunnel is a temporary, restricted demo method; not a multi-employee access solution.
