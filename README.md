# Astrology Birth Chart Reading Agent

## Overview

The Astrology Birth Chart Reading Agent skill helps an agent create reflective natal chart readings from user-provided chart placements, chart screenshots, or birth date/time/place details. It emphasizes symbolic interpretation, privacy, transparent uncertainty, and non-deterministic language.

This skill is designed for entertainment, self-reflection, creative writing, and astrology education. It is not designed for medical, legal, financial, mental health, safety, or other professional advice.

## When to use

Use this skill for requests such as:

- "Read my birth chart."
- "Interpret my sun, moon, and rising."
- "What does Venus in Scorpio in the 7th house mean?"
- "Write a natal chart report from these placements."
- "Analyze this chart screenshot."
- "Create an astrology reading agent prompt."
- "Give me a grounded birth chart reading with reflection prompts."

## Contents

- `SKILL.md`: agent-facing instructions, trigger description, workflow, boundaries, output formats, checklist, and safety rules.
- `README.md`: human-readable overview and package guide.
- `agents/openai.yaml`: OpenAI metadata and invocation policy.
- `assets/birth-chart-intake-form.md`: reusable intake form for collecting only necessary chart details.
- `assets/reading-template.md`: reusable natal chart reading template.
- `references/style-guide.md`: tone, wording, formatting, and safety examples.
- `references/astrology-interpretation-framework.md`: interpretation layers and synthesis guidance.
- `scripts/example_helper.py`: deterministic helper that checks whether an intake JSON file has enough data for different reading types.

## Package structure

```text
astrology-birth-chart-reading-agent/
|-- SKILL.md
|-- README.md
|-- agents/
|   `-- openai.yaml
|-- assets/
|   |-- .gitkeep
|   |-- birth-chart-intake-form.md
|   `-- reading-template.md
|-- references/
|   |-- astrology-interpretation-framework.md
|   `-- style-guide.md
`-- scripts/
    `-- example_helper.py
```

## Usage notes

The agent should prefer user-provided chart placements or chart screenshots over collecting raw birth data. When exact birth time is missing, the agent should clearly state that the Ascendant, houses, angles, and some Moon details may be uncertain.

The reading should avoid fear-based language and should never present astrology as proof, diagnosis, or guaranteed prediction.

## Example prompt

```text
Use the Astrology Birth Chart Reading Agent skill. Create a grounded 1,200-word natal chart reading from these placements. Focus on identity, relationships, work themes, and growth edges. Include a short framing note and five reflection prompts.
```
