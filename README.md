# apitests
Python based test framework called `Pytest` to test public API. Mainly designed to test a Public API `https://api.weather.gov/points/39.7456,-97.0892`

# how to run the tests?
1. Clone to repositiry to a folder and change to close folder
2. Make sure you have python3 and install the following packages `pip3 install pytest` and `pip3 install requestes`
3. run command `pytest` on shell command

# Pros of Pytest framework approach
1. Pytest framework does not need any license and easy to learn
2. Pytest can choose to run a particular test method or all the test methods of a particular test file based on conditions.
3. Pytest is capable of skipping a few test methods out of all the test methods during test execution.
4. Pytest can be used to test a wide range of applications on API, database and so on.
5. We can add more assertions if needed
6. It can be easily integrated with CI/CD pipeline
8. Easy to maintain tests in Pytest framework

# Cons of Pytest framework approach
1. Tests will not uncover every bug.
2. It will not catch errors in integration.
