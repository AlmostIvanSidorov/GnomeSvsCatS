from lprogram import devision_local
import pytest


@pytest.mark.parametrize("a, b, result", [(10, 5, 2)])
def test_dev(a, b, result):
    assert devision_local(a, b) == result

