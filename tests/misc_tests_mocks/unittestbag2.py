from src.bag import Bag
from src.reusabletimer import ReusableTimer
from src.identification import FingerprintScanner
from unittest.mock import Mock
import pytest
from random import randint


# @pytest.MonkeyPatch


@pytest.mark.parametrize("mock_input", "expected_value",[
    ('Toronto', 'Toronto'),
    ('Montreal', 'Montreal'),
    ('Ottawa', 'Ottawa')
])
def test_devicelocation_fail(mock_input, expected_value):
    assert not mock_input == expected_value

@pytest.mark.xfail
def test_check_it_fails():
    pass


@pytest.mark.
@pytest.fixture
# set environment
def myBag():
    timer = Mock(spec=ReusableTimer)
    scanner = Mock(spec=FingerprintScanner)
    bag = Bag(timer, scanner)
    bag.set_location('Ottawa')
    bag.get_temperature()  # or we could mock temperature

    return bag


def test_start(myBag):
    timer = myBag.timer
    settings = myBag.settings
    devloc = myBag.devicelocation
    assert ('Ottawa' in devloc)
    myBag.charge_battery(100 * randint(1, 10))
    myBag.place_contents()


def test_end():
    def mockreturn():
        return Bag()

    pytest.MonkeyPatch.setattr(Bag, "", mockreturn())

    assert('20C' == None)
