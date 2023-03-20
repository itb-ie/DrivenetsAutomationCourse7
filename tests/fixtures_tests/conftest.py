import random
import pytest
import logging

logger = logging.getLogger(__name__)
possible_fruits = ["apple", "banana", "orange", "cherry", "tomato", "fig", "grape", "kiwi", "mango", "coconut", "durian", "lemon"]


@pytest.fixture(scope="session")
def harvest_fruit():
    initial_harvest = random.sample(possible_fruits, 6)
    logger.info(f"We harvested: {initial_harvest}")
    yield initial_harvest
    logger.info(f"After the meal, we got these fruits left: {initial_harvest}")
    initial_harvest = []
    logger.info(f"We threw away the leftover fruit, got these fruits left: {initial_harvest}")


@pytest.fixture(scope='class')
def fruit_bowl(harvest_fruit):
    logger.info(f"Created the bowl with {harvest_fruit}")
    return harvest_fruit.copy()


@pytest.fixture()
def get_fruit(fruit_bowl):
    # get a random fruit from the fruit bowl
    fruit = random.choice(fruit_bowl)
    logger.info(f"Picked the fruit {fruit} from the fruit ball")
    return fruit