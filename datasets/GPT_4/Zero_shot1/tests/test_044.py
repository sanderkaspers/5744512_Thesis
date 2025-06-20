import unittest


class TestVersion(unittest.TestCase):
    def test_1(self):
        with patch("builtins.print") as mocked:
            divisor(6)
        mocked.assert_has_calls([call(1), call(2), call(3), call(6)])

    def test_2(self):
        with patch("builtins.print") as mocked:
            divisor(7)
        mocked.assert_has_calls([call(1), call(7)])

    def test_3(self):
        with patch("builtins.print") as mocked:
            divisor(1)
        mocked.assert_called_once_with(1)

    def test_4(self):
        with patch("builtins.print") as mocked:
            divisor(-5)
        mocked.assert_not_called()

    def test_5(self):
        with patch("builtins.print") as mocked:
            divisor(9)
        mocked.assert_has_calls([call(1), call(3), call(9)])

    def test_6(self):
        with patch("builtins.print") as mocked:
            divisor(100)
        expected = [call(i) for i in [1, 2, 4, 5, 10, 20, 25, 50, 100]]
        mocked.assert_has_calls(expected)

    def test_7(self):
        with patch("builtins.print") as mocked:
            divisor(12)
        calls = [call(1), call(2), call(3), call(4), call(6), call(12)]
        self.assertEqual(mocked.mock_calls, calls)

    def test_8(self):
        with patch("builtins.print") as mocked:
            divisor(2)
        mocked.assert_has_calls([call(1), call(2)])

    def test_9(self):
        self.assertIsNone(divisor(5))

    def test_10(self):
        with patch("builtins.print") as mocked:
            divisor(8)
        outputs = [c[1][0] for c in mocked.call_args_list]
        self.assertEqual(outputs, [1, 2, 4, 8])

    def test_11(self):
        with patch("builtins.print") as mocked:
            divisor(True)
        mocked.assert_called_once_with(1)

    def test_12(self):
        with patch("builtins.print") as mocked:
            divisor(10)
        self.assertIn(call(10), mocked.mock_calls)

    def test_13(self):
        with patch("builtins.print") as mocked:
            divisor(30)
        seen = set()
        for c in mocked.call_args_list:
        self.assertNotIn(c[1][0], seen)
        seen.add(c[1][0])

    def test_14(self):
        with patch("builtins.print") as mocked:
            divisor(15)
        calls = mocked.call_args_list
        for i in range(1, 16):
            if 15 % i == 0:
                self.assertIn(call(i), calls)

    def test_15(self):
        with patch("builtins.print") as mocked:
            divisor(-10)
            mocked.assert_not_called()
