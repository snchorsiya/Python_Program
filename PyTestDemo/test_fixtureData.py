import pytest

from BasceClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):

    def test_editProfile(self, dataLoad):
        log = self.getLogger()
        log.info(dataLoad[0])
        # print(dataLoad[0])
        log.info(dataLoad[1])
        log.info(dataLoad[2])
        # print(dataLoad[1])
        # print(dataLoad[2])


