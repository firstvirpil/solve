"""say_hello берет из локального файла conftest
 get_random_number берет из глобального файла conftest
 и на выводе получается
 tests/something/test_one.py::test_one Это фикструра в папке something
834

 """


def test_one(say_hello, get_random_number):
    assert 1 == 1,  "вроде да"
    print(get_random_number)

