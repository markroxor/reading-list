import textract
import re
import sys

print('Reading file..')
text = textract.process(sys.argv[1])
print('Read file.')

with open(sys.argv[2], 'a') as f:
    f.write('\n- author: Harari, Yuval Noah')
    f.write('\n  title: A Brief History of Humankind, Sapiens.')
    f.write('\n  finished: 2019-05-15')
    f.write('\n  rating: 4.2')
    f.write('\n  quotes:')
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
        content = ' '.join(tex.replace(':', '').split()[:-2])
        a = "\n        - page: " +  "\"" + page + "\"\n"
        b = "          content: " + content

        if len(content) < 100000 and len(content) > 2:
            f.write(a+b)

        tex = ''