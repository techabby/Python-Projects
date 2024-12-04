import PyPDF2 as pp

PDF_files = ["/home/abby/Documents/Projects/Pyhton Intermediate Projects/3. PDF Merger/1.pdf",
            "/home/abby/Documents/Projects/Pyhton Intermediate Projects/3. PDF Merger/2.pdf"]

merge = pp.PdfMerger()

for filename in PDF_files:
    PDF_file = open(filename, "rb")
    PDF_reader = pp.PdfReader(PDF_file)
    merge.append(PDF_reader)

PDF_file.close()
merge.write("/home/abby/Documents/Projects/Pyhton Intermediate Projects/3. PDF Merger/Merged.pdf")
