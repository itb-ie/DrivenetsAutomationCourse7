import pytest


@pytest.mark.skip
def test_1():
    logger.info("Will compare 2+2 with 6")
    assert 2+2 == 6


@pytest.mark.xfail(reason="This is zero division")
def test_2():
    logger.info("About to do some 0 division")
    assert 4/0


@pytest.mark.parametrize("input_value, expected_result", [(2, 4), (4, 8), (22, 44)])
def test_double(input_value, expected_result):
    assert 2*input_value == expected_result


@pytest.mark.parametrize("input_value, expected_result, negative", [(2, 4, False), (4, 8, False), (22, 44, False), (2, 5, True)])
def test_double_2(input_value, expected_result, negative):
    if not negative:
        assert 2*input_value == expected_result
    else:
        assert 2 * input_value != expected_result


@pytest.mark.parametrize("input_value, expected_result, negative", [(2, 5, False), (4, 9, False), (122, 44, False), (2, 4, False)])
@pytest.mark.xfail(reason="wrong values")
def test_double_3(input_value, expected_result, negative):
    if not negative:
        assert 2*input_value == expected_result
    else:
        assert 2 * input_value != expected_result




