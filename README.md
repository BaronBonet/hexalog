# HexaLog

HexaLog is a logging port and set of opinionated adapters meant to simplify using a logger in a hexagonal architecture.

## Why

In hexagonal architecture dependencies external dependencies should be injected to adapters and the service at runtime. This means business logic doesn't directly depend on external concerns which can (arguably) make code easier to test and maintain. A logger is an external dependency, therefor it to can be passed into a service or adapter at runtime.

![HexaLog Example](https://cdn.ericcbonet.com/python-hexalog-example.png)

## Installation

```bash
pip install hexalog
```

## Usage

For production environments hexalog wraps [structlog](https://www.structlog.org/en/stable/) and provides a `structlog` adapter.

From development environments hexalog wraps the standard library `logging` module and provides a `logging` adapter.

If you have some service or adapter then make the logger port a dependency of that class:

```python
from hexalog.ports import Logger

class SomeService:
    def __init__(self, logger: Logger):
        self.logger = logger

    def do_something(self):
        self.logger.info("Doing something")
```

Then in your entrypoint to the application where you wire up your dependencies you can inject a logger like so:

```python
import os

from some_service import SomeService
from hexalog.adapters.struct_logger import StructLogger

log_level = os.getenv("LOG_LEVEL", "DEBUG")

logger = StructLogger(log_level=log_level)
# If you want to use the cli logger then you just need to inject that one
# logger = CliLogger(log_level=log_level)

service = SomeService(logger=logger)

service.do_something()
```

See the `examples` directory for more information.
