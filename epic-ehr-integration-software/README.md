# Integrating Software Applications with the Epic Electronic Health Record System

An interactive HTML roadmap for software engineers building applications that integrate with Epic EHR — from foundational interoperability concepts through advanced API patterns, App Orchard distribution, clinical workflow embedding, and production operations.

## How to Use

1. **Open `roadmap.html` in any modern browser** (Chrome, Firefox, Safari, Edge)
2. Browse topics organized in 6 progressive sections
3. Click any topic to view details, resources, and prerequisites
4. Check off topics as you complete them to track progress
5. Use search and difficulty filters to find specific topics
6. Follow prerequisite links to navigate the learning path

No internet connection required (except for Google Fonts, which degrades gracefully to system fonts).

## Statistics

| Metric | Value |
|--------|-------|
| Total Topics | 65 |
| Total Resources | 196 |
| Total Edges (Prerequisites) | 86 |
| Sections | 6 |
| Milestones | 9 |
| Estimated Total Hours | ~480 |
| Difficulty Levels | Beginner → Intermediate → Advanced → Expert |

## Sections

1. **Healthcare Foundations** (9 topics, ~65h) — EHR concepts, HIPAA, Cures Act, FDA SaMD, clinical terminology
2. **Core Standards and Security** (11 topics, ~85h) — FHIR R4, US Core, OAuth 2.0, SMART authorization, JWT/JWKS
3. **Application Development and Interfaces** (10 topics, ~95h) — SMART on FHIR apps, HL7v2 interfaces, integration engines
4. **Advanced Integration Patterns** (17 topics, ~110h) — CDS Hooks, MyChart, Bulk FHIR, clinical workflow embedding
5. **Distribution and Operations** (13 topics, ~85h) — Epic Showroom, SOC 2, go-live, observability, incident response
6. **Architecture and Mastery** (5 topics, ~40h) — Integration surface selection, hybrid patterns, reference architectures

## Package Contents

| File | Description |
|------|-------------|
| `roadmap.html` | Interactive HTML roadmap (self-contained, ~140KB) |
| `README.md` | This file |
| `architecture/roadmap-final.json` | Structured roadmap data (65 nodes, 86 edges, 196 resources) |
| `architecture/layout-spec.md` | Visual layout specification |

## Target Audience

Fullstack software engineers and technical leads (2-8 years experience) building applications that integrate with Epic. Assumes proficiency in web development and REST APIs, but no prior experience with Epic, FHIR, HL7, or healthcare interoperability.

## Credits

- Generated on 2026-03-19
- Data sources: Epic official documentation (open.epic.com, fhir.epic.com), HL7 FHIR specification, SMART Health IT, ONC, HHS, and community resources
- Built with the Topic Mastery Roadmap workflow (OpenClaw)
