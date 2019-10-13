import pytest
import time

@pytest.mark.parametrize("wait_time", [5] * 20)
def test_slow(wait_time):
    time.sleep(wait_time)
    assert True
