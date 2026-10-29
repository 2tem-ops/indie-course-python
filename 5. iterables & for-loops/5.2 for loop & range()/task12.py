for i in range(1, n := int(input()) + 1):
    if (s:=input().lower()).find("рок") > -1: print(i, s.find("рок") + 1)