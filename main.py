def fun(a, b, c):
    delta = b**2-4*a*c
    if delta > 0:
        x1=(-b-delta**0.5)/(2*a)
        x2=(-b+delta**0.5)/(2*a)
        print(f'Dwa rozne pierwiastki x1={x1}, x2={x2}')
        return

    if delta == 0:
        x0=-b/(2*a)
        print(f'Pierwiastek podwojny: x0={x0}')
        return

    deltaz = abs(delta)
    xr=-b/(2*a)
    xi=(deltaz**0.5)/(2*a)
    print(f'Dwa pierwiastki zespolone: x1={xr}+{xi}i, x2={xr}-{xi}i')
    return

fun(-1,2,2)