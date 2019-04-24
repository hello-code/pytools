''' count words frequncy'''''
from collections import Counter
import re
import os

article = "article.txt"
omit = "omitwords.txt"

with open(article, encoding='UTF-8') as f:
    file_text = f.read().lower()

omit_text = []
with open(omit) as f:
    for line in f:
        omit_text.append(line.strip('\n'))

words = re.findall(r'\w+', file_text)
words[:] = [x for x in words if x not in omit_text]
print("total words: ", len(words))

# wirte in file
os.remove("words_counter.txt")
c = Counter(words)
with open('words_counter.txt', 'a', encoding='UTF-8') as f:
    for k, v in c.most_common():
        if k.isnumeric() is False:
            if len(k) > 3:
                f.write("{} {}\n".format(k, v))
