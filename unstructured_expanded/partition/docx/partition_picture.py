from typing import Iterator

from docx.text.paragraph import Paragraph
from unstructured.documents.elements import Image
from unstructured.partition.docx import PicturePartitionerT, DocxPartitionerOptions

from unstructured_expanded.shared.models import ExpandedImage
from unstructured_expanded.shared.tools import extract_desc


class DocxPicturePartitioner(PicturePartitionerT):

    namespaces: dict[str, str] = {
        'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
        'wp': 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing',
        'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
        "pic": 'http://schemas.openxmlformats.org/drawingml/2006/picture'
    }

    @classmethod
    def iter_elements(
            cls,
            paragraph: Paragraph,
            opts: DocxPartitionerOptions
    ) -> Iterator[Image]:

        # Extract 'blips' in the paragraph which will hold image elements
        # noinspection PyProtectedMember
        blips = paragraph._element.findall('.//a:blip', namespaces=cls.namespaces)

        # Iterate blips
        for blip in blips:

            # Extract the relationship ID
            r_id = blip.attrib['{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed']

            # Yield an image with the blob and descriptive text word generates
            yield ExpandedImage.load(
                image_bytes=opts.document.part.related_parts[r_id].blob,

                # For docx, the base tag is pic, i.e. pic:nvPicPr. For pptx, it's p:nvPicPr
                # As a result, namespaces also differ
                desc=extract_desc(blip, base_tag="pic", namespaces=cls.namespaces)
            )


