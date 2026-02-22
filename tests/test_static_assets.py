from pathlib import Path


def test_index_exists():
    assert Path('index.html').exists()
