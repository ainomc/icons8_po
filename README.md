# icon8 selenium/pytest tests
Runner: python init.py -login ainomc+1@gmail.com -password 123 -server https://demo.icons8.com/

Tests list:

- Landing Page - https://demo.icons8.com/web-app/24581/new-window#filled


Structure:

- Tests
    - Landing Page tests
- Context
    - Base Page Context - context/fixtures fo all pages
- Logic
    - Base Page Logic - tests logic fo all pages
- Locators
    - Base Page Locators - locators fo all pages
    - Landing Page Locators - locators fo landing pages

Empty context/logic/locators file not created.


