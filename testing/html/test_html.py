import json

from unstructured.partition.auto import partition

elements = partition(
    file=open("page 21 Notes de cours - Éthique et I test.html", "rb"),
)

data = []

for element in elements:
    data.append(element.to_dict())

with open("output_html.json", "w") as f:
    f.write(json.dumps(data, indent=4))
