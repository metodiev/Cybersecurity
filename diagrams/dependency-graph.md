# Dependency Graph

> **Status:** generated architecture view. All edges come from [`manifest/course-manifest.yaml`](../manifest/course-manifest.yaml). Do not hand-edit edges.

## Table of contents

- [Graph metadata](#graph-metadata)
- [How to read these diagrams](#how-to-read-these-diagrams)
- [Diagram 1 — Level spine](#diagram-1-level-spine)
- [Diagram 2 — Foundations detail](#diagram-2-foundations-detail)
- [Diagram 3 — Application and product security chain](#diagram-3-application-and-product-security-chain)
- [Diagram 4 — Binary exploitation and reverse-engineering chain](#diagram-4-binary-exploitation-and-reverse-engineering-chain)
- [Diagram 5 — Adversary emulation and control-validation chain](#diagram-5-adversary-emulation-and-control-validation-chain)
- [Diagram 6 — Detection and response chain](#diagram-6-detection-and-response-chain)
- [Diagram 7 — Forensics, malware, and case chain](#diagram-7-forensics-malware-and-case-chain)
- [Diagram 8 — Cloud, container, and platform engineering chain](#diagram-8-cloud-container-and-platform-engineering-chain)
- [Diagram 9 — Data, cryptography, supply-chain, and privacy chain](#diagram-9-data-cryptography-supply-chain-and-privacy-chain)
- [Diagram 10 — Research and teaching strand](#diagram-10-research-and-teaching-strand)
- [What the graph guarantees](#what-the-graph-guarantees)
- [What the graph does not guarantee](#what-the-graph-does-not-guarantee)
- [Maintenance](#maintenance)

## Graph metadata

| Property | Value |
|---|---|
| Source of truth | [`manifest/course-manifest.yaml`](../manifest/course-manifest.yaml) |
| Modules | 67 |
| Edges | All prerequisite relationships in the manifest |
| Layout | One overview plus nine dependency-chain slices |
| Renderer | Mermaid CLI 12.0.0 |
| Rendered | 2026-10-19 |
| Result | 10 of 10 diagrams rendered successfully |

## How to read these diagrams

The dependency graph is split into one overview and nine readable slices. An arrow means **“is a prerequisite of”**: `A --> B` means A must be completed before B.

The diagrams show only prerequisites internal to each slice. Every slice lists its external prerequisites below it. The authoritative, machine-readable edge list is in [`manifest/course-manifest.yaml`](../manifest/course-manifest.yaml); if a diagram and the manifest disagree, the manifest wins.

### Diagram 1: Level spine

```mermaid
flowchart LR
  L0["L0<br/>Orientation and labcraft<br/>ORI-01 to ORI-03"]
  L1["L1<br/>Systems foundations<br/>SYS · NET · PRG · CRY · IAM · DAT · GIT"]
  L2["L2<br/>Core security practice<br/>SEC · APP · WEB · API · VUL · NET · END · LOG · IR · RSK · CLD · CNT"]
  L3["L3<br/>Advanced specialization<br/>EXP · REV · MAL · AD · CLD · K8S · LOG · IR · FOR · TI · CRY · SCS · AI · OFF"]
  L4["L4<br/>Expert practice and leadership<br/>RED · PUR · ARC · PDE · SRE · FOR · MAL · GOV · PRI · TCH"]
  L5["L5<br/>Research and contribution<br/>RES-01 to RES-07"]
  CAP["Capstones<br/>CAP-01 to CAP-05"]
  L0 --> L1 --> L2 --> L3 --> L4 --> L5
  L4 --> CAP
  L5 --> CAP
```

The spine is a **minimum depth order**, not a lock-step sequence. A learner may start a research-strand module in parallel with technical modules once its prerequisites are met.

### Diagram 2: Foundations detail

```mermaid
flowchart TD
  subgraph SG_ORI [Orientation]
    ORI01["ORI-01<br/>Security Mindset, Ethics, Law, and Labcraft"]
    ORI02["ORI-02<br/>Threat Modeling Foundations"]
    ORI03["ORI-03<br/>Technical Writing, Evidence, and Reproducibility"]
  end
  subgraph SG_SYS [Systems]
    SYS01["SYS-01<br/>Computer Architecture and Memory"]
    SYS02["SYS-02<br/>Operating Systems Internals"]
    SYS03["SYS-03<br/>Linux Administration and Hardening"]
    SYS04["SYS-04<br/>Windows Architecture, Registry, NTFS, and AD Preview"]
  end
  subgraph SG_NET [Networking]
    NET01["NET-01<br/>Networking and TCP/IP"]
    NET02["NET-02<br/>DNS, HTTP, and TLS"]
  end
  subgraph SG_CODE [Programming and supply chain]
    PRG01["PRG-01<br/>Python for Security Engineering"]
    PRG02["PRG-02<br/>Bash and PowerShell for Operators"]
    GIT01["GIT-01<br/>Git, CI/CD, and Supply Chain Foundations"]
  end
  subgraph SG_SEC [Security foundations]
    CRY01["CRY-01<br/>Cryptography Foundations"]
    IAM01["IAM-01<br/>Identity and Access Management Foundations"]
    DAT01["DAT-01<br/>Data and Database Security"]
  end
  NET01 --> CRY01
  PRG01 --> CRY01
  NET02 --> DAT01
  IAM01 --> DAT01
  PRG01 --> GIT01
  NET02 --> IAM01
  CRY01 --> IAM01
  SYS01 --> NET01
  NET01 --> NET02
  ORI01 --> ORI02
  ORI01 --> ORI03
  ORI01 --> PRG01
  SYS03 --> PRG02
  SYS04 --> PRG02
  ORI01 --> SYS01
  SYS01 --> SYS02
  SYS02 --> SYS03
  SYS02 --> SYS04
```

ORI-01 is the only true entry point; every other foundation module traces back to it.  
*External prerequisites for this slice:* None.

### Diagram 3: Application and product security chain

```mermaid
flowchart TD
  subgraph SG_BUILD [Design, build, and test]
    SEC01["SEC-01<br/>Secure Design Principles and Architecture"]
    APP01["APP-01<br/>Application Security Fundamentals"]
    WEB01["WEB-01<br/>Web Security Deep Dive"]
    API01["API-01<br/>API Security"]
    VUL01["VUL-01<br/>Vulnerability Management and Risk-Based Prioritization"]
  end
  subgraph SG_PROGRAM [Product security program]
    SCS01["SCS-01<br/>Software Supply Chain Security"]
    MOB01["MOB-01<br/>Mobile Security"]
    PDE01["PDE-01<br/>Product Security Engineering and SSDLC"]
    CAP02["CAP-02<br/>Application Security Program"]
  end
  WEB01 --> API01
  SEC01 --> APP01
  PDE01 --> CAP02
  API01 --> CAP02
  SCS01 --> CAP02
  APP01 --> MOB01
  APP01 --> PDE01
  SCS01 --> PDE01
  SEC01 --> PDE01
  APP01 --> SCS01
  SEC01 --> VUL01
  APP01 --> WEB01
```

This chain shows how design review, application testing, supply-chain assurance, and program management converge on the application-security capstone.  
*External prerequisites for this slice:* CNT-01, GIT-01, NET-01, NET-02, NET-03, ORI-02, PRG-01, SYS-02.

### Diagram 4: Binary exploitation and reverse-engineering chain

```mermaid
flowchart TD
  subgraph SG_LOW [Low-level foundations]
    SYS01["SYS-01<br/>Computer Architecture and Memory"]
    SYS02["SYS-02<br/>Operating Systems Internals"]
    PRG01["PRG-01<br/>Python for Security Engineering"]
  end
  subgraph SG_BIN [Exploitation and reverse engineering]
    EXP01["EXP-01<br/>Memory Safety and Exploit Mitigations"]
    EXP02["EXP-02<br/>Binary Exploitation"]
    REV01["REV-01<br/>Reverse Engineering Fundamentals"]
  end
  subgraph SG_SAMPLE [Malware and firmware]
    MAL01["MAL-01<br/>Malware Analysis in Isolated Labs"]
    HW01["HW-01<br/>Hardware and Firmware Security"]
  end
  SYS01 --> EXP01
  SYS02 --> EXP01
  PRG01 --> EXP01
  EXP01 --> EXP02
  SYS01 --> HW01
  REV01 --> HW01
  REV01 --> MAL01
  SYS01 --> REV01
  PRG01 --> REV01
  SYS01 --> SYS02
```

SYS-04 (Windows internals) and NET-01 are also required for MAL-01 but are omitted here to keep the chain readable; see Diagram 2.  
*External prerequisites for this slice:* NET-01, ORI-01, SYS-04.

### Diagram 5: Adversary emulation and control-validation chain

```mermaid
flowchart LR
  subgraph SG_ENTRY [Entry paths and methodology]
    APP01["APP-01<br/>Application Security Fundamentals"]
    WEB01["WEB-01<br/>Web Security Deep Dive"]
    API01["API-01<br/>API Security"]
    VUL01["VUL-01<br/>Vulnerability Management and Risk-Based Prioritization"]
    NET03["NET-03<br/>Network Security and Defenses"]
    OFF01["OFF-01<br/>Penetration Testing Methodology"]
  end
  subgraph SG_ADV [Adversary operations]
    AD01["AD-01<br/>Active Directory Attack and Defense"]
    TI01["TI-01<br/>Threat Intelligence"]
    LOG02["LOG-02<br/>Detection Engineering II and SIEM"]
    RED01["RED-01<br/>Red Team Operations and Adversary Emulation"]
    PUR01["PUR-01<br/>Purple Team and Control Validation"]
  end
  subgraph SG_CAP [Capstone]
    CAP03["CAP-03<br/>Adversary Emulation and Detection Research"]
  end
  NET03 --> AD01
  WEB01 --> API01
  RED01 --> CAP03
  PUR01 --> CAP03
  TI01 --> CAP03
  NET03 --> LOG02
  WEB01 --> OFF01
  NET03 --> OFF01
  VUL01 --> OFF01
  OFF01 --> PUR01
  LOG02 --> PUR01
  OFF01 --> RED01
  AD01 --> RED01
  TI01 --> RED01
  APP01 --> WEB01
```

RED-01 also requires EXP-01; PUR-01 deliberately depends on offensive methodology plus detection engineering rather than on full red-team operations.  
*External prerequisites for this slice:* CRY-01, EXP-01, LOG-01, NET-01, NET-02, PRG-01, SEC-01, SYS-04.

### Diagram 6: Detection and response chain

```mermaid
flowchart TD
  subgraph SG_SENSOR [Sensors and telemetry]
    SYS03["SYS-03<br/>Linux Administration and Hardening"]
    SYS04["SYS-04<br/>Windows Architecture, Registry, NTFS, and AD Preview"]
    NET01["NET-01<br/>Networking and TCP/IP"]
    NET03["NET-03<br/>Network Security and Defenses"]
  end
  subgraph SG_DETECT [Detection and response]
    LOG01["LOG-01<br/>Logging, Telemetry, and Detection Engineering I"]
    LOG02["LOG-02<br/>Detection Engineering II and SIEM"]
    IR01["IR-01<br/>Incident Response Foundations"]
    IR02["IR-02<br/>Incident Response and Crisis Management"]
    TI01["TI-01<br/>Threat Intelligence"]
  end
  subgraph SG_VALIDATE [Validation]
    OFF01["OFF-01<br/>Penetration Testing Methodology"]
    PUR01["PUR-01<br/>Purple Team and Control Validation"]
  end
  SYS03 --> LOG01
  SYS04 --> LOG01
  NET01 --> LOG01
  NET01 --> NET03
  NET03 --> LOG02
  LOG01 --> LOG02
  LOG01 --> IR01
  LOG01 --> TI01
  NET01 --> TI01
  IR01 --> IR02
  LOG02 --> IR02
  NET03 --> OFF01
  OFF01 --> PUR01
  LOG02 --> PUR01
```

This chain is the defensive counterpart to Diagram 5: telemetry is only useful if it is collected, normalized, detected, and validated. `END-01` is covered in the core and in the defensive path but is omitted here because it is not a prerequisite of `LOG-01`.  
*External prerequisites for this slice:* CRY-01, NET-02, SYS-01, SYS-02, VUL-01, WEB-01.

### Diagram 7: Forensics, malware, and case chain

```mermaid
flowchart TD
  subgraph SG_SOURCES [Evidence and sample sources]
    SYS03["SYS-03<br/>Linux Administration and Hardening"]
    SYS04["SYS-04<br/>Windows Architecture, Registry, NTFS, and AD Preview"]
    IR01["IR-01<br/>Incident Response Foundations"]
    REV01["REV-01<br/>Reverse Engineering Fundamentals"]
    NET03["NET-03<br/>Network Security and Defenses"]
  end
  subgraph SG_ANALYSIS [Forensic and malware analysis]
    FOR01["FOR-01<br/>Digital Forensics"]
    FOR02["FOR-02<br/>Advanced Forensics and Memory Analysis"]
    MAL01["MAL-01<br/>Malware Analysis in Isolated Labs"]
    MAL02["MAL-02<br/>Malware Research and Triage Automation"]
    ICS01["ICS-01<br/>OT/ICS Security"]
  end
  subgraph SG_CASE [Case integration]
    LOG02["LOG-02<br/>Detection Engineering II and SIEM"]
    IR02["IR-02<br/>Incident Response and Crisis Management"]
    CAP04["CAP-04<br/>Incident Response and Forensics Case"]
  end
  SYS03 --> FOR01
  SYS04 --> FOR01
  IR01 --> FOR01
  FOR01 --> FOR02
  REV01 --> FOR02
  REV01 --> MAL01
  MAL01 --> MAL02
  NET03 --> ICS01
  LOG02 --> IR02
  IR01 --> IR02
  IR02 --> CAP04
  FOR01 --> CAP04
  MAL01 --> CAP04
  LOG02 --> CAP04
```

This chain shows how evidence acquisition, reverse engineering, malware triage, and incident leadership converge on the defensive capstone.  
*External prerequisites for this slice:* CRY-01, NET-01, NET-02, SYS-01, SYS-02, VUL-01, WEB-01.

### Diagram 8: Cloud, container, and platform engineering chain

```mermaid
flowchart LR
  subgraph SG_FOUND [Identity and platform foundations]
    IAM01["IAM-01<br/>Identity and Access Management Foundations"]
    CLD01["CLD-01<br/>Cloud Security Foundations"]
    CNT01["CNT-01<br/>Container Security Foundations"]
  end
  subgraph SG_PLATFORM [Platform engineering]
    CLD02["CLD-02<br/>Cloud Security Engineering"]
    K8S01["K8S-01<br/>Kubernetes Security"]
    SRE01["SRE-01<br/>Security Reliability Engineering"]
  end
  subgraph SG_GOV [Architecture, governance, capstone]
    ARC01["ARC-01<br/>Security Architecture and Enterprise Engineering"]
    GOV01["GOV-01<br/>Governance, Compliance, and Audit"]
    CAP01["CAP-01<br/>Security Engineering Platform"]
  end
  CLD02 --> ARC01
  ARC01 --> CAP01
  SRE01 --> CAP01
  GOV01 --> CAP01
  IAM01 --> CLD01
  CLD01 --> CLD02
  IAM01 --> CLD02
  CNT01 --> K8S01
  CLD01 --> K8S01
  CLD02 --> SRE01
  K8S01 --> SRE01
```

NET-03 is an external prerequisite for the cloud foundations and is shown in Diagram 2 and Diagram 6.  
*External prerequisites for this slice:* CRY-01, GIT-01, LOG-02, NET-02, NET-03, RSK-01, SEC-01, SYS-03.

### Diagram 9: Data, cryptography, supply-chain, and privacy chain

```mermaid
flowchart LR
  subgraph SG_CRYPTO [Cryptography and identity]
    CRY01["CRY-01<br/>Cryptography Foundations"]
    CRY02["CRY-02<br/>Applied Cryptography Engineering"]
    IAM01["IAM-01<br/>Identity and Access Management Foundations"]
  end
  subgraph SG_DATA [Data, supply chain, and AI]
    DAT01["DAT-01<br/>Data and Database Security"]
    SCS01["SCS-01<br/>Software Supply Chain Security"]
    AI01["AI-01<br/>AI and LLM Security"]
  end
  subgraph SG_RISK [Risk, governance, and privacy]
    RSK01["RSK-01<br/>Risk Management and Security Governance"]
    GOV01["GOV-01<br/>Governance, Compliance, and Audit"]
    PRI01["PRI-01<br/>Privacy Engineering and Data Protection"]
  end
  CRY01 --> CRY02
  IAM01 --> DAT01
  RSK01 --> GOV01
  CRY01 --> IAM01
  GOV01 --> PRI01
  DAT01 --> PRI01
  CRY02 --> PRI01
```

DAT-01 requires IAM-01; PRI-01 requires GOV-01, DAT-01, and CRY-02, which is why the governance subgraph closes the chain.  
*External prerequisites for this slice:* APP-01, CLD-01, CNT-01, GIT-01, NET-01, NET-02, ORI-02, PRG-01.

### Diagram 10: Research and teaching strand

```mermaid
flowchart LR
  subgraph SG_METHOD [Method, ethics, and teaching]
    ORI03["ORI-03<br/>Technical Writing, Evidence, and Reproducibility"]
    SEC01["SEC-01<br/>Secure Design Principles and Architecture"]
    RSK01["RSK-01<br/>Risk Management and Security Governance"]
    RES01["RES-01<br/>Research Methods in Security"]
    RES06["RES-06<br/>Ethics, Disclosure, and Open Science"]
    TCH01["TCH-01<br/>Technical Teaching and Curriculum Design"]
  end
  subgraph SG_EMPIRICAL [Empirical, discovery, human, and formal methods]
    RES02["RES-02<br/>Empirical Security Measurement and Statistics"]
    RES03["RES-03<br/>Vulnerability Discovery Research"]
    RES04["RES-04<br/>Usable Security and Human Factors"]
    RES05["RES-05<br/>Formal Methods and Program Analysis"]
  end
  subgraph SG_THESIS [Synthesis and thesis]
    RES07["RES-07<br/>Thesis Proposal and Defense"]
    CAP05["CAP-05<br/>Research Thesis"]
  end
  RES07 --> CAP05
  ORI03 --> RES01
  RSK01 --> RES01
  RES01 --> RES02
  RES01 --> RES03
  RES01 --> RES04
  RES01 --> RES05
  RES01 --> RES06
  RES01 --> RES07
  RES02 --> RES07
  RES03 --> RES07
  RES04 --> RES07
  RES05 --> RES07
  RES06 --> RES07
  ORI03 --> TCH01
  SEC01 --> TCH01
```

Every technical module also contributes an evidence note or reproduction log to this strand, even when the module is not shown here.  
*External prerequisites for this slice:* CRY-02, DAT-01, NET-02, ORI-01, ORI-02, PRG-01, SYS-02, VUL-01.

## What the graph guarantees

- Every module except ORI-01 has at least one prerequisite.
- Every prerequisite exists in the manifest.
- The graph is acyclic.
- Each learning path in `LEARNING_PATHS.md` is closed under prerequisites.
- Capstones have explicit specialization prerequisites.

## What the graph does not guarantee

- **Readiness.** Passing a prerequisite is necessary, not sufficient; mastery gates still apply.
- **Scheduling.** The graph says what may follow what, not what must be taught concurrently.
- **Content quality.** A planned module is not an authored or validated module.
- **Tool stability.** Version-specific labs may need revision when tools change.

## Maintenance

1. Edit the manifest, not this file.
2. Regenerate the diagram blocks from the manifest.
3. Render the Markdown with the pinned Mermaid CLI.
4. Compare the rendered output and the manifest edge count.
5. Update the [graph metadata](#graph-metadata) table.

A diagram is a communication aid, not the specification. If a diagram is unreadable, split it; do not delete an edge to make it fit.
