# strings: ordered , immutable, text representation

selam = "selam kayace"
print(f"{selam}")

# TypeError: 'str' object does not support item assignment
# selam[-1] = 'i' # strings are immutable  
# print(f"{selam}")
substring = selam[2:12]
print(f"substring: {substring}")
every2char = selam[::2]
print(f"every2char: {every2char}")
reverse = selam[::-1]
print(f"reverse: {reverse}")
for i in selam:
    print(i)
if "selam" in selam:
    print("aleykum selam")
else:
    print("merhaba")

msg = "    hello world    "
print(msg)
print("stripped ",msg.strip())
info = "Adnan Kayace"
print(f"upper: {info.upper()}")
print(f"lower: {info.lower()}")
print(f"startswith: {info.startswith('kaya')}")
print(f"endswith: {info.endswith('ce')}")
print(f"find: {info.find('Kaya')}")
print(f"find not found: {info.find('Kayaci')}")
print(f"count: {info.count('a')}")
print(f"not replace: {info.replace('Kayaci', 'KAYACE')}")
print(f"replace: {info.replace('Kayace', 'KAYACE')}")
msg = "this is my message to the world"
msg = msg.replace(" ","-")
print(f"msg: {msg}")
mlist = msg.split('-')
print(f"mlist: {mlist}")
newmsg = ' / '.join(mlist)
print(f"newmsg: {newmsg}")
print()
mlist = ['a'] * 10
print(f"mlist: {mlist}")
mstr = ' '.join(mlist)
print(f"mstr: {mstr}")
var = 3.14159
print("formatted {:.2f}".format(var))
