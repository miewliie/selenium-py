""" Test DuckDuckGo Searches 

-`test` always start name with test as pytest will look for it.
- Anytime pytest see word `test` with an argument `e.g browser`
- it will check arg name available on fixture `conftet.py` file
- And pass in whatever return for this arg `browser` to execute 
command in the test, once done it will return to conftest.py to quit. 

"""

def test_basicduckduckgo_search(browser):

    # Given the DuckDuckGo home page is displayed
    # TODO

    # When the user searches for "duck"
    # TODO

    # Then the search result title contains "duck"
    # TODO

    # And the search result query is "duck"
    # TODO

    # And the search result links pertain to "duck"
    # TODO

    raise Exception("Incomplete Test")