# this is the simplests way to write pytest tests
import time

import logging

import pytest

logger = logging.getLogger(__name__)

def test_1():
    time.sleep(2)
    logger.info("This is my first and simplest test!")

def test_2():
    time.sleep(3)
    logger.info("This is my second and simplest test!")

def test_3():
    time.sleep(1)
    logger.info("This is my third and simplest test!")
    logger.debug("First I prepare the IP addrs")
    ip = "1.2.3.4"
    logger.debug("Incrementing the ip")
    ip = "1.2.3.5"
    logger.warning(f"validating that ip {ip} equals 5.5.5.5")
    assert ip == "5.5.5.5"

def bogdan_test():
    logger.info("this one also?")
    logger.debug("Will it get collected???")
    assert False

def test_divide_1():
    logger.info("Doing a simple division test")
    x = 4
    y = 2
    assert x/y == 2


def test_divide_2():
    logger.info("Doing invalid import test")
    with pytest.raises(ModuleNotFoundError):
        import bogdan
    assert True
