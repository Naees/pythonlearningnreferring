# set = collection which is unordedred, unindexed. SNo duplicate values

dogs = {"German Shepherd", "Bulldog", "Labrador Retriever", "Golden Retriever"}
cats = {"Siamese cat", "British Shorthair", "Maine Coon", "Persian Cat"}

print("Before applying methods:")
for x in dogs:
    print(x)
print()

dogs.add("Alaskan Malamute")
print("List after adding Alaskan Malamute:")
for x in dogs:
    print(x)
print()


dogs.remove("German Shepherd")
print("List after remove German Shepherd:")
for x in dogs:
    print(x)
print()


dogs.clear()
print("List after applying the clear method:")
for x in dogs:
    print(x)
print()


dogs.update(cats)
print("List after updating the DOGS set with CATS: ")
for x in dogs:
    print(x)
print()

# dogs = {"German Shepherd", "Bulldog", "Labrador Retriever", "Golden Retriever"}
# Set will not union duplicates, uncomment the set on line 38 to try out the union with a different test case
unionlist = dogs.union(cats)
print("List after UNION/combining both sets ")
for x in unionlist:
    print(x)
print()