# icon8 selenium/pytest tests
Runner: python -m pytest -v tests/tests_* -s -l --login po_tests@gmail.com  --password 123 --landing_url https://demo.icons8.com/icon/ --icon8_mobile_url https://demo.icons8.com/icons/ --junitxml=report/junit.xml --html=html_report/report.html


Structure:

- Tests
    - Landing Page tests - tests for https://demo.icons8.com/web-app/24581/new-window#filled
    - SleekLogos Page tests - tests for https://sleeklogos.design/
    - IconPharm Page tests - tests for https://iconpharm.com/
- Context
    - Base Page Context - context/fixtures fo all pages
    - SleekLogos Page Context
    - IconPharm Page Context
- Logic
    - Base Page Logic - tests logic for all pages
    - Base Page Click Logic - click logic for all pages
    - Base Page Locate Logic - locate logic for all pages
- Locators
    - Base Page Locators - locators fo all pages
    - Landing Page Locators - locators fo landing pages
    - SleekLogos Page Locators
    - IconPharm Page Locators

Empty context/logic/locators file not created.


