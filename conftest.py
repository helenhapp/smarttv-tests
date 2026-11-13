import pytest
from smart_tv import SmartTV


@pytest.fixture
def tv():
    return SmartTV()


@pytest.fixture
def tv_on():
    tv = SmartTV()
    tv.power_on()
    return tv
