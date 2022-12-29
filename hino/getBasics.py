from hinoapi import api

def getbasics(info: str) -> str:
            """Return basic info about Hino"""

            info = info.lower().replace(" ", "")
            for i in list(api.keys())[:-1]:
                if i in info:
                    return api[i]
            else:
                raise TypeError(f"\"{info}\" is not defined in \"Basics\".")
