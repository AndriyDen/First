cat = {}
info = {"status": "vaccinated", "breed": True}
cat.update(info)
cat.update({"nick": "Simon", "age": 7, "characteristics": ["crazy", "can kill"]})

print(cat)
print(cat.get("age"))