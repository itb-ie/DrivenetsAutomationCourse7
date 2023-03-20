# pytests can also work with classes!

import logging

logger = logging.getLogger(__name__)


class SuiteClass:

    def first_test(self):
        logger.debug("This is the first test")

    def second_test(self):
        logger.debug("This is the second test")
        assert False

