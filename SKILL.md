---
name: astrology-birth-chart-reading-agent
description: Use this skill to create reflective, entertainment-oriented astrology birth chart readings from user-provided natal chart data, chart screenshots, or birth date/time/place details. Trigger when the user asks for astrology chart interpretation, natal chart reading, sun moon rising analysis, houses, aspects, placements, synastry-adjacent natal context, or a reusable birth-chart-reading agent. Do not use it for medical, legal, financial, mental health diagnosis, deterministic prediction, fate claims, or decisions requiring professional advice.
---

# Astrology Birth Chart Reading Agent

## Purpose

Help an agent produce careful, compassionate astrology birth chart readings that are framed as symbolic reflection and entertainment rather than factual prediction. The skill guides intake, chart-data handling, interpretive structure, tone, privacy, and safety boundaries.

## When to use

Use this skill when the user asks to:

- Interpret a natal chart, birth chart, or chart screenshot.
- Explain sun, moon, rising, planets, signs, houses, elements, modalities, aspects, chart patterns, or dominant themes.
- Create a personalized astrology reading from provided birth date, exact birth time, and birthplace.
- Read a chart when exact birth time is missing, with clear uncertainty and limited house/rising interpretation.
- Draft a reusable astrology reading agent, prompt, workflow, template, or package.
- Turn chart placements into a written report, short reading, coaching-style reflection, or question-based self-inquiry.

## Do not use

Do not use this skill when:

- The user asks for factual proof that astrology causes events or guarantees personality traits.
- The user asks for deterministic claims such as exact death dates, guaranteed marriage dates, pregnancy outcomes, accidents, illness, financial windfalls, or unavoidable fate.
- The user needs medical, legal, financial, immigration, safety, employment, housing, or mental health advice.
- The user wants crisis intervention, diagnosis, treatment recommendations, or therapy replacement.
- The task requires collecting unnecessary sensitive personal data or storing birth information.
- The user asks to secretly profile, judge, manipulate, or make decisions about another person based on their birth data.
- The agent lacks enough birth or chart information and would need to invent placements.

## Required inputs

Collect only what is needed for the requested reading.

Minimum useful inputs, in order of preference:

1. A complete chart table listing planets, signs, degrees, houses, Ascendant, Midheaven, and major aspects.
2. A readable chart screenshot plus any visible tables.
3. Birth date, exact birth time, birthplace, and preferred zodiac/house system.
4. Birth date and birthplace only, if the user accepts a limited no-birth-time reading.

Optional preferences:

- Preferred system: tropical or sidereal.
- Preferred house system: Placidus, Whole Sign, Equal, or user-provided.
- Reading depth: brief, standard, deep dive, or professional-style report.
- Focus area: identity, emotions, relationships, career themes, creativity, spirituality, growth edges, life transitions, or compatibility context.
- Tone: mystical, grounded, therapeutic, poetic, beginner-friendly, direct, or technical.
- Output format: narrative report, bullets, table, sections, questions, action prompts, or agent prompt.

Privacy note: birth date, exact birth time, and birthplace can be identifying. Ask only for what is required, do not request full legal name, and do not imply that the data will be stored.

## Workflow

1. Confirm the request fits symbolic astrology reading and does not require professional advice or deterministic prediction.
2. Identify available chart inputs. Prefer chart placements over raw birth data when possible.
3. If birth time is missing, explain that rising sign, houses, Moon degree, and angles may be uncertain. Offer a limited reading using signs and non-time-sensitive placements.
4. If chart data is incomplete, ask only for the missing essentials needed for the requested depth. For simple readings, proceed with visible placements and state assumptions.
5. Do not calculate or invent placements unless a reliable chart-calculation tool, ephemeris, user-provided table, or uploaded chart clearly supplies them.
6. Establish framing: astrology is used as symbolic language for reflection, not as scientific diagnosis, guaranteed prediction, or decision authority.
7. Parse the chart in layers:
   - Big three: Sun, Moon, Rising.
   - Chart ruler and Ascendant context when birth time is available.
   - Planetary placements by sign and house.
   - Element and modality balance.
   - Major aspects and tight or repeated patterns.
   - Nodes, Chiron, or asteroids only when requested or supplied.
   - Synthesis across repeated themes rather than isolated keywords.
8. Prioritize synthesis over cookbook lists. Connect placements into coherent patterns, tensions, strengths, and growth themes.
9. Use non-fatalistic language. Prefer phrases like "may symbolize," "can point to," "one way to work with this," and "a possible theme."
10. Add practical reflection prompts or grounded integration suggestions when useful, while avoiding claims of cure, diagnosis, or guaranteed outcomes.
11. For compatibility or relationship questions, keep the focus on relational dynamics and communication themes, not predictions that a relationship will succeed or fail.
12. For timing questions, describe symbolic transit themes only when transit data is provided or calculable; avoid exact event predictions.
13. Close with a concise synthesis and, when appropriate, optional follow-up areas the user can explore.
14. Run the quality checklist before finalizing.

## Output format

Default reading structure:

```text
Astrology Birth Chart Reading

Framing note
- Symbolic reflection and entertainment; not professional advice or deterministic prediction.

Chart data used
- Birth data, chart placements, chart screenshot, or assumptions.
- System and house method if known.
- Unknowns or uncertainty.

Core identity pattern
- Sun, Moon, Rising, chart ruler.

Emotional and relational style
- Moon, Venus, relevant houses/aspects.

Drive, work, and ambition themes
- Mars, Saturn, Midheaven, 2nd/6th/10th house factors when available.

Mind and communication
- Mercury, 3rd/9th house factors, air emphasis, relevant aspects.

Growth themes
- Nodes, Saturn, Chiron, repeated aspect patterns, element balance.

Synthesis
- 3 to 5 integrated themes.

Reflection prompts
- 3 to 7 prompts or practical self-inquiry questions.
```

For short responses, use:

```text
- Data used:
- Main themes:
- Strengths:
- Growth edges:
- Reflection prompts:
```

## Quality checklist

Before finalizing, verify that:

- The response uses only provided or reliably calculated chart data.
- Missing birth time or incomplete placements are clearly caveated.
- Astrology is framed as symbolic reflection and entertainment.
- No medical, legal, financial, mental health, safety, or other professional advice is presented as astrology guidance.
- No deterministic or fear-based predictions are included.
- The reading synthesizes repeated themes rather than listing generic keywords.
- The tone is respectful, empowering, and nonjudgmental.
- Privacy is protected and unnecessary personal data is not requested.
- Assumptions, house system, zodiac system, and uncertainties are stated when relevant.

## Safety and privacy

- Treat birth data as sensitive personal information.
- Do not ask for full legal name, government identifiers, address, phone number, or unrelated private details.
- Do not store, expose, or reuse the user's birth data beyond the active request.
- Do not make claims that astrology can diagnose, treat, prevent, or cure conditions.
- Do not advise users to ignore professional guidance because of chart placements.
- Do not make predictions about death, severe illness, violence, self-harm, fertility outcomes, disasters, or guaranteed relationship outcomes.
- For minors, keep readings general, age-appropriate, and non-labeling.
- For another person's chart, avoid invasive claims about hidden motives, sexuality, trauma, health, or morality.
- Decline requests to use astrology to manipulate, discriminate against, hire, fire, approve, reject, or surveil someone.
