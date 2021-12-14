#
# abc201 b
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
        input = """3
Everest 8849
K2 8611
Kangchenjunga 8586"""
        output = """K2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
Kita 3193
Aino 3189
Fuji 3776
Okuhotaka 3190"""
        output = """Kita"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
QCFium 2846
chokudai 2992
kyoprofriends 2432
penguinman 2390"""
        output = """QCFium"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    ST = []
    for i in range(N):
        n, h = input().split()
        h = int(h)
        ST.append([n, h])

    ST.sort(key=lambda x: x[1], reverse=True)
    print(ST[1][0])


if __name__ == "__main__":
    # unittest.main()
    resolve()
