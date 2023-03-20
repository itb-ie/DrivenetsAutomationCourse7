import logging
import pytest

logger = logging.getLogger(__name__)


def test_1(name):
    logger.info(f"Dear {name}, this is the first test")
    assert True


def test_2(name):
    logger.info(f"Dear {name}, this is the second test")
    assert False

@pytest.mark.bogdan
def test_3(name):
    logger.info(f"Dear {name}, this is the third test")
    assert True

def test_4(name):
    logger.info(f"Dear {name}, this is the forth test")
    assert True