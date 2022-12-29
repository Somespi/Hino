from hinoapi import api

def GET_SHARDS(info: str, shardnum: int = None) -> str:
            """Return shards info about Hino"""

            info = info.lower().replace(" ", "")
            if shardnum is None and info == "count":
                return api["shards"]["count"]
            elif shardnum and info:
                if int(api["shards"]["count"]) >= shardnum:
                    keywords = list(api["shards"][f"shard{shardnum}"].keys())
                    for x in keywords:
                        if x in info:
                            return str(api["shards"][f"shard{shardnum}"][x])
                    else:
                        raise TypeError(
                            f"\"{info}\" is not defined in \"shards Info\".")
                else:
                    raise TypeError(f"\"Shard{shardnum}\" No such shard.")
