def getclient(info: str) -> str:
            """Return client info about Hino"""
            from hinoapi import api
            info = info.lower().replace(" ", "")
            for i in list(client.keys())[:-2]:
                if i in info:
                    return str(client[i])
            else:
                raise TypeError(f"\"{info}\" is not defined in \"client\".")
