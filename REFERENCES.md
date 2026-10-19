# References

> **Verification date:** 2026-10-19. **Scope:** architecture-level source grounding. This is not a complete bibliography for every future lesson.

## Table of contents

- [1. Verification levels](#1-verification-levels)
- [2. Source ledger](#2-source-ledger)
- [3. Source gaps and exclusions](#3-source-gaps-and-exclusions)
- [4. Citation style](#4-citation-style)
- [5. Refresh policy](#5-refresh-policy)
- [6. What verification does not mean](#6-what-verification-does-not-mean)

## 1. Verification levels

| Code | What was checked | What it does not mean |
|---|---|---|
| `V1` | Landing page fetched (HTTP 200); title, edition, and/or date matched the citation | The full document was read end to end |
| `V2` | DOI resolved through Crossref; title, authors, and year matched | The paper's claims were independently reproduced |
| `V3` | PDF fetched; file type validated; not fully read | The content or metadata was independently verified |
| `V4` | Publisher or catalogue page was bot-protected, blocked, or missing; bibliographic metadata was checked through a catalogue or standard designation | The link will work in automated checks, or the edition is current |
| `V5` | Project site was unavailable or unstable | The source should be used as a required citation |

Most standards were verified at the landing-page level. Module authoring must verify the specific clauses, versions, and claims used in a lesson.

## 2. Source ledger

Each source has a stable ID. Modules reference these IDs in the manifest and in lesson source lists. To see which modules use a source, search the manifest for the ID.

### Standards and government guidance

- **N01** — NIST, *The NIST Cybersecurity Framework (CSF) 2.0*. *CSWP 29, 2024-02-26*. [link](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final). `V1`
- **N02** — NIST, *Security and Privacy Controls for Information Systems and Organizations*. *SP 800-53 Rev. 5, incl. Update 1*. [link](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final). `V1`
- **N03** — NIST, *Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile*. *SP 800-61 Rev. 3, 2025-04-03*. [link](https://csrc.nist.gov/pubs/sp/800/61/r3/final). `V1`
- **N04** — NIST, *Digital Identity Guidelines*. *SP 800-63-4, 2025-07-31*. [link](https://csrc.nist.gov/pubs/sp/800/63/4/final). `V1`
- **N05** — NIST, *Zero Trust Architecture*. *SP 800-207*. [link](https://csrc.nist.gov/pubs/sp/800/207/final). `V1`
- **N06** — NIST, *Secure Software Development Framework (SSDF)*. *SP 800-218, Version 1.1*. [link](https://csrc.nist.gov/pubs/sp/800/218/final). `V1`
- **N07** — NIST, *Engineering Trustworthy Secure Systems*. *SP 800-160 Vol. 1 Rev. 1*. [link](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final). `V1`
- **N08** — NIST, *Risk Management Framework for Information Systems and Organizations*. *SP 800-37 Rev. 2*. [link](https://csrc.nist.gov/pubs/sp/800/37/r2/final). `V1`
- **N09** — NIST, *Guide for Conducting Risk Assessments*. *SP 800-30 Rev. 1*. [link](https://csrc.nist.gov/pubs/sp/800/30/r1/final). `V1`
- **N10** — NIST, *Guide to Computer Security Log Management*. *SP 800-92*. [link](https://csrc.nist.gov/pubs/sp/800/92/final). `V1`
- **N11** — NIST, *Technical Guide to Information Security Testing and Assessment*. *SP 800-115*. [link](https://csrc.nist.gov/pubs/sp/800/115/final). `V1`
- **N12** — NIST, *Application Container Security Guide*. *SP 800-190*. [link](https://csrc.nist.gov/pubs/sp/800/190/final). `V1`
- **N13** — NIST, *Guide to Operational Technology (OT) Security*. *SP 800-82 Rev. 3*. [link](https://csrc.nist.gov/pubs/sp/800/82/r3/final). `V1`
- **N14** — NIST, *Guide to Integrating Forensic Techniques into Incident Response*. *SP 800-86*. [link](https://csrc.nist.gov/pubs/sp/800/86/final). `V1` — Check for a revision at authoring time; the guide predates modern cloud and mobile environments.
- **N15** — NIST, *Ransomware Risk Management: A Cybersecurity Framework Profile*. *NIST IR 8374*. [link](https://csrc.nist.gov/pubs/ir/8374/final). `V1`
- **N16** — NIST, *Transition to Post-Quantum Cryptography Standards*. *NIST IR 8547, initial public draft, 2024-11-12*. [link](https://csrc.nist.gov/pubs/ir/8547/ipd). `V1` — Draft; do not treat timelines or requirements as final.
- **N17** — NIST, *Recommendations for Key-Encapsulation Mechanisms*. *SP 800-227, initial public draft*. [link](https://csrc.nist.gov/pubs/sp/800/227/ipd). `V1` — Draft; page updated during 2025. Re-check status before citing.
- **N18** — NIST, *Module-Lattice-Based Key-Encapsulation Mechanism Standard*. *FIPS 203, 2024-08-13*. [link](https://csrc.nist.gov/pubs/fips/203/final). `V1`
- **N19** — NIST, *Module-Lattice-Based Digital Signature Standard*. *FIPS 204, 2024-08-13*. [link](https://csrc.nist.gov/pubs/fips/204/final). `V1`
- **N20** — NIST, *Stateless Hash-Based Digital Signature Standard*. *FIPS 205, 2024-08-13*. [link](https://csrc.nist.gov/pubs/fips/205/final). `V1`
- **N21** — NIST, *AI Risk Management Framework 1.0*; *Generative AI Profile*. *AI RMF 1.0, 2023-01-26; NIST AI 600-1, 2024-07*. [link](https://www.nist.gov/itl/ai-risk-management-framework). `V1` — The AI RMF page states that version 1.0 is being revised; check status before relying on it.
- **N22** — NIST, *Privacy Framework*. *Version 1.0; Version 1.1 initial public draft*. [link](https://www.nist.gov/privacy-framework). `V1` — 1.1 was an initial public draft at verification time; do not present it as final.
- **N23** — NIST, *Workforce Framework for Cybersecurity (NICE Framework)*. *SP 800-181 Rev. 1, 2020-11-16*. [link](https://csrc.nist.gov/pubs/sp/800/181/r1/final). `V1`
- **N24** — NIST, *Information Security Continuous Monitoring (ISCM) for Federal Information Systems and Organizations*. *SP 800-137*. [link](https://csrc.nist.gov/pubs/sp/800/137/final). `V1`
- **N25** — NIST, *Guidelines on Firewalls and Firewall Policy*. *SP 800-41 Rev. 1*. [link](https://csrc.nist.gov/pubs/sp/800/41/r1/final). `V1`
- **N26** — NIST, *Guide to Intrusion Detection and Prevention Systems (IDPS)*. *SP 800-94*. [link](https://csrc.nist.gov/pubs/sp/800/94/final). `V1`
- **N27** — NIST, *Guide to Malware Incident Prevention and Handling*. *SP 800-83, 2013-07-22*. [link](https://csrc.nist.gov/pubs/sp/800/83/final). `V1` — Dated relative to modern malware; pair with current ATT&CK and vendor documentation.
- **N28** — NIST, *Guidelines on Mobile Device Forensics*. *SP 800-101 Rev. 1, 2014*. [link](https://doi.org/10.6028/NIST.SP.800-101r1). `V1` — DOI resolves to the NIST PDF; link checked 2026-10-19.
- **N29** — NIST, *Guide to Cyber Threat Information Sharing*. *SP 800-150*. [link](https://csrc.nist.gov/pubs/sp/800/150/final). `V1`
- **N30** — NIST, *Guidelines on Security and Privacy in Public Cloud Computing*. *SP 800-144*. [link](https://csrc.nist.gov/pubs/sp/800/144/final). `V1`
- **N31** — NIST, *The NIST Definition of Cloud Computing*. *SP 800-145*. [link](https://csrc.nist.gov/pubs/sp/800/145/final). `V1`
- **N32** — NIST, *Platform Firmware Resiliency Guidelines*. *SP 800-193*. [link](https://csrc.nist.gov/pubs/sp/800/193/final). `V1`
- **N33** — NIST, *A Zero Trust Architecture Model for Access Control in Cloud-Native Applications in Multi-Cloud Environments*. *SP 800-207A*. [link](https://csrc.nist.gov/pubs/sp/800/207/a/final). `V1`
- **N34** — NIST, *Guide to Data-Centric System Threat Modeling*. *SP 800-154, initial public draft, 2016-04-15*. [link](https://csrc.nist.gov/pubs/sp/800/154/ipd). `V1` — Draft and old; use as a historical method, not current normative guidance.
- **N35** — NIST, *Guide to General Server Security*. *SP 800-123*. [link](https://csrc.nist.gov/pubs/sp/800/123/final). `V1` — Dated; pair with current CIS benchmarks and vendor hardening guides.
- **N36** — NIST, *Recommendation for Key Management: Part 1 – General*. *SP 800-57 Part 1 Rev. 5*. [link](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final). `V1`
- **I01** — ISO/IEC, *Information security, cybersecurity and privacy protection — Information security management systems — Requirements*. *ISO/IEC 27001:2022*. [link](https://www.iso.org/standard/27001). `V4` — Automated access returned HTTP 403; edition recorded from the standard designation. Verify in a browser or through a licensed copy.

### OWASP and community standards

- **O01** — OWASP, *OWASP Top 10:2025*. *2025 edition*. [link](https://owasp.org/Top10/2025/). `V1`
- **O02** — OWASP, *Application Security Verification Standard (ASVS)*. *5.0.0, released 2025-05-30*. [link](https://owasp.org/www-project-application-security-verification-standard/). `V1` — Version verified from the project release metadata.
- **O03** — OWASP, *Web Security Testing Guide (WSTG)*. *v4.2, released 2020-12-03*. [link](https://github.com/OWASP/wstg/releases/tag/v4.2). `V1` — A 2023 prerelease exists but is not treated as the stable edition here.
- **O04** — OWASP, *API Security Top 10*. *2023 edition*. [link](https://owasp.org/API-Security/editions/2023/en/0x00-header/). `V1`
- **O05** — OWASP, *Top 10 for LLM Applications*. *2025 edition*. [link](https://genai.owasp.org/llm-top-10/). `V1`
- **O06** — OWASP, *Software Assurance Maturity Model (SAMM)*. *Version 2*. [link](https://owasp.org/www-project-samm/). `V1`
- **O07** — OWASP, *Mobile Application Security Verification Standard (MASVS)* and *Mobile Top 10*. *MASVS 2.1.0 (2024-01-18); Mobile Top 10 2024*. [link](https://mas.owasp.org/MASVS/). `V1` — Version verified from the MASVS release metadata; Mobile Top 10 2024 is a separate project.
- **O08** — OWASP, *Threat Modeling Cheat Sheet*. *Living document*. [link](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html). `V1` — Living document; record the access date when citing.
- **O09** — OWASP, *SQL Injection Prevention Cheat Sheet*. *Living document*. [link](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html). `V1` — Living document; record the access date when citing.
- **O10** — OWASP, *Docker Top 10*. *Project page*. [link](https://owasp.org/www-project-docker-top-10/). `V1`

### MITRE knowledge bases

- **M01** — MITRE, *ATT&CK*. *Version 20.0, released 2026-10-13*. [link](https://attack.mitre.org/). `V1` — Version verified from the official STIX release metadata: <https://github.com/mitre-attack/attack-stix-data/releases/tag/v20.0>
- **M02** — MITRE, *D3FEND*. *Matrix*. [link](https://d3fend.mitre.org/). `V1`
- **M03** — MITRE, *ATLAS*. *Knowledge base*. [link](https://atlas.mitre.org/). `V1`

### Vulnerability, risk, and disclosure data

- **C01** — FIRST, *Common Vulnerability Scoring System v4.0*. *CVSS v4.0*. [link](https://www.first.org/cvss/v4-0/). `V1`
- **C02** — FIRST, *Exploit Prediction Scoring System (EPSS)*. *Project page*. [link](https://www.first.org/epss/). `V1` — EPSS is model- and data-dependent; record the model version and date when using scores.
- **C03** — CISA, *Known Exploited Vulnerabilities Catalog*. *Living catalog*. [link](https://www.cisa.gov/known-exploited-vulnerabilities-catalog). `V1` — Living data; record the retrieval date.
- **C04** — CISA, *Software Bill of Materials (SBOM)*. *Program page*. [link](https://www.cisa.gov/sbom). `V1`
- **C05** — Center for Internet Security, *CIS Critical Security Controls*. *Version 8.1*. [link](https://www.cisecurity.org/controls/v8-1). `V1`
- **C06** — CISA, *Coordinated Vulnerability Disclosure (CVD) Program*. *Program page*. [link](https://www.cisa.gov/coordinated-vulnerability-disclosure-process). `V1`

### Protocols and supply-chain specifications

- **P01** — SLSA, *Supply-chain Levels for Software Artifacts*. *Version 1.2*. [link](https://slsa.dev/spec/v1.2/). `V1` — The v1.0 page states that v1.2 is current; v1.0 is retired.
- **P02** — Sigstore. *Project site*. [link](https://www.sigstore.dev/). `V1`
- **P03** — in-toto. *Project site*. [link](https://in-toto.io/). `V1`
- **P04** — Open Source Security Foundation (OpenSSF). *Project site*. [link](https://openssf.org/). `V1`
- **P05** — IETF, *The Transport Layer Security (TLS) Protocol Version 1.3*. *RFC 8446*. [link](https://www.rfc-editor.org/rfc/rfc8446). `V1`
- **P06** — IETF, *HTTP Semantics*. *RFC 9110*. [link](https://www.rfc-editor.org/rfc/rfc9110). `V1`
- **P07** — IETF, *Domain names — concepts and facilities*. *RFC 1034*. [link](https://www.rfc-editor.org/rfc/rfc1034). `V1`
- **P08** — IETF, *Transmission Control Protocol (TCP)*. *RFC 9293*. [link](https://www.rfc-editor.org/rfc/rfc9293). `V1`
- **P09** — IETF, *The OAuth 2.0 Authorization Framework*. *RFC 6749*. [link](https://www.rfc-editor.org/rfc/rfc6749). `V1`
- **P10** — IETF, *Best Current Practice for OAuth 2.0 Security*. *RFC 9700*. [link](https://www.rfc-editor.org/rfc/rfc9700). `V1`
- **P11** — IETF, *HTTP State Management Mechanism*. *RFC 6265*. [link](https://www.rfc-editor.org/rfc/rfc6265). `V1`
- **P12** — IETF, *The Web Origin Concept*. *RFC 6454*. [link](https://www.rfc-editor.org/rfc/rfc6454). `V1`

### Tool and project documentation

- **T01** — Sigma, *SIEM detection format*. *Project site*. [link](https://sigmahq.io/). `V1`
- **T02** — YARA, *Documentation*. *Version 4.5.0 at verification*. [link](https://yara.readthedocs.io/). `V1`
- **T03** — AFL++. *GitHub repository*. [link](https://github.com/AFLplusplus/AFLplusplus). `V1`
- **T05** — KLEE. *Project site*. [link](https://klee.github.io/). `V1`
- **T06** — TLA+. *Lamport's TLA+ page*. [link](https://lamport.azurewebsites.net/tla/tla.html). `V1`
- **T07** — Volatility 3, *Documentation*. *Version 2.28.2 at verification*. [link](https://volatility3.readthedocs.io/). `V1`
- **T08** — Ghidra. *GitHub repository*. [link](https://ghidra-sre.org/). `V1`
- **T09** — Microsoft, *Sysmon*. *Sysinternals documentation*. [link](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon). `V1`
- **T10** — Kubernetes, *Security*. *Official documentation*. [link](https://kubernetes.io/docs/concepts/security/). `V1`
- **T11** — Center for Internet Security, *Kubernetes Benchmark*. *Benchmark page*. [link](https://www.cisecurity.org/benchmark/kubernetes). `V1`

### Academic literature

- **A01** — Saltzer, J. H., and Schroeder, M. D., *The Protection of Information in Computer Systems*. *1975*. [link](https://doi.org/10.1109/PROC.1975.9939). `V2`
- **A07** — Shacham, H., *The Geometry of Innocent Flesh on the Bone: Return-into-libc without Function Calls (on the x86)*. *2007*. [link](https://doi.org/10.1145/1315245.1315313). `V2`
- **A08** — Szekeres, L., Payer, M., Wei, T., and Song, D., *SoK: Eternal War in Memory*. *2013*. [link](https://doi.org/10.1109/SP.2013.13). `V2`
- **A09** — Abadi, M., Budiu, M., Erlingsson, Ú., and Ligatti, J., *Control-Flow Integrity*. *2005*. [link](https://doi.org/10.1145/1102120.1102165). `V2`
- **A10** — Kocher, P., et al., *Spectre Attacks: Exploiting Speculative Execution*. *2019*. [link](https://doi.org/10.1109/SP.2019.00002). `V2`
- **A13** — Adams, A., and Sasse, M. A., *Users are not the enemy*. *1999*. [link](https://doi.org/10.1145/322796.322806). `V2`
- **A15** — Herley, C., *So long, and no thanks for the externalities: the rational rejection of security advice by users*. *2009*. [link](https://doi.org/10.1145/1719030.1719050). `V2`
- **A16** — Dwork, C., and Roth, A., *The Algorithmic Foundations of Differential Privacy*. *2013*. [link](https://doi.org/10.1561/9781601988195). `V2`
- **A17** — Manes, V. J. M., et al., *The Art, Science, and Engineering of Fuzzing: A Survey*. *2021*. [link](https://doi.org/10.1109/TSE.2019.2946563). `V2`
- **A18** — Bailey, M., Dittrich, D., and Kenneally, E., *The Menlo Report*. *2012*. [link](https://doi.org/10.1109/MSP.2012.52). `V2`
- **A19** — ACM/IEEE-CS/AAAI, *Computer Science Curricula 2023 (CS2023)*. *2023*. [link](https://csed.acm.org/). `V1`
- **A20** — Thompson, K., *Reflections on Trusting Trust*. *1984*. [link](https://doi.org/10.1145/358198.358210). `V2`

### Books

- **B01** — Anderson, R., *Security Engineering: A Guide to Building Dependable Distributed Systems*. *3rd edition, 2020; free online*. [link](https://www.cl.cam.ac.uk/~rja14/book.html). `V1`
- **B02** — Boneh, D., and Shoup, V., *A Graduate Course in Applied Cryptography*. *Online edition; PDF verified*. [link](https://toc.cryptobook.us/). `V3` — Free online book; version changes over time. Record the access date.
- **B03** — Shostack, A., *Threat Modeling: Designing for Security*. *2014*. [link](https://www.wiley.com/en-us/Threat+Modeling%3A+Designing+for+Security-p-9781118809990). `V1`
- **B04** — Aumasson, J.-P., *Serious Cryptography*. *2nd edition*. [link](https://nostarch.com/seriouscrypto). `V1`
- **B05** — Ferguson, N., Schneier, B., and Kohno, T., *Cryptography Engineering: Design Principles and Practical Applications*. *2010*. [link](https://www.wiley.com/en-us/Cryptography+Engineering%3A+Design+Principles+and+Practical+Applications-p-9780470474242). `V1`
- **B06** — Andriesse, D., *Practical Binary Analysis*. *2018*. [link](https://openlibrary.org/works/OL20171035W). `V4` — Publisher page was bot-protected; metadata checked through Open Library search; the work page may require a browser.
- **B07** — Sikorski, M., and Honig, A., *Practical Malware Analysis*. *2012*. [link](https://openlibrary.org/works/OL16509463W). `V4` — Publisher page returned 404; metadata checked through Open Library search; the work page may require a browser.
- **B08** — Ligh, M. H., Case, A., Levy, J., and Walters, A., *The Art of Memory Forensics*. *Wiley*. [link](https://www.wiley.com/en-us/The+Art+of+Memory+Forensics%3A+Detecting+Malware+and+Threats+in+Windows+Memory-p-9781118825099). `V1`
- **B09** — Russinovich, M., Solomon, D., and Ionescu, A., *Windows Internals*. *7th edition, Part 1*. [link](https://learn.microsoft.com/en-us/sysinternals/resources/windows-internals). `V1` — Part 2 covers additional subsystems; check the current edition before citing page numbers.
- **B10** — Rice, L., *Container Security*. *2020*. [link](https://openlibrary.org/works/OL21882743W). `V4` — Publisher page returned HTTP 403; metadata checked through Open Library search; the work page may require a browser.
- **B11** — Zalewski, M., *The Tangled Web: A Guide to Securing Modern Web Applications*. *2011*. [link](https://openlibrary.org/works/OL16215318W). `V4` — Publisher page returned HTTP 403; metadata checked through Open Library search; the work page may require a browser.
- **B12** — Dowd, M., McDonald, J., and Schuh, J., *The Art of Software Security Assessment*. *Addison-Wesley*. no stable link. `V4` — Bibliographic entry only; no stable publisher page or publication year was machine-verified.
- **B13** — Dang, B., Gazet, A., and Bachaalany, E., *Practical Reverse Engineering*. *2014*. [link](https://openlibrary.org/works/OL19978523W). `V4` — Publisher page was not verified; metadata checked through Open Library search; the work page may require a browser.
- **B14** — Sanders, C., and Smith, J., *Applied Network Security Monitoring*. *2014*. [link](https://openlibrary.org/works/OL17432132W). `V4` — Publisher page was not verified; metadata checked through Open Library search; the work page may require a browser.
- **B15** — Beyer, B., et al., *Site Reliability Engineering*. *Free online edition*. [link](https://sre.google/sre-book/table-of-contents/). `V1`
- **B16** — Adkins, H., et al., *Building Secure and Reliable Systems*. *2020; free online*. [link](https://sre.google/books/building-secure-reliable-systems/). `V1`

### Systems and platform documentation

- **L01** — Linux man-pages project, *syscalls(2)*. [link](https://man7.org/linux/man-pages/man2/syscalls.2.html). `V1`
- **L02** — Linux man-pages project, *seccomp(2)*. [link](https://man7.org/linux/man-pages/man2/seccomp.2.html). `V1`
- **L03** — Linux man-pages project, *capabilities(7)*. [link](https://man7.org/linux/man-pages/man7/capabilities.7.html). `V1`
- **L04** — Linux man-pages project, *namespaces(7)*. [link](https://man7.org/linux/man-pages/man7/namespaces.7.html). `V1`
- **L05** — Linux man-pages project, *cgroups(7)*. [link](https://man7.org/linux/man-pages/man7/cgroups.7.html). `V1`
- **L06** — Linux man-pages project, *inode(7)*. [link](https://man7.org/linux/man-pages/man7/inode.7.html). `V1`
- **L07** — Linux man-pages project, *credentials(7)*. [link](https://man7.org/linux/man-pages/man7/credentials.7.html). `V1`
- **L08** — Linux man-pages project, *ptrace(2)*. [link](https://man7.org/linux/man-pages/man2/ptrace.2.html). `V1`
- **L09** — Linux man-pages project, *elf(5)*. [link](https://man7.org/linux/man-pages/man5/elf.5.html). `V1`
- **L10** — x86-64 psABI, *System V Application Binary Interface: AMD64 Architecture Processor Supplement*. [link](https://gitlab.com/x86-psABIs/x86-64-ABI). `V1`
- **L11** — Arm, *Arm Architecture Reference Manual for A-profile architecture* (DDI 0487). [link](https://developer.arm.com/documentation/ddi0487/latest/). `V4` — automated access returned HTTP 403; edition and register/exception-level content were not machine-verified in this milestone.
- **L12** — Intel, *Intel 64 and IA-32 Architectures Software Developer's Manual*. [link](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html). `V4` — automated access returned HTTP 403; verify the current volume and revision in a browser.
- **L13** — The Open Group, *POSIX.1-2024 (IEEE Std 1003.1-2024)*. [link](https://pubs.opengroup.org/onlinepubs/9799919799/). `V1`
- **L14** — Microsoft, *Access Control (Windows security)*. [link](https://learn.microsoft.com/en-us/windows/win32/secauthz/access-control). `V1`
- **L15** — Microsoft, *Processes and Threads*. [link](https://learn.microsoft.com/en-us/windows/win32/procthread/processes-and-threads). `V1`
- **L16** — Microsoft, *Memory Management (Windows)*. [link](https://learn.microsoft.com/en-us/windows/win32/memory/memory-management). `V1`
- **L17** — Microsoft, *PE Format*. [link](https://learn.microsoft.com/en-us/windows/win32/debug/pe-format). `V1`
- **L18** — Linux kernel documentation, *Seccomp BPF (SECure COMPuting with filters)*. [link](https://www.kernel.org/doc/html/latest/userspace-api/seccomp_filter.html). `V1`
- **L19** — Linux kernel documentation, *Control Group v2*. [link](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html). `V1`
- **L20** — Clang documentation, *Control Flow Integrity*. [link](https://clang.llvm.org/docs/ControlFlowIntegrity.html). `V1`
- **L21** — Microsoft, *Mandatory Integrity Control*. [link](https://learn.microsoft.com/en-us/windows/win32/secauthz/mandatory-integrity-control). `V1`
- **L22** — Microsoft, *Job Objects*. [link](https://learn.microsoft.com/en-us/windows/win32/procthread/job-objects). `V1`
- **L23** — Apple, *App Sandbox*. [link](https://developer.apple.com/documentation/security/app_sandbox). `V1`
- **L25** — Linux man-pages project, *proc(5)*. [link](https://man7.org/linux/man-pages/man5/proc.5.html). `V1`
- **L26** — Linux man-pages project, *mount_namespaces(7)*. [link](https://man7.org/linux/man-pages/man7/mount_namespaces.7.html). `V1`
- **L27** — Linux man-pages project, *pid_namespaces(7)*. [link](https://man7.org/linux/man-pages/man7/pid_namespaces.7.html). `V1`
- **L28** — Linux man-pages project, *clone(2)*. [link](https://man7.org/linux/man-pages/man2/clone.2.html). `V1`

### Research methods and scientific practice

- **R01** — Page, M. J., McKenzie, J. E., Bossuyt, P. M., et al., *The PRISMA 2020 statement: an updated guideline for reporting systematic reviews*. *2021*. [link](https://doi.org/10.1136/bmj.n71). `V2`
- **R02** — Wohlin, C., Runeson, P., Höst, M., Ohlsson, M. C., Regnell, B., and Wesslén, A., *Experimentation in Software Engineering*. *2012*. [link](https://doi.org/10.1007/978-3-642-29044-2). `V2`
- **R03** — Ralph, P., et al., *Empirical Standards for Software Engineering Research*. *2020*. [link](https://arxiv.org/abs/2010.03525). `V1` — preprint; check for a peer-reviewed version before citing as established guidance.
- **R04** — National Academies of Sciences, Engineering, and Medicine, *Reproducibility and Replicability in Science*. *2019*. [link](https://doi.org/10.17226/25303). `V2`
- **R05** — Sandve, G. K., Nekrutenko, A., Taylor, J., and Hovig, E., *Ten Simple Rules for Reproducible Computational Research*. *2013*. [link](https://doi.org/10.1371/journal.pcbi.1003285). `V2`
- **R06** — Munafò, M. R., Nosek, B. A., Bishop, D. V. M., et al., *A manifesto for reproducible science*. *2017*. [link](https://doi.org/10.1038/s41562-016-0021). `V2`
- **R07** — Greenland, S., Senn, S. J., Rothman, K. J., et al., *Statistical tests, P values, confidence intervals, and power: a guide to misinterpretations*. *2016*. [link](https://doi.org/10.1007/s10654-016-0149-3). `V2`
- **R08** — Ioannidis, J. P. A., *Why Most Published Research Findings Are False*. *2005*. [link](https://doi.org/10.1371/journal.pmed.0020124). `V2`
- **R09** — Wasserstein, R. L., and Lazar, N. A., *The ASA Statement on p-Values: Context, Process, and Purpose*. *2016*. [link](https://doi.org/10.1080/00031305.2016.1154108). `V2`
- **R10** — Software Engineering Institute, Carnegie Mellon University, *CERT Guide to Coordinated Vulnerability Disclosure*. [link](https://www.sei.cmu.edu/library/cert-guide-to-coordinated-vulnerability-disclosure/). `V1`
- **R11** — ISO/IEC, *Information technology — Security techniques — Vulnerability disclosure*. *ISO/IEC 29147:2018*. [link](https://www.iso.org/standard/72311.html). `V4` — automated access returned HTTP 403; verify the edition in a browser or licensed copy.
- **R12** — NIST/SEMATECH, *e-Handbook of Statistical Methods*. [link](https://www.itl.nist.gov/div898/handbook/). `V1`
- **R13** — ACM, *Artifact Review and Badging*. [link](https://www.acm.org/publications/policies/artifact-review-and-badging-current). `V4` — automated access returned HTTP 403; verify in a browser.
- **R14** — ACM, *Publications Policies*. [link](https://www.acm.org/publications/policies). `V4` — automated access returned HTTP 403; verify in a browser.
- **R15** — U.S. Department of Health and Human Services, *The Belmont Report*. *1979*. [link](https://www.hhs.gov/ohrp/regulations-and-policy/belmont-report/index.html). `V4` — automated access returned HTTP 403; verify in a browser.

### Legacy and unstable sources

- **U01** — Penetration Testing Execution Standard (PTES). *Legacy community methodology*. [link](https://github.com/penetration-testing-execution-standard/ptes). `V5` — The project website was unreachable on 2026-10-19, and the GitHub repository is an automation framework rather than the full standard text. Use NIST SP 800-115 and OWASP WSTG as primary methodology sources; keep PTES only as historical context.

## 3. Source gaps and exclusions

These sources were considered but are **not** in the required ledger yet. Do not cite them as if they were verified.

| Source | Issue found on 2026-10-19 | Interim guidance |
|---|---|---|
| NSA/CISA, *Kubernetes Hardening Guidance* v1.2 (2022) | The CISA landing page returned HTTP 404 and the defense.gov PDF returned HTTP 403 | Use the official Kubernetes security documentation (`T10`) and the CIS Kubernetes Benchmark (`T11`) until a stable URL is found |
| ACM, *Artifact Review and Badging* | The policy page returned HTTP 403 to the automated client | Use the CS2023 curriculum (`A19`) and the Menlo Report (`A18`) for research and artifact guidance; re-check the ACM page in a browser |
| ISO/IEC 27001:2022 | The ISO catalogue page returned HTTP 403 to the automated client | The edition is recorded from the standard designation (`I01`); verify in a browser or licensed copy |
| O'Reilly books | O'Reilly pages returned HTTP 403 | Bibliographic metadata is recorded through Open Library or the publisher where available |
| PTES | The project website was unreachable; the GitHub repository is not the full standard text | Use `N11` and `O03` as primary methodology sources; keep `U01` as legacy context only |
| NIST SP 800-154 | Initial public draft from 2016 | Use as a historical threat-modeling method (`N34`), not current normative guidance |
| NIST SP 800-227 | Initial public draft; page updated during 2025 | Re-check final status before citing requirements (`N17`) |
| NIST IR 8547 | Initial public draft | Treat migration timelines as proposals, not commitments (`N16`) |
| NIST SP 800-86 | Older guide; page does not indicate a current revision | Pair with current forensic tooling documentation and record limitations (`N14`) |

### Source quality rules

1. **Primary over secondary.** Standards, RFCs, official documentation, and peer-reviewed papers come first.
2. **Living documents need dates.** OWASP cheat sheets, ATT&CK, KEV, EPSS, and vendor docs change; record the access date and model/version.
3. **Vendor claims are not benchmarks.** A vendor's performance or detection claim must be labeled as a vendor claim unless independently verified.
4. **AI output is not a source.** It may help locate a source, but the source itself must be read and cited.
5. **Broken links are findings.** A 404 or 403 is recorded, not hidden. Replace the source or document the limitation.

## 4. Citation style

- In manifest `sources` lists and module source sections, use the bracketed ID: `[N03]`, `[O02]`, `[A18]`.
- In prose, use a readable citation plus the ID: "NIST SP 800-61r3 [N03]".
- For living sources, add the access date: "ATT&CK v20.0 [M01], accessed 2026-10-19".
- For books, include the edition when the content differs across editions.
- Never cite a source you have not opened. A catalogue record verifies existence, not content.

## 5. Refresh policy

| Cadence | Action |
|---|---|
| Every 6 months | Re-check standards editions, RFC status, tool versions, and links; update the ledger and manifest |
| On major release | ATT&CK, OWASP Top 10, ASVS, CVSS, SLSA, NIST CSF, or a primary cloud provider's security model |
| On broken link | Record the failure, find a stable replacement, or mark the source `V5` |
| Before publishing a module | Verify every claim that depends on a version, default, or tool capability |
| After a learner report | Check whether the source changed or the lesson misread it |

Ownership: the curriculum maintainer owns the ledger; module authors propose additions with a verification note and the specific claims the source supports.

## 6. What verification does not mean

- It does not mean the source is correct, current, or applicable to the learner's jurisdiction.
- It does not mean the curriculum has reproduced the source's results.
- It does not mean a standard's draft is final.
- It does not mean a tool behaves as documented in every environment.
- It does not transfer liability or authorization to the learner.

The ledger is a record of diligence, not a guarantee.
