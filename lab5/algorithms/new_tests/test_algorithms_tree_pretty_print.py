# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import algorithms.tree.pretty_print as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "6c'qES(m"
    module_0.tree_print(str_0)


def test_case_1():
    bytes_0 = b"u3\xc8D\xf4\xc2?\xf4\xb3z\xb3\\\xa7\xa7.\xcd\xc1\x8dh\xdc"
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
    var_0 = module_0.tree_print(dict_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.tree_print(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "w{o1wx 6`8I ~Sc"
    dict_0 = {str_0: str_0}
    var_0 = module_0.tree_print(dict_0)
    module_0.tree_print(var_0)
