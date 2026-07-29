# Application Mentor V1.0

Application Mentor is an AI-agent skill for reviewing a student's own grant,
scholarship, internship, exchange, and university application documents. It
looks at a draft from a selection committee's perspective and identifies the
specific places where it becomes generic, unsupported, inconsistent, or
non-compliant with the target program.

## What it reviews

- CVs and resumes
- motivation letters and cover letters
- personal statements and application essays
- recommendation letters
- study plans and research proposals
- application and interview answers
- Uzbek scholarship documents, including tavsiyanoma, tavsifnoma,
  taqriznoma, and obyektivka
- the basic legitimacy of fee-charging programs

## Core principles

- Check word limits, required sections, format, dates, signatures, and
  attachments before reviewing style.
- Tie feedback to the target program and to exact lines from the student's
  document.
- Turn unsupported claims into evidence-based statements.
- Preserve the student's voice.
- Never invent achievements, scores, dates, names, or numerical results.
- Use `[YOZING: ...]` placeholders when essential facts are missing.
- Do not generate a complete submission-ready application the student did not
  write.

## Structure

```text
application-mentor/
├── SKILL.md
├── references/
│   ├── application-questions.md
│   ├── cv-and-resume.md
│   ├── motivation-and-cover-letters.md
│   ├── personal-statement-and-essays.md
│   ├── programs-and-requirements.md
│   ├── prose-and-authenticity.md
│   ├── recommendation-letters.md
│   ├── study-plans-and-research.md
│   └── uzbek-scholarship-documents.md
└── scripts/
    └── read_document.py
```

## Installation in Claude Code

Place the `application-mentor` directory in the Claude Code skills directory:

```bash
mkdir -p ~/.claude/skills
cp -R application-mentor ~/.claude/skills/
```

Start a new conversation after installation so Claude Code can discover the
skill.

Example request:

```text
Motivatsion xatimni ko'rib bering. DAAD dasturiga topshiryapman,
500 so'z limit bor.
```

## Document helper

The bundled script extracts text and useful statistics from supported
application documents:

```bash
python3 scripts/read_document.py "path/to/document.docx"
python3 scripts/read_document.py "path/to/document.docx" --stats-only
```

It uses macOS `textutil` for `.docx`, `.doc`, `.rtf`, and related formats.
`.pptx`, `.xlsx`, `.txt`, and `.md` processing uses Python's standard library.
Review PDFs directly in the host AI tool because layout is important for CVs
and other formatted documents.

## Licence — non-commercial use only

Required Notice: Copyright 2026 Feruzbek Baqoyev

This project is made publicly available under the
[PolyForm Noncommercial License 1.0.0](https://polyformproject.org/licenses/noncommercial/1.0.0.txt).
By using, modifying, or distributing it, you agree to the complete licence
terms at that link.

**Do not use this skill, its instructions, references, or script as a
commercial component.** Without separate written permission from the copyright
holder, you may not sell it, resell it, include it in a paid product or
subscription, integrate it into a commercial service or SaaS product, or use
it as part of a paid admissions, consulting, or training offering.

Personal study, research, experimentation, and qualifying use by educational,
charitable, public-research, public-health, environmental, and government
institutions are permitted as described in the licence.

Because commercial use is restricted, this is technically a
**source-available project rather than OSI-approved open-source software**.
OSI-approved open-source licences must permit commercial use.

## Privacy and accuracy

- Do not publish student applications or personal data in public issues.
- Use fictional or fully anonymized examples when reporting a problem.
- Deadlines, fees, stipend amounts, GPA thresholds, visa rules, rankings, and
  program requirements change. Verify them on the current official page.
- This project is not affiliated with any university, scholarship,
  organization, or government agency named in its materials.
- Feedback from the skill does not guarantee admission, funding, or visa
  approval.
