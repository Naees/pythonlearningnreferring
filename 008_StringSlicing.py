# 8. String slicing

# slicing = "create a substring by extracting elements from another string indexing[] or slice() [start:stop:step]"

name = "Naees Er"

firstname = name[:4]                   # [start:4]
lastname = name[5:]                    # [5:end]
funkyname = name[::1]                  # [start:end:increments of 1]
funkynametwo = name[::3]               # [start:end:increments of 3]          
reversedname = name[::-1]              # [start:end:reversing in increments of 1]

print(firstname)
print(lastname)
print(funkyname)
print(funkynametwo)
print(reversedname)

websiteone = "https://google.com"
websitetwo = "https://youtube.com"

slice = slice(8,-4)
print(websiteone[slice])
print(websitetwo[slice])
