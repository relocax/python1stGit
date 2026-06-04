capitals = {"USA" : "WASHINGTON D.C",
            "India" : "New Delhi",
            "China" : "Bejing",
            "Russia" : "Moscow"
            }

# print(dir(capitals))
# print(help(capitals))
# capitals.update({"Germany" : "Berlin"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()
keys = capitals.keys()
print(keys)
if capitals.get("China"):
    print("The capital exists")
print(capitals.get("USA"))
values = capitals.values()
print(values)
