import pytest

# here we define our hooks

# what if we want to add extra options to pytest???

def pytest_addoption(parser):
    parser.addoption(
        '--name',
        action='store',
        dest='name',
        default='Bogdan',
        help='Name of the person running the tests'
    )

@pytest.fixture(scope='session')
def name(request):
    return request.config.getoption('name')


def pytest_collection_modifyitems(items):
    print("Running collection modify")
    new_test_items = []
    for item in items[:]:
        if item.name == "test_2":
            # return
            # items.remove(item)
            continue
        if item.get_closest_marker('bogdan'):
            # If the 'run_twice' marker is present, add the test item to the collection twice
            # new_test_items.extend([item, item])
            new_test_items = [item] + new_test_items
        else:
            new_test_items.append(item)

    items[:] = new_test_items


def pytest_runtest_setup(item):
    if item.name == "test_4":
        pytest.skip("Skipping test_4")