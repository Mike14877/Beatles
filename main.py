# Beatles

beatles = []
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
len_beatles = len(beatles)
print("Step 1:", beatles)

for x in range(1):
    beatles.append("StuSutcliffe")
    beatles.append("Pete Best")
print("Step 2:", beatles)

del beatles[3]
del beatles[3]

beatles.insert(3, "Ringo Starr")
print("Step 3:", beatles)
