
def GET_HANDLER(info: str) -> str:
            """Return handler info about Hino"""
            from hinoapi import api
            info = info.lower().replace(" ", "")
            for i in list(api["shards"]["handler"].keys()):
                if i in info:
                    return str(api["shards"]["handler"][i])
            else:
                raise TypeError(f"\"{info}\" is not defined in \"handler\".")
