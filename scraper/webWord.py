import requests
from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation


ans = {"word_counts": {u'computer': 0.0, u'doctoral': 0.0,
                       u'algorithms': 0.0, u'watson': 0.0}, "page_word_counts": {}}


def countWords(webPage):

    # We get the url
    r = requests.get(webPage)
    soup = BeautifulSoup(r.content)

    # We get the words within paragrphs
    text_p = (''.join(s.findAll(text=True))for s in soup.findAll('p'))
    c_p = Counter((x.rstrip(punctuation).lower()
                   for y in text_p for x in y.split()))

    # We get the words within divs
    text_div = (''.join(s.findAll(text=True))for s in soup.findAll('div'))
    c_div = Counter((x.rstrip(punctuation).lower()
                     for y in text_div for x in y.split()))

    # We sum the two countesr and get a list with words count from most to less common
    total = c_div + c_p
    list_most_common_words = total.most_common()

    print(webPage)
    ans["page_word_counts"][webPage] = sum([x[1] for x in total.items()])
    ans["word_counts"][u'computer'] += total[u'computer']
    ans["word_counts"][u'doctoral'] += total[u'doctoral']
    ans["word_counts"][u'algorithms'] += total[u'algorithms']
    ans["word_counts"][u'watson'] += total[u'watson']
    print('computer', total[u'computer'])
    print('doctoral', total[u'doctoral'])
    print('algorithms', total[u'algorithms'])
    print('watson', total[u'watson'])
    print(sum([x[1] for x in total.items()]))


countWords('https://cs.usu.edu')
countWords('https://cs.usu.edu/research/index')
countWords('https://cs.usu.edu/students/graduate/courses')
countWords('https://cs.usu.edu/news/index')
countWords('https://cs.usu.edu/people/faculty/index')


all_words = sum([v for k, v in ans["page_word_counts"].items()])
print(all_words)

print('tf computer', ans["word_counts"][u'computer'],
      ans["word_counts"][u'computer']/all_words)
print('tf doctoral', ans["word_counts"][u'doctoral'],
      ans["word_counts"][u'doctoral']/all_words)
print('tf algorithms', ans["word_counts"][u'algorithms'],
      ans["word_counts"][u'algorithms']/all_words)
print('tf watson', ans["word_counts"][u'watson'],
      ans["word_counts"][u'watson']/all_words)
