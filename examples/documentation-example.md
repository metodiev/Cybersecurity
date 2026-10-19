# Documentation Example

This page demonstrates the three diagram types the academy uses most often in its authoring and review documentation. It is a working example, not a lesson. If the diagrams render in the local MkDocs site, the Mermaid integration is configured correctly.

## 1. Authoring and validation flow

The flowchart shows the path from a Markdown edit to a published page. The loop is intentional: failed checks return the author to the specific step that failed, not to the beginning.

```mermaid
flowchart TD
  A["Author edits Markdown"] --> B["make lint"]
  B --> C{"Lint passes?"}
  C -->|No| D["Fix style or structure"]
  D --> B
  C -->|Yes| E["make links"]
  E --> F{"Links and anchors valid?"}
  F -->|No| G["Fix target or anchor"]
  G --> E
  F -->|Yes| H["make manifest"]
  H --> I{"Manifest valid?"}
  I -->|No| J["Fix manifest or schema"]
  J --> H
  I -->|Yes| K["make build"]
  K --> L{"Strict build passes?"}
  L -->|No| M["Fix MkDocs warning"]
  M --> K
  L -->|Yes| N["Review and publish"]
```

**What to notice:** the manifest check comes before the site build because a broken prerequisite or path should fail fast. The build is strict, so a warning is a failure.

## 2. Review sequence

The sequence diagram shows the same work as an interaction between the author, CI, a reviewer, and MkDocs. It makes the hand-offs explicit.

```mermaid
sequenceDiagram
  autonumber
  actor Author
  participant CI as Git and CI
  participant Reviewer
  participant Site as MkDocs Material
  Author->>CI: Push Markdown and manifest changes
  CI->>CI: Validate manifest and source IDs
  CI->>CI: Lint Markdown and check links
  CI->>Site: Build with --strict
  Site-->>CI: Site artifact
  CI->>Reviewer: Request review with check results
  Reviewer-->>Author: Findings and required changes
  Author->>CI: Revise and push
  Reviewer->>Site: Approve publication
```

**What to notice:** the reviewer sees the check results before reading the content. The author is responsible for fixing the failed check, not the reviewer.

## 3. Page lifecycle

The state diagram mirrors the manifest's publication status. Validation is tracked separately from publication; a page can be published only after the required checks pass.

```mermaid
stateDiagram-v2
  [*] --> Planned
  Planned --> Drafted: Lesson and lab authored
  Drafted --> Reviewed: Peer review passed
  Reviewed --> LabValidated: Lab run on a clean environment
  LabValidated --> Published: Strict build and checks pass
  Published --> Deprecated: Superseded or withdrawn
  Drafted --> Planned: Review rejected
  Reviewed --> Drafted: Defects found
  LabValidated --> Reviewed: Lab drift found
```

**What to notice:** moving backward is allowed when evidence is found. The reason and reviewer must be recorded.

## Local commands

From the repository root:

```bash
make install   # create .venv and install pinned documentation dependencies
make serve     # serve at http://127.0.0.1:8000
make check     # manifest, links, Markdown lint, and strict build
make build     # strict build into site/
```

The optional Mermaid render check requires `mmdc` on `PATH`:

```bash
make mermaid
```

If `mmdc` is unavailable, the build still works; the script reports that rendering was skipped.
