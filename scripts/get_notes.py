import textract
import re
text = textract.process("/Users/mark/Downloads/Archive/Dalio - 2007 - Principles-annotated.pdf")

with open('a.txt', 'w') as f:
    tex = ''
    p = ''
    for t in re.compile(b'Mohit Rathore').split(text):
        t = t.split(b'\n')[2:-1]
        t = b' '.join(t).decode('utf8').split()
        tex = tex + ' ' + " ".join(t)

        if len(t) < 2 or 'Page' not in t[-2]:
            if len(t) >1:
                print(t[-2])
            continue

        page = t[-1]
        a = "\n- page: " +  "\"" + page + "\"\n"
        b = " content: " + tex
        f.write(a+b)
        tex = ''