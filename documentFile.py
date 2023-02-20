import aspose.words as aw

doc = aw.Document()
builder = aw.DocumentBuilder(doc)

builder.write("hei")
doc.save("test.docx")