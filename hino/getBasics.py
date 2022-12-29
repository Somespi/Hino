
def getbasics(info: str) -> str:
            """Return basic info about Hino"""
	    from hinoapi import api
            info = info.lower().replace(" ", "")
            for i in list(api.keys())[:-1]:
                if i in info:
                    return api[i]
            else:
                raise TypeError(f"\"{info}\" is not defined in \"Basics\".")
