# pretty logger

## Example:

```
from pretty_logging import pretty_logger

pretty_logger.info("info---sss")
pretty_logger.error("error---sss")
pretty_logger.debug("debug---sss")

同时发到fluentd

export FLUENT_HOST=127.0.0.1
export FLUENT_PORT=24224
export FLUENT_APP=pretty
export FLUENT_TAG=log
```