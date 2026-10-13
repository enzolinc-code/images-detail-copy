# Image generation adapters

V0.1 intentionally does not implement a Python SDK wrapper for image generation.

In normal Codex usage, the Skill directs Codex to use the built-in `image_gen` tool. This keeps the first version aligned with Codex's native image workflow and avoids requiring an API key.

A future explicit CLI/API adapter may be added only when needed for unattended batch jobs or external orchestration.
