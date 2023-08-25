from pathlib import Path

from PyPDF2 import PdfReader, PdfWriter


ROOT_FOLDER = Path(__file__).parent
ORIGINALS_FOLDER = ROOT_FOLDER / 'pdf_originals'
NEW_FOLDER = ROOT_FOLDER / 'new_files'

RELATORIO_BACEN = ORIGINALS_FOLDER / 'R20230519.pdf'

NEW_FOLDER.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO_BACEN)

page0 = reader.pages[0]
image0 = page0.images[0]

with open(NEW_FOLDER / image0.name, 'wb') as fp:
    fp.write(image0.data)


writer = PdfWriter()
writer.add_page(page0)

with open(NEW_FOLDER / 'page0.pdf', 'wb') as file:
    writer.write(file)
