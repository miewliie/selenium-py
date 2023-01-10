""" Test DuckDuckGo Searches 

-`test` always start name with test as pytest will look for it.
- Anytime pytest see word `test` with an argument `e.g browser`
- it will check arg name available on fixture `conftet.py` file
- And pass in whatever return for this arg `browser` to execute 
command in the test, once done it will return to conftest.py to quit. 

"""


from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage


def test_basicduckduckgo_search(browser):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    PHRASE = "duck"

    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user searches for "duck"
    search_page.search(PHRASE)

    # Then the search result title contains "duck"
    assert PHRASE in result_page.title()

    # And the search result query is "duck"
    assert PHRASE == result_page.search_input_value()

    # And the search result links pertain to "duck"
    for title in result_page.result_link_titles():
        assert PHRASE.lower() in title.lower()

    raise Exception("Incomplete Test")