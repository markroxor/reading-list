import urllib2

#get page source
user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
headers = { 'User-Agent' : user_agent }
req = urllib2.Request('https://www.goodreads.com/review/list/57207853-mohit-rathore?shelf=to-read', None, headers)
response = urllib2.urlopen(req)
page = response.read()
response.close()

page = page.split("\n")
print page

f=open('./data/to-read.yaml', 'w+')

for i,words in enumerate(page):
    #get book title
    if "title\"><label>title</label><div" in words:
        f.write("- author: "+words.split("class=\"value\">")[1].split("\"")[1].replace("#","")+"\n")
    #get book author
    elif "<td class=\"field author\"><label>author</label><div class=\"value\">" in words:
        f.write("  title: "+words.split("<a")[-1].split("</a>")[0].split("\">")[1]+"\n")

#close io stream
f.close()
