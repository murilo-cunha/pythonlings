import inspect
import pydantic5 as mod
from pydantic5 import d, c2


def test_model_dump_returns_dict():
    assert isinstance(d, dict)

def test_model_dump_values():
    assert d == {"host": "localhost", "port": 8080, "debug": False}

def test_model_validate():
    assert c2.host == "0.0.0.0"
    assert c2.port == 443

def test_uses_v2_api():
    src = inspect.getsource(mod)
    assert "model_dump" in src
    assert "model_validate" in src
