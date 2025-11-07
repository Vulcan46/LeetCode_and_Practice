def longest_unique_substr(s):
    l = r =0
    maxx = 0
    seq = set()
    while r<len(s):
        while s[r] in seq:
            seq.remove(s[l])
            l+=1
        seq.add(s[r])
        maxx = max(maxx,r-l+1)
        r+=1
    return maxx

word = "yeastblind"
print(longest_unique_substr(word))
