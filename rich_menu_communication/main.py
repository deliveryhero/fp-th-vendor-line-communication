import requests

list = ["U2b9495e231b925da2ed4163beeef6dad", "U2b9495e231b925da2ed4163beeef6dad"]

for i in list:
    # print(i)
    url = 'https://api.line.me/v2/bot/user/{}/richmenu/richmenu-55b2f4bf95dfb0c75d39f109075e4690'.format(i)
    myobj = {'Authorization': 'Bearer {HSQDSPQP7n5J9aSDWP1MXh9cck42P6yge9PIYyk8ITEIyNnb6MPu7J1mILKH62XCd5FqkbmWHSqV8TuvdgF/AV3uqdphWw4t3Bk9FDVNmDFn0s0hRa4jKV1yxb5acO4pgFLxe2CFkU1/CylAUNr+RAdB04t89/1O/w1cDnyilFU=}'}
    x = requests.post(url, headers = myobj)
    # print(x)