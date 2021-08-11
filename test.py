from collections import Counter
import liwc
import re
parse, category_names = liwc.load_token_parser('LIWC2007_English100131.dic')

print('no. categories:', len(category_names))


def tokenize(text):
    # you may want to use a smarter tokenizer
    for match in re.finditer(r'\w+', text, re.UNICODE):
        yield match.group(0)


gettysburg = '''It was a big company so luckily I didn't have to see him all the time, but when I did, he again acted as though I didn't exist. I tried to talk to him and update him on the pregnancy, and ask him to be involved for our child's sake, and he literally stared right through me without saying a word. 3 months after our daughter was born, I texted him and told him he was missing out on the most amazing person in this world, and how it wasn't fair to her. To my surprise, he wrote back and wanted to see her. He apologized, said he had changed and within a couple of months, we were engaged.'''.lower()

gettysburg_tokens = tokenize(gettysburg)

gettysburg_counts = Counter(
    category for token in gettysburg_tokens for category in parse(token))
print(gettysburg_counts)
print(len(gettysburg_counts))
