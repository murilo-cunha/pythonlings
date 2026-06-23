from abstract_classes4 import JsonRecord, CsvRow, Serializable, BaseModel


def test_json_record():
    assert JsonRecord({"name": "Ada"}).serialize() == '{"name": "Ada"}'

def test_csv_row():
    assert CsvRow([1, 2, 3]).serialize() == "1,2,3"

def test_csv_satisfies_protocol():
    assert isinstance(CsvRow([1]), Serializable)

def test_csv_not_base_model():
    assert not isinstance(CsvRow([1]), BaseModel)
