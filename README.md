# HexaLog

HexaLog is a logging port and set of opinionated adapters meant to simplify using a logger in a hexagonal architecture.

## Why

In hexagonal architecture dependencies external dependencies should be injected to adapters and the service at runtime. This means business logic doesn't directly depend on external concerns which can (arguably) make code easier to test and maintain. A logger is an external dependency, therefor it to can be passed into a service or adapter at runtime.


```python

```
