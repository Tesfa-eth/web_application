"""
wikiAPI.py

uses wikipedia apa from mediaWiki to extract university information from wikipedia
"""
import wikipediaapi

def get_summary(name):
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page_py = wiki_wiki.page(name)
    if wiki_wiki.page('NonExistingPageWithStrangeName'):
        return 'Wiki summary not found'
    else:
        return page_py.summary