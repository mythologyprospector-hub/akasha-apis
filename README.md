# Akasha APIs

Akasha APIs define the standardized interfaces between the Akasha ecosystem
and external data sources.

This repository contains connectors, authentication patterns, and normalization
schemas for interacting with public APIs.

These connectors allow Akasha systems to gather artifacts from the outside world
without embedding API logic throughout the ecosystem.

---

## Purpose

Akasha APIs serve as the ecosystem's **data interface layer**.

External services → API connectors → normalized artifacts → Akasha systems

This separation ensures that:

- external dependencies remain modular
- API credentials remain isolated
- collectors remain replaceable
- internal systems remain stable

---

## Components

### API Registry

`API_REGISTRY.yaml`

Defines known APIs, endpoints, authentication methods, and associated collectors.

---

### API Credentials

`API_KEYS.env.example`

Template for configuring API credentials locally.

Never commit real keys to this repository.

---

### Collectors

Collectors implement connectors for specific APIs.

Examples:

- GitHub API
- NASA API
- Wikidata SPARQL
- OpenAlex research graph
- arXiv paper search

Collectors return normalized artifacts usable by:

- Akasha Lens
- Akasha Discovery
- Akasha Forge

---

### Schemas

Schemas define normalized artifact formats returned by collectors.

These schemas ensure consistent data structures across the ecosystem.

---

## Philosophy

External systems change frequently.

Akasha APIs isolate those changes from the rest of the ecosystem.

Collectors may evolve.

The internal ontology remains stable.

---

## Role in the Akasha Ecosystem

Akasha APIs function as **external sensors**.

They gather signals from the wider world and convert them into artifacts
that can be interpreted by the system.

Axioms define the laws.
World defines the ontology.
Constellation defines the map.

APIs gather new information from reality.
Lens interprets it.
Discovery explores it.
Forge builds with it.

---

Akasha APIs expand the system's awareness.
---

This repository participates in the Akasha ecosystem and is described by repo-manifest.yaml.
