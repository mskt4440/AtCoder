#
# arc105 a
#
import sys
from io import StringIO
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

    def test_入力例_1(self):
        input = """1 3 2 4"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 2 4 8"""
        output = """No"""
        self.assertIO(input, output)


def resolve():
    I = list(map(int, input().split()))

    ans = "No"
    for bit in range(1 << 3):
        e = 0
        ne = 0
        if "1" not in bin(bit):
            continue
        for i in range(4):
            if bit & 1 << i:
                e += I[i]
            else:
                ne += I[i]
        if e == ne:
            ans = "Yes"
            break

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
