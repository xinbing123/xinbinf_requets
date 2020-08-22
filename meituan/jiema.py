# *-* coding:utf8 *-*
import zlib
import json
import base64
# d="eJxVjstuqzAURf/F04uCMU9H6iBKCM9AIaWk96oDoEkwBGiwidNU/fe6aju40pH2PuuswXkHo/cC5gqEGEIJXPYjmANlBmcGkACj4qIbqgFVC6uabkig+p8Zpi6Bcnxcgfk/BRmmpOjK8xdJBRDEgpKJ4LP0XQ0sKtLEfDmeUEDN2Cudy3JV01m3J2wq+lk1dLLotCayeAIIt3sQrsj2J4ufZL/7RnwtXEqOvWh7n5+aCkW8WST17lJra+Y93JPdwV5Wj21YBc6S+yi1S/vQWNmQ8cFGhbM086d2ovEK3jcI97zlfLBuTekd/yzyLbraVscO2JRlPfP0ZRKZruskPSd5o5GmrfCrW8MnNWj8l8C/aptQ9brwr1IeKMQZ2XrZlWF3VyvrmKUjydLayWnXwzLonUWxDU3vEp0CzZU3eV15A02n3O6tuHpLT5yGq3g6nxViFsUNF8ZxMqyRcLQfo/N0iymOkwgma79L7u7AxycfSoxF"
# d="eJxVjk1vqkAUhv/LbCUyzOiA7pCJAgqKFKVtugBEZuRDYaCaNve/32naLpqc5H3Pc57F+QSdcwJzDcIZhAp4zzswB9oYjglQQC/kZUrw1CATQjAxFJD9ZROEFZB2BwrdmrxoiREFw8vZF9hJIYkBFR/BN+a5kJiuayPlyHKkA1vc3MVfVjIlxnfN+SJpxdq1V2QXjqnwCSLd+kq7M8ieTn+x/d09+LV3Bi0a23L1Xlwiu7xczYLnKna5PEGy7gKU8ZAts84XvNsk9zG6l0xTBUtOphYv0fhDPp100sodZcysuERZ8CZ2OUYPjK3aKnXqOR2oZLDpoo2tc5lnvbcOd9diyEJsRFVXrBDZbnYm7p+LxhN2wsodNZsZueG4JXX/sbDMSjzb2hxfL3tb6uj1+rHxew6JC2MppYy6z1PP2i00Zbgxa+ZZDcI/0w3DyV7Dn7TFOs3bEph48JfXxUR38I/V1892toloD//4DIT+KaQ=="
#
# token =d .encode()
# print(token)
# token = base64.b64decode(token)
# print(token)
# # # #
# token = zlib.decompress(token)
# token = token.decode()
# print(token)
# token = json.loads(token)
# print(token)
# print('=================================')
# # sign ='eJxdj11vgjAUhv+K6e0WKEiZmOxCow4tCioC27ILRYQqVGbLhyz776NeuGwXTZ73OW+bni9wme5Bv6NAaED42AFldGkjUCQo6aDNnIkp0rvI0JGmKprWyvCfVQ1hdxdv1Op3xVDblxTYgx83uxLyr70nTSRVE+dWnoouSDjPWV+Ww4RJWUR4saVSeM7klllCZPEvIOqZK+qCTnfa3on/urnYSVxjJKaCo1nluReGq2awfED1PDmSsj7b5ukzXRY0sMIC7UmWkkS2UW4ahzeEx2ZMXits8+A6hLZhWk/VeOd7h8UQUTR3lF6Bg+rsD12O6TKBg169ak6Y4XRCD7UPkbuysH4smoNzrBEPzmaaY6VIqDrx17NyQhcO7RYGDkjeS0ioz5qZvb/mFouP8XYxz5TSm0Z8o2svGyvWULNe8IhWI3lXOeXmGXz/ABxDhEs='
#
# sign = token.get('sign')
# sign = sign.encode(encoding="utf-8", errors="strict")
# print(sign)
# sign = base64.b64decode(sign)
# print(sign)
# sign = zlib.decompress(sign)
# print(sign)
# sign = sign.decode()
# print(sign)


