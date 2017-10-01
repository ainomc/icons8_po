# icon8 selenium/pytest tests

### Run
    Runner: python -m pytest -v tests/tests_* -s -l --login po_tests@gmail.com  --password 123 --landing_url https://demo.icons8.com/icon/ --icon8_mobile_url https://demo.icons8.com/icons/ --junitxml=junit_report/junit.xml --html=html_report/report.html


### Tests
    Landing Page tests - tests for https://demo.icons8.com/web-app/24581/new-window#filled
    SleekLogos Page tests - tests for https://sleeklogos.design/
    IconPharm Page tests - tests for https://iconpharm.com/
    Icons mobile page - tests for https://demo.icons8.com/icons/ with mobile scree resolution
   
### Project sctructure
    .
    ├── confest_fixtures        # Confest fixtures for tests
    ├── download                # Folder for download tests
    ├── html_report             # HTML tests report
    ├── locators                # Locators for tests
    ├── logic                   # Logic for tests
    ├── report                  # Junit report treport
    ├── tests                   # Tests
    ├── .gitignore
    └── README.md



