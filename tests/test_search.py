""" Test DuckDuckGo Searches 

-`test` always start name with test as pytest will look for it.
- Anytime pytest see word `test` with an argument `e.g browser`
- it will check arg name available on fixture `conftet.py` file
- And pass in whatever return for this arg `browser` to execute 
command in the test, once done it will return to conftest.py to quit. 

"""

import pytest
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage


@pytest.mark.parametrize('phrase', ['cat', 'duck', 'python language'])
def test_basicduckduckgo_search(browser, phrase):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)

    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user searches for phrase
    search_page.search(phrase)

    # Then the search result query is phrase
    assert phrase == result_page.search_input_value()

    # And the search result links pertain to phrase
    titles = result_page.result_link_titles()
    matches = [t for t in titles if phrase.lower() in t.lower()]
    assert len(matches) > 0

    # And the search result title contains phrase
    assert phrase in result_page.title()

