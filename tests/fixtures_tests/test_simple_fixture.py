import pytest
import os
import logging

logger = logging.getLogger()


@pytest.fixture(autouse=False)
def write_to_file():
    logger.info("Creating the file")
    fp = open("test.txt", "w")
    logger.info("Putting the text inside the file")
    fp.write("Bye World!")
    fp.close()
    yield
    # this is the teardown, I delete the file
    logger.info("Deleting the file in the teardown part")
    os.remove("test.txt")


def test_file(write_to_file):
    logger.warning("Starting the test!!!")
    fp = open("test.txt", "r")
    text = fp.read()
    logger.warning(f"Checking that Bye in inside the {text}")
    assert "Bye" in text


def test_file_not_there():
    logger.info("Checking if the file is there")
    with pytest.raises(FileNotFoundError):
        fp = open("test.txt", "r")
        fp.close()
