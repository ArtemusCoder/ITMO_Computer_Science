import re
import time
start_time = time.time()

yaml_file = open("origin.yaml", 'r', encoding="UTF-8")
text = yaml_file.read()[3:]
text = re.sub("\n", "", text)
elements_raw = re.split("  ", text)
elements = [i for i in elements_raw if i != '']
main = elements[0][:-1]
json_dict = {main:[]}
for thing in elements[1:]:
    if re.match(r"-.*:$", thing):
        now_key = thing[2:-1]
        json_dict[main].append({now_key:[]})
    elif re.match(r"-.*", thing):
        json_dict[main][-1][now_key].append(thing[3:-1])
    elif re.match(r'.*:$', thing):
        now_key = thing[:-1]
        json_dict[main][-1][now_key] = []

res = str(json_dict)
res = re.sub(r"'", '"', res)
with open("json_regular.json", "w", encoding="UTF-8") as f:
    f.write(res)
print("--- %s seconds ---" % (time.time() - start_time))
