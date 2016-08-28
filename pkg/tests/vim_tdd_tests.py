import unittest
import pkg.plugin.vim_tdd as sut


@unittest.skip("Don't forget to test!")
class VimTddTests(unittest.TestCase):

    def test_example_fail(self):
        result = sut.vim_tdd_example()
        self.assertEqual("Happy Hacking", result)
