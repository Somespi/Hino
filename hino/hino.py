import requests
import json 

class Hino:
    res = requests.get("https://hino.tk/api", stream=True)
    if res.status_code != 200:
        raise ValueError(
            "API is not working. status code :" + str(res.status_code))
    else:
        api = json.loads(res.content)["api"]
        others = json.loads(res.content)
        developers = others["client"]["developers"]
        partners = others["client"]["partners"]

        def getbasics(self, info: str) -> str:
            """Return basic info about Hino"""

            info = info.lower().replace(" ", "")
            for i in list(self.api.keys())[:-1]:
                if i in info:
                    return self.api[i]
            else:
                raise TypeError(f"\"{info}\" is not defined in \"Basics\".")

        def getshards(self, info: str, shardnum: int = None) -> str:
            """Return shards info about Hino"""
            info = info.lower().replace(" ", "")
            if shardnum is None and info == "count":
                return self.api["shards"]["count"]
            elif shardnum and info:
                if int(self.api["shards"]["count"]) >= shardnum:
                    keywords = list(self.api["shards"]
                                    [f"shard{shardnum}"].keys())
                    for x in keywords:
                        if x in info:
                            return str(self.api["shards"][f"shard{shardnum}"][x])
                    else:
                        raise TypeError(
                            f"\"{info}\" is not defined in \"shards Info\".")
                else:
                    raise TypeError(f"\"Shard{shardnum}\" No such shard.")

        def gethandler(self, info: str) -> str:
            """Return handler info about Hino"""
            info = info.lower().replace(" ", "")
            for i in list(self.api["shards"]["handler"].keys()):
                if i in info:
                    return str(self.api["shards"]["handler"][i])
            else:
                raise TypeError(f"\"{info}\" is not defined in \"handler\".")

        def getclient(self, info: str) -> str:
            """Return client info about Hino"""
            info = info.lower().replace(" ", "")
            for i in list(self.others["client"].keys())[:-2]:
                if i in info:
                    return str(self.others["client"][i])
            else:
                raise TypeError(f"\"{info}\" is not defined in \"client\".")
