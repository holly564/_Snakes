#toasterintegrationTest.py
from unittest import TestCase, main
from filework.src.reusableTimer import ReusableTimer
from filework.src.toaster import Toaster



class ToasterIntegrationTest(TestCase):
    """Single integration test which verifies Toaster and RusableTimer classes together w/o any mocks"""
    def setUp(self):
        self.timer = ReusableTimer()
        self.toaster = Toaster(self.timer)
        self.toaster.doneness = 0

    def tearDown(self):
        print("* Test clean-up")


    def test_wait_finish(self):
        self.assertFalse(self.toaster.hot)
        self.toaster.push_down()
        self.assertTrue(self.toaster.hot)
        self.timer.timer.join()
        self.assertFalse(self.toaster.hot)

    def test_cancel_early(self):
        self.assertFalse(self.toaster.hot)
        self.toaster.push_down()
        self.assertTrue(self.toaster.hot)
        self.toaster.pop_up()
        self.assertFalse(self.toaster.hot)

    if __name__ == "__main__":
        main()
