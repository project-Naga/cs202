# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import algorithms.strings.count_binary_substring as module_0


def test_case_0():
    str_0 = "`Mk0@J"
    var_0 = module_0.count_binary_substring(str_0)
    assert var_0 == 5


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 3984
    module_0.count_binary_substring(int_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "\n    :type n: int\n    :rtype: bool\n    "
    var_0 = module_0.count_binary_substring(str_0)
    assert var_0 == 28
    module_0.count_binary_substring(var_0)
