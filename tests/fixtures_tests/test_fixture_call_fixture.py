import logging
import pytest
import random

logger = logging.getLogger(__name__)


class Suite1:
    def test_1(self, fruit_bowl, get_fruit, harvest_fruit):
        logger.info(f"Inside the test, we have the fruit bowl: {fruit_bowl}")
        logger.info(f"We eat: {get_fruit}")
        fruit_bowl.remove(get_fruit)
        logger.info(f"I am left with {fruit_bowl} in the bowl")
        assert get_fruit not in fruit_bowl and get_fruit in harvest_fruit

    def test_2(self, fruit_bowl, get_fruit, harvest_fruit):
        logger.info(f"Inside the test, we have the harvest: {fruit_bowl}")
        logger.info(f"We eat: {get_fruit}")
        fruit_bowl.remove(get_fruit)
        logger.info(f"I am left with {fruit_bowl} in the bowl")
        assert get_fruit not in fruit_bowl and get_fruit in harvest_fruit


class Suite2:
    def test_1(self, fruit_bowl, get_fruit, harvest_fruit):
        logger.info(f"Inside the test, we have the fruit bowl: {fruit_bowl}")
        logger.info(f"We eat: {get_fruit}")
        fruit_bowl.remove(get_fruit)
        logger.info(f"I am left with {fruit_bowl} in the bowl")
        assert get_fruit not in fruit_bowl and get_fruit in harvest_fruit

    def test_2(self, fruit_bowl, get_fruit, harvest_fruit):
        logger.info(f"Inside the test, we have the harvest: {fruit_bowl}")
        logger.info(f"We eat: {get_fruit}")
        fruit_bowl.remove(get_fruit)
        logger.info(f"I am left with {fruit_bowl} in the bowl")
        assert get_fruit not in fruit_bowl and get_fruit in harvest_fruit
