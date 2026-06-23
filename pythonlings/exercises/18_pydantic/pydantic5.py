"""
Pydantic v2 renamed several methods from v1:
  .dict()            → .model_dump()       (returns a plain Python dict)
  .json()            → .model_dump_json()  (returns a JSON string)
  Model.parse_obj()  → Model.model_validate() (validates from a dict)

Update the two deprecated method calls to use the v2 names.
"""

# I AM NOT DONE

from pydantic import BaseModel


class Config(BaseModel):
    host: str
    port: int
    debug: bool = False


c = Config(host="localhost", port=8080)

d = c.dict()

c2 = Config.parse_obj({"host": "0.0.0.0", "port": 443, "debug": True})
