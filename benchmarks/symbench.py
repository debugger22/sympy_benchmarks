#!/usr/bin/env python
from __future__ import print_function, division
from sympy.core.compatibility import xrange

from random import random
from sympy import factor, I, Integer, pi, simplify, sin, sqrt, Symbol, sympify
from sympy.abc import x, y, z
from timeit import default_timer as clock


class TimeSymbench:
    # originally from sympy/benchmarks/bench_symbench.py

    def time_bench_R1():
        "real(f(f(f(f(f(f(f(f(f(f(i/2)))))))))))"
        def f(z):
            return sqrt(Integer(1)/3)*z**2 + I/3
        e = f(f(f(f(f(f(f(f(f(f(I/2)))))))))).as_real_imag()[0]

    def time_R2():
        "Hermite polynomial hermite(15, y)"
        def hermite(n, y):
            if n == 1:
                return 2*y
            if n == 0:
                return 1
            return (2*y*hermite(n-1, y) - 2*(n-1)*hermite(n-2, y)).expand()

        a = hermite(15, y)

    def time_R3():
        "a = [bool(f==f) for _ in range(10)]"
        f = x + y + z
        a = [bool(f == f) for _ in range(10)]

    def time_R5():
        "blowup(L, 8); L=uniq(L)"
        def blowup(L, n):
            for i in range(n):
                L.append( (L[i] + L[i + 1]) * L[i + 2] )

        def uniq(x):
            v = list(set(x))
            v.sort()
            return v
        L = [x, y, z]
        blowup(L, 8)
        L = uniq(L)

    def time_R6():
        "sum(simplify((x+sin(i))/x+(x-sin(i))/x) for i in xrange(100))"
        s = sum(simplify((x + sin(i))/x + (x - sin(i))/x) for i in xrange(100))

    def time_R7():
        "[f.subs(x, random()) for _ in xrange(10**4)]"
        f = x**24 + 34*x**12 + 45*x**3 + 9*x**18 + 34*x**10 + 32*x**21
        a = [f.subs(x, random()) for _ in xrange(10**4)]

    def time_R8():
        "right(x^2,0,5,10^4)"
        def right(f, a, b, n):
            a = sympify(a)
            b = sympify(b)
            n = sympify(n)
            x = f.atoms(Symbol).pop()
            Deltax = (b - a)/n
            c = a
            est = 0
            for i in range(n):
                c += Deltax
                est += f.subs(x, c)
            return est*Deltax

        a = right(x**2, 0, 5, 10**4)

    def time_R10():
        "v = [-pi,-pi+1/10..,pi]"
        def srange(min, max, step):
            v = [min]
            while (max - v[-1]).evalf() > 0:
                v.append(v[-1] + step)
            return v[:-1]
        v = srange(-pi, pi, sympify(1)/10)

    def time_R11():
        "a = [random() + random()*I for w in [0..1000]]"
        a = [random() + random()*I for w in range(1000)]
        a.sort()

    def time_S1():
        "e=(x+y+z+1)**7;f=e*(e+1);f.expand()"
        e = (x + y + z + 1)**7
        f = e*(e + 1)
        f = f.expand()