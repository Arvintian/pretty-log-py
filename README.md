# pretty logger

## Example:

```
from pretty_logging import pretty_logger

pretty_logger.info("info---sss")
pretty_logger.error("error---sss")
pretty_logger.debug("debug---sss")

同时发到fluentd

export LOG_FLUENT_HOST=127.0.0.1
export LOG_FLUENT_PORT=24224
export LOG_FLUENT_APP=pretty
export LOG_FLUENT_TAG=log

// send an event record with 'pretty.log'
```