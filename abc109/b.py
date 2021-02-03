#
# abc109 b
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
        input = """4
hoge
english
hoge
enigma"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """9
basic
c
cpp
php
python
nadesico
ocaml
lua
assembly"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8
a
aa
aaa
aaaa
aaaaa
aaaaaa
aaa
aaaaaaa"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """3
abc
arc
agc"""
        output = """No"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    W = [input() for _ in range(N)]

    ans = "Yes"
    if len(set(W)) != N:
        ans = "No"
    else:
        l = W[0][-1]
        for w in W[1:]:
            if w[0] != l:
                ans = "No"
                break
            l = w[-1]

    print(ans)


if __name__ == "__main__":
    # unittest.main()
    resolve()
