"""
logging.getLogger(name) returns (or creates) a named logger.
Set logger.setLevel(logging.DEBUG) to emit debug-level messages.
The root logger defaults to WARNING — child loggers inherit it unless overridden.

Set the logger level to DEBUG so all three messages appear in the output.
"""

# I AM NOT DONE

import logging
import io

log_buffer = io.StringIO()
handler = logging.StreamHandler(log_buffer)
handler.setLevel(logging.DEBUG)

logger = logging.getLogger("myapp")
logger.addHandler(handler)

logger.debug("starting up")
logger.info("processing item 1")
logger.warning("low disk space")

output = log_buffer.getvalue()
