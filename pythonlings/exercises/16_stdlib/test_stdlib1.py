from stdlib1 import data_dir, hello_file


def test_data_dir_exists():
    assert data_dir.is_dir()

def test_hello_file_exists():
    assert hello_file.exists()

def test_hello_file_content():
    assert hello_file.read_text() == "Hello, pathlib!"

def test_suffix():
    assert hello_file.suffix == ".txt"

def test_stem():
    assert hello_file.stem == "hello"
