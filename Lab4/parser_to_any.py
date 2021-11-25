yaml_file = open("origin.yaml", 'r', encoding="UTF-8")
text = yaml_file.read()[3:]
text = text.replace("\n", "")
elements_raw = text.split("  ")
elements = [i for i in elements_raw if i != '']
main = elements[0][:-1]
json_dict = {main: []}
for thing in elements[1:]:
    if thing[0] == "-" and thing[-1] == ":":
        now_key = thing[2:-1]
        json_dict[main].append({now_key: []})
    elif thing[0] == "-":
        json_dict[main][-1][now_key].append(thing[3:-1])
    elif thing[-1] == ":":
        now_key = thing[:-1]
        json_dict[main][-1][now_key] = []


choice = input("Введите название файла (Расширения: CSV, TSV, WML): ")
if choice.split('.')[1] == "csv" or choice.split('.')[1] == "tsv":
    delimiter = ";" if choice.split('.')[1] == "csv" else "\t"
    csv_or_tsv_text = ""
    csv_or_tsv_text += delimiter.join(json_dict[main][0].keys()) + '\n'
    for lesson in json_dict[main]:
        all = []
        for value in lesson.values():
            all.append(', '.join(value))
        csv_or_tsv_text += delimiter.join(all) + "\n"
    f = open(choice, "w", encoding="UTF-8")
    f.write(csv_or_tsv_text)
    f.close()
