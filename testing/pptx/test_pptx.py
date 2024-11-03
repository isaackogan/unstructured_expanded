import json

from unstructured_expanded.partition.docx import partition_docx
from unstructured_expanded.partition.pptx.partition_pptx import partition_pptx

elements = partition_pptx(
    filename="Iguana.pptx",
    file=open("Iguana.pptx", "rb"),
)

data = []

for element in elements:
    data.append(element.to_dict())

with open("output_pptx.json", "w") as f:
    f.write(json.dumps(data, indent=4))