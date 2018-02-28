from tempfile import TemporaryDirectory
from pathlib import Path

import pytest


@pytest.fixture(scope='session')
def tmpdir():
    with TemporaryDirectory() as d:
        yield Path(d)


@pytest.fixture
def testdir():
    return Path(__file__).parent
