def test_widget_functions_as_expected():
    assert True

def test_widget_fails():
    assert True


def some_convenience_function():
    print('kiss my big ...')


def acumula(arrcumula):
    if len(arrcumula)==0:
        return arrcumula
    else:
        print(arrcumula[0])
        return acumula(arrcumula[1:])


def test_acumula():
    comales = [1,2,3,4,5,6,7]
    coletas = ['1','4',3,4,5,6,7,7,8,'a']
    testers = [comales,coletas]
    for x in testers:
        copa = acumula(x)
        print(copa)

test_acumula()