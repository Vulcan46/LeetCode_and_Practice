strs = ["ab","a"]
if not strs:
    print("")
prefix = strs[0]
for s in strs[1:]:
    while not s.startswith(prefix) and prefix:
        prefix = prefix[:-1]
    if not prefix:
        print("")
print(prefix)





