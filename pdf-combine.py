import sys
from PyPDF4 import PdfFileMerger

sys.argv.pop(0)
merger = PdfFileMerger()

for pdf in sys.argv:
    merger.append(pdf)

merger.write('combined.pdf')
merger.close()
