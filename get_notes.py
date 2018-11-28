import textract
import re
text = textract.process("/home/markroxor/Desktop/a.pdf")

for t in re.compile(b'Unknown Unknown\n\nPage ').split(text):
    note = re.compile(b'\n\n[0-9\(\)]+/[0-9\(\)]+/[0-9\(\)]+ [0-9\(\)]+:[0-9\(\)]+\n').split(t)
    page = note[0]

    try:
        page = int(page)
    except ValueError:
        continue

    content = note[1]
    content = re.compile(b'\n[0-9\(\)]+\n\n').split(content)[0]

    if content != b'':
        print (page , '-', content)
