import json
def task() -> float:
    with open('input.json', 'r') as j:
data = json.load(j)
total = sum(d["score"] * d["weight"] for d in data)
return rouns(total, 3)
print(task())
