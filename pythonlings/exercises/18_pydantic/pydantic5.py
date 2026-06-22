# I AM NOT DONE

import warnings
warnings.filterwarnings("error", category=DeprecationWarning)

from pydantic import BaseModel


class Config(BaseModel):
    host: str
    port: int
    debug: bool = False


c = Config(host="localhost", port=8080)

# Fix: use the correct Pydantic v2 method names
# In Pydantic v2: .dict() is deprecated, use .model_dump()
#                 Model.parse_obj() is deprecated, use Model.model_validate()
d = c.dict()  # Fix: use c.model_dump()

c2 = Config.parse_obj({"host": "0.0.0.0", "port": 443, "debug": True})  # Fix: use Config.model_validate()

# DON'T EDIT THE TESTS
assert d == {"host": "localhost", "port": 8080, "debug": False}
assert isinstance(d, dict)
assert c2.host == "0.0.0.0"
assert c2.port == 443
