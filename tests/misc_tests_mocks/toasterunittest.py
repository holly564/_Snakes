from unittest import TestCase
from unittest.mock import Mock
import unittest.main
from filework.src.reusableTimer import ReusableTimer
from filework.src.toaster import Toaster


"""unit testing of Toaster class only which is why ReusableTimer is mocked"""
class ToasterUnitTestCase(TestCase):
    def test_start(self):
        timer = Mock(spec=ReusableTimer)
        toaster = Toaster(timer)
        toaster.push_down()
        self.assertTrue(toaster.hot)
        timer.countdown.assert_called_once_with(30, toaster.pop_up)

    def test_end(self):
        timer = Mock(spec=ReusableTimer)
        toaster = Toaster(timer)
        toaster.hot = True
        toaster.pop_up()
        self.assertFalse(toaster.hot)
        timer.end.assert_called_once()



if __name__ == '__main__':
    unittest.main()
