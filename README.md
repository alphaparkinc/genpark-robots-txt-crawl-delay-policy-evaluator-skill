# genpark-robots-txt-crawl-delay-policy-evaluator-skill

Agent Skill implementing **RFC 9309 Robots.txt Permission & Rate Delay Evaluation** in 100% Python standard library.

## Architectural Flow
```mermaid
flowchart TD
    Robots["robots.txt File"] --> Parser["Directive Parser (Disallow / Allow / Crawl-delay)"]
    Path["Target URL Path"] --> Matcher["Prefix Path Matcher"]
    Parser & Path --> Matcher
    Matcher --> Allow{"Matches Allow Rule?"}
    Allow -->|Yes| Permit["Permit Crawl Request"]
    Allow -->|No| Disallow{"Matches Disallow Rule?"}
    Disallow -->|Yes| Block["Block Autonomous Agent Access"]
    Disallow -->|No| Permit
```
