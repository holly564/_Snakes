import threading
from unittest import TestCase
from unittest import mock
import unittest.main
from filework.src.reusableTimer import ReusableTimer

"""Unit testing Reusable Timer and mocking its threading.timer dependency"""


class ReusableTimerUnitTestCase(TestCase):
    def test_countdown(self):
        my_func = lambda: None
        with mock.patch("threading.Timer"):
            timer = ReusableTimer()
            timer.countdown(0.1, my_func)
            threading.Timer.assert_called_once_with(0.1, my_func)
            timer.timer.start.assert_called_once()

    def test_end(self):
        my_func = lambda: None
        with mock.patch("threading.Timer"):
            timer = ReusableTimer()
            timer.countdown(0.1, my_func)
            timer.end()
            timer.timer.cancel.assert_called_once()


if __name__ == '__main__':
    unittest.main()
