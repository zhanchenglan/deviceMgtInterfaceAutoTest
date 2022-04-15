"""
Copyright @2022-01-15 Mobiledrive All Rights Reserved

author : xiaolong.song
"""
from src.main.environment import Environment


class DEVICEMGT(Environment):

    def dev(self):
        pass

    def test(self):
        return DEVICEMGT(
            url="http://121.41.109.132:20197/",
            client_id="console_911427",
            client_secret="Fih793987",
            grant_type="password",
            usertype="6357376",
            username="admin",
            password="Fih123456"
        )

    def pre(self):
        return DEVICEMGT(
            url="http://",
            client_id="console_911427",
            client_secret="Fih793987",
            grant_type="password",
            usertype="6357376",
            username="admin",
            password="Fih123456"
        )

    def prd(self):
        pass

    def aws(self):
        pass
