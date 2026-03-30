# akasha-apis

Akasha's external API adapter layer.

This repo provides normalized adapters for outside data sources so other Akasha systems
do not need to speak raw provider dialects directly.

## Purpose

`akasha-apis` sits between:

- external services
- Akasha-native systems

It is responsible for:

- fetching data from providers
- normalizing responses into Akasha-shaped payloads
- exposing provider metadata
- keeping source-specific weirdness out of higher layers

## What it is not

This repo is **not**:

- a discovery catalog
- a bookmark atlas
- a dashboard repo
- a pattern-analysis engine
- a meaning-making layer

That means:

- Grand Atlas discovers candidate APIs and tools
- `akasha-apis` implements stable adapters to chosen sources
- `akasha-time-nexus` consumes those adapters to enrich event records

## Core adapter contract

Every adapter should expose the same basic surface:

- `fetch(...)`
- `normalize(raw)`
- `metadata()`

A thin convenience method like `get(...)` may combine fetch + normalize.

## Initial provider classes

V2 includes starter adapters for:

- astronomy
  - sunrise/sunset provider
  - lunar context stub
- weather
  - Open-Meteo snapshot provider
- geo
  - timezone lookup from coordinates

## Relationship to other Akasha repos

```text
Grand Atlas
    discovers APIs, datasets, services

akasha-apis
    implements normalized adapters

akasha-time-nexus
    consumes adapters to build context bundles
```

## Next moves

- add caching
- expand provider registry
- add tides provider
- add geomagnetic provider
- add tests around normalization contracts
