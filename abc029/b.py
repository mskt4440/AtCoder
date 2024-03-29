#
# abc029 b
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

    def test_入力例1(self):
        input = """january
february
march
april
may
june
july
august
september
october
november
december"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """rrrrrrrrrr
srrrrrrrrr
rsr
ssr
rrs
srsrrrrrr
rssrrrrrr
sss
rrr
srr
rsrrrrrrrr
ssrrrrrrrr"""
        output = """11"""
        self.assertIO(input, output)


def resolve():
    S = [input() for _ in range(12)]

    ans = 0
    for s in S:
        if s.count("r") >= 1:
            ans += 1
    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
