"""
wikiAPI.py

uses wikipedia apa from mediaWiki to extract university information from wikipedia
"""
import wikipediaapi

def get_summary(name):
    """takes the title of university and returns a wiki summery"""
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page_py = wiki_wiki.page(name)
    if page_py.exists():
        return page_py.summary
    else:
        return 'Wiki summary not found'