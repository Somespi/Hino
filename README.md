# Hino API Package - HAP
 unofficial API package for [Hino](https://hino.tk).
 
 <hr>
 
 # Docs
 
 ## Installation
 you can install this package by typing
 
 ```py
 $ pip install hino
 ```

There are 4 main methods to fetch the data: 
 
 `getshards()`
 `getclient()`
 `getbasics()`
 `gethandler()`

 simple code:
 ```py
 hino = Hino()
 print(hino.getclient("name"))
 
```
<hr>

## Variables

#### `hino.developers` returns a list of Hino's developers

#### `hino.partners` returns a list of Hino's partners

## Methods

### getbasics()

#### Arguments
info: str

#### returns
data as string data type

#### how to use it
you can get diffrent data by changing the value of `info` , `info` has 7 cases, if diffrent value were put, it will return `TypeError`
the 7 cases are:
- name - url - author
- license - version - website_api_version
- latecy

```py
hino = Hino()
hino.getbasics("license")
```
<hr>

### getshards()

#### Arguments
info: str
shardNum: int

#### returns
data as string data type

#### how to use it
you can get diffrent data for diffrent shards by changing the value of `info` and `shardNum` , `info` has 5 cases, if diffrent value were put, it will return `TypeError`.
the 5 cases are:
- name - version - users
- servers - type
each shard has a diffrent value of `info` to change it, you must change the `shardNum` to the shard number you want to fetch.
tip: if you left the `shardNum` blank and changed the value of `info` to *count* , it will return the shards count.


```py
hino = Hino()
hino.getshards("type",2)
```


```py
hino = Hino()
hino.getshards("count")
```
<hr>

### getclient()

#### Arguments
info: str

#### returns
data as string data type

#### how to use it
you can get diffrent data by changing the value of `info` , `info` has 6 cases, if diffrent value were put, it will return `TypeError`
the 6 cases are:
- name - banner - version
- color - color2 - ping

```py
hino = Hino()
hino.getclient("name")
```
<hr>

### gethandler()

#### Arguments
info: str

#### returns
data as string data type

#### how to use it
you can get diffrent data by changing the value of `info` , `info` has 7 cases, if diffrent value were put, it will return `TypeError`
the 7 cases are:
- name - description - version
- process - websocket - type 
- module

```py
hino = Hino()
hino.gethandler("description")
```
<hr>
