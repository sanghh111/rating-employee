from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT,WD_ALIGN_VERTICAL
document  = Document()


table = document.add_table(1, 12)
# table.alignment = WD_TABLE_ALIGNMENT.CENTER
hdr_cell =  table.rows[0].cells

hdr_cell_merge = hdr_cell[0]
for counter in range(1,len(hdr_cell)):
    hdr_cell_merge= hdr_cell_merge.merge(hdr_cell[counter])
hdr_cell_merge.alignment = WD_ALIGN_VERTICAL.CENTER


hdr_cell_merge.text = "Skill Sheet(Soft Engineer)"
document.save('demo.docx')
