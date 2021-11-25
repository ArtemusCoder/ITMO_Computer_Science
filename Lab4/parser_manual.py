import time
start_time = time.time()

yaml_file = open("origin.yaml", 'r', encoding="UTF-8")
text = yaml_file.read()[3:]
text = text.replace("\n", "")
elements_raw = text.split("  ")
elements = [i for i in elements_raw if i != '']
main = elements[0][:-1]
json_dict = {main: []}
print(elements)
for thing in elements[1:]:
    if thing[0] == "-" and thing[-1] == ":":
        now_key = thing[2:-1]
        json_dict[main].append({now_key: []})
    elif thing[0] == "-":
        json_dict[main][-1][now_key].append(thing[3:-1])
    elif thing[-1] == ":":
        now_key = thing[:-1]
        json_dict[main][-1][now_key] = []

res = str(json_dict)
res = res.replace("'", '"')
with open("json_manual.json", "w", encoding="UTF-8") as f:
    f.write(res)
print("--- %s seconds ---" % (time.time() - start_time))
