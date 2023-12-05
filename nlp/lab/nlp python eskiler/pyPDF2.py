from PyPDF2 import PdfReader

reader = PdfReader("NLP_re_hwk.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"
    print(text)
