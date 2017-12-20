
import pytest


class TestCheck(object):

    @pytest.mark.usefixtures("driver_landing")
    def test_check(self):
        print("WORK !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1")