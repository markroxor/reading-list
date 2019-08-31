import textract
import re
import sys

print('Reading file..')
text = textract.process(sys.argv[1])
print('Read file.')

with open(sys.argv[2], 'w') as f:
    f.write('\n- author: Mitnick, Kevin')
    f.write('\n  title: The Art Of Invisibility.')
    f.write('\n  finished: 2019-08-31')
    f.write('\n  rating: 4.8')
    f.write('\n  quotes:')
    tex = ''
    p = ''
    for t in re.compile(b'Mohit Rathore').split(text):
        t = t.split(b'\n')[2:-1]
        t = b' '.join(t).decode('utf8').split()

        if 'Page' not in t[0]:
            continue
        page = t[1]
        content = ' '.join(t[4:]).replace(':', '')
        a = "\n        - page: " +  "\"" + page + "\"\n"
        b = "          content: " + content

        # if len(content) < 100000 and len(content) > 2:
        f.write(a+b)

        # tex = ''