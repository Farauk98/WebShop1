# Artist Model Unit Tests

The `ArtistModelTest` class contains unit tests for the `Artist` model in the project.

## Setup

The `setUp` method is called before each test to set up the necessary data for testing. In this case, an `Artist` instance is created with the following details:
- Title: Vincent van Gogh
- Birth Date: 1853
- Death Date: 1890

## Test Cases

### `test_str_representation`

This test verifies that the `__str__` method of the `Artist` model returns the expected string representation. It asserts that the string representation of the `self.artist` instance is equal to 'Vincent van Gogh'.

### `test_birth_date_default_value`

This test checks the default value of the `birth_date` field in the `Artist` model. It creates an `Artist` instance with the title 'Pablo Picasso' and asserts that the `birth_date` is equal to 0.

### `test_death_date_default_value`

Similar to the previous test, this test validates the default value of the `death_date` field in the `Artist` model. It creates an `Artist` instance with the title 'Leonardo da Vinci' and asserts that the `death_date` is equal to 0.


**Unit Test Results:**
```shell
- Found 3 test(s).
- Creating test database for alias 'default'...
- System check identified no issues (0 silenced).
- ...
- Ran 3 tests in 0.007s.
- OK
- Destroying test database for alias 'default'...
```