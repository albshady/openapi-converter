import pathlib

import pytest

import converter


@pytest.fixture
def data_dir():
    return pathlib.Path(__file__).parent / 'data'


def test_convert(data_dir: pathlib.Path):
    input_file = data_dir / 'openapi.json'
    converted = converter.json_to_yaml(input_file.read_text())

    assert 'read_item' not in converted
    assert 'readItem' in converted
    assert 'create_item' not in converted
    assert 'createItem' in converted
