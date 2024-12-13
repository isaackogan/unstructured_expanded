import json

from unstructured_expanded.partition.pdf.partition_pdf import partition_pdf

elements = partition_pdf(
    file=open("Syllabus_HUMA.pdf", "rb"),
    extract_images_in_pdf=True,
    extract_image_block_to_payload=True,
    extract_image_block_types=["Image"]
)

data = []

for element in elements:
    data.append(element.to_dict())

with open("output_pdf.json", "w") as f:
    f.write(json.dumps(data, indent=4))
