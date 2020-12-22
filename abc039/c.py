#
# abc039 c
#
import sys
from io import StringIO
from typing import TYPE_CHECKING
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例1(self):
        input = """WBWBWWBWBWBWWBWBWWBW"""
        output = """Do"""
        self.assertIO(input, output)


def resolve():
    S = input()

    T = "WBWBWWBWBWBW"*3
    d = {}
    d["Do"] = T[:20]
    d["Re"] = T[2:22]
    d["Mi"] = T[4:24]
    d["Fa"] = T[5:25]
    d["So"] = T[7:27]
    d["La"] = T[9:29]
    d["Si"] = T[11:31]

    for k, v in d.items():
        if v == S:
            print(k)
            break


if __name__ == "__main__":
    # unittest.main()
    resolve()
