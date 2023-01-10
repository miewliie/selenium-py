# selenium + python
Course at TAU by Andrew Knight: https://testautomationu.applitools.com/selenium-webdriver-python-tutorial/

Documentation in my versions:
1. Install python
2. Install pipenv (pipenv -- version)
    - Pip3 install pipenv
3. then, clone/create project on git.
    * Download Chrome Driver 
        * open it
        * Move to bin : `mv current/chromedriver /usr/local/bin` to bin.
    * Download Firefox Driver (geckodriver)
        * open it
        * Move to bin : `mv current/geckodriver /usr/local/bin` to bin. 
4. Open project in VS Code.
5. Install selenium using pipenv (creates and manages a virtualenv for the projects).
    1. `pipenv install selenium `
6. Create `confetti.py` file for config fixture.
    1. Create web driver instance etc. 
    2. Then always QUIT the instance.
7. Add `fixture` to test cases.
8. Create test file under tests.
    1. tests/test_search.py 
9. Start plan/draft test steps