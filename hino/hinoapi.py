res = requests.get("https://hino.tk/api", stream=True)
api = json.loads(res.content)["api"]
client = json.loads(res.content)["client"] 
