most = input()
ebreszto = input()
nap = 0
ebresztes = most + ebreszto
a = True
while a:
    if(ebresztes > 24):
        ebresztes -= 24
        nap += 1
    else:
        a = False
        
print(ebresztes)
