import json
import logging
from pathlib import Path
import yaml


from docling.backend.pypdfium2_backend import PyPdfiumDocumentBackend
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.datamodel.base_models import InputFormat
from docling.document_converter import (
    DocumentConverter,
    PdfFormatOption,
    WordFormatOption
)
from docling.pipeline.simple_pipeline import SimplePipeline
from docling.pipeline.standard_pdf_pipeline import StandardPdfPipeline
from docling_core.types.doc import ImageRefMode

# configure logging
logging.basicConfig(level=logging.INFO)
_log = logging.getLogger(__name__)

###   function

###   function


###   function
def main():
    input_paths = [
        Path(r"docs\fintepla_en")
    ]
    output_dir = "scratch"
    #convert_documents(input_paths,output_dir)

if __name__ == "__main__":
    main()

