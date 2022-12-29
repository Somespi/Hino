class Hino:
    from hinoapi import res, client
    if res.status_code != 200:
        raise ValueError(
            "API is not working. status code :" + str(res.status_code))
    else:
        developers = client["developers"]
        partners = client["partners"]

        def getbasics(self, info: str) -> str:
            """Return basic info about Hino"""
            from getBasics import GET_BASICS
            return GET_BASICS(info)

        def getshards(self, info: str, shardnum: int = None) -> str:
            """Return shards info about Hino"""
            from getShards import GET_SHARDS
            return GET_SHARDS(info, shardnum)

        def gethandler(self, info: str) -> str:
            """Return handler info about Hino"""
            from getHandler import GET_HANDLER
            return GET_HANDLER(info)

        def getclient(self, info: str) -> str:
            """Return client info about Hino"""
            from getClient import GET_CLIENT
            return GET_CLIENT(info)
