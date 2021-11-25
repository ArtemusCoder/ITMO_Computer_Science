import yaml
import json
with open("origin.yaml", 'r', encoding='UTF-8') as yaml_in, open("json_library.json", "wt", encoding="UTF-8") as json_out:
    yaml_object = yaml.safe_load(yaml_in)
    json.dump(yaml_object, json_out, ensure_ascii=False)