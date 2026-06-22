# I AM NOT DONE

import logging
import io

# Fix: configure a logger named "myapp" at DEBUG level
# that writes to a StringIO buffer so we can inspect the output
log_buffer = io.StringIO()
handler = logging.StreamHandler(log_buffer)
handler.setLevel(logging.DEBUG)

logger = logging.getLogger("myapp")
# Fix: set logger level to DEBUG (currently it won't emit DEBUG messages)
logger.addHandler(handler)

logger.debug("starting up")
logger.info("processing item 1")
logger.warning("low disk space")

output = log_buffer.getvalue()


# DON'T EDIT THE TESTS
assert "starting up" in output       # Only present if DEBUG level is set
assert "processing item 1" in output
assert "low disk space" in output
