# selenium + python
Course at TAU by Andrew Knight: https://testautomationu.applitools.com/selenium-webdriver-python-tutorial/

Documentation in my versions:
1. Install python (python 3)
2. Install pipenv (pipenv -- version)
    1. `pip3 install pipenv`
3. Then, clone/create project on git.
    1. Download Chrome Driver 
        * Open it
        * Move to bin : `mv current/chromedriver /usr/local/bin` to bin.
    2. Download Firefox Driver (geckodriver)
        * Open it
        * Move to bin : `mv current/geckodriver /usr/local/bin` to bin. 
4. Open project in VS Code.
5. Install selenium using pipenv (creates and manages a virtualenv for the projects).
    1. `pipenv install selenium `
    2. `pipenv install pytest`
6. Create `conftest.py` file for config fixture.
    1. Create web driver instance etc. 
    2. Then always QUIT the instance.
7. Add `fixture` to test cases.
8. Create test file under tests.
    1. tests/test_search.py 
9. Start plan/draft test steps
10. Try to run test
    1. `pipenv run python -m pytest`
    2. If able to open chrome. Mean that the driver set up correctly.
11. Note: 
    1. Please manual install pylint `pip3 install pylint` at your terminal.
    2. DO NOT let VScode install for you.
    3. It locator directory might go wrong. Causing lint can’t import.
12. Use `pytest-xdist` to run test in pararell `pipenv install pytest-xdist`
13. To run it in parallel after install `pytest-xdist`.
    1. Run `pipenv run python -m pytest -n ${number of thread that you want it to run}` 