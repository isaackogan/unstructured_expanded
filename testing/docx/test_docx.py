import json

from unstructured_expanded.partition.docx import partition_docx

elements = partition_docx(
    file=open("Leonie.docx", "rb"),
)

data = []

for element in elements:
    data.append(element.to_dict())

with open("output_docx.json", "w") as f:
    f.write(json.dumps(data, indent=4))