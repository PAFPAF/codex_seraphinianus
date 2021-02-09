import fitz

pdffile = "pics/Codex_Seraphinianus.pdf"
doc = fitz.open(pdffile)

for i in doc:
    if int(str(i).split(' ')[1]) == 0:
        pass
    else:
        pix = i.getPixmap()
        output = "pics/" + str(i).split(' ')[1] +".png"
        pix.writePNG(output)