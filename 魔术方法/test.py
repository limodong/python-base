import math
from functools import total_ordering

@total_ordering
class Fraction:
    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ValueError("分母不能为零")
        # 保证分母为正，负号移到分子
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator
        # 约分
        gcd = math.gcd(abs(numerator), denominator)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

    # ---------- 算术运算 ----------
    def __add__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        if other.numerator == 0:
            raise ZeroDivisionError("不能除以零")
        num = self.numerator * other.denominator
        den = self.denominator * other.numerator
        return Fraction(num, den)

    # ---------- 比较运算 ----------
    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        # 分母为正，可直接交叉相乘
        return self.numerator * other.denominator < other.numerator * self.denominator

    # ---------- 类型转换 ----------
    def __float__(self):
        return self.numerator / self.denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"
    
f1 = Fraction(1, 2)   # 1/2
f2 = Fraction(1, 3)   # 1/3

print(f1 + f2)        # 5/6
print(f1 - f2)        # 1/6
print(f1 * f2)        # 1/6
print(f1 / f2)        # 3/2
print(f1 == f2)       # False
print(f1 > f2)        # True
print(float(f1))      # 0.5
print(str(f1))        # "1/2"
print(repr(f1))       # "Fraction(1, 2)"