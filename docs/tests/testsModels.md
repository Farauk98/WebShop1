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

# Paiting Model Unit Tests

The `PaintingModelTest` class contains unit tests for the `Painting` model in the project.

## Setup

The `setUp` method is called before each test to set up the necessary data for testing. In this case, an `Artist` instance is created with the following details:
- Title: Vincent van Gogh
- Birth Date: 1853
- Death Date: 1890

A `Painting` instance is also created with the following details:
- Title: Starry Night
- Width: 92.1
- Height: 73.7
- Depth: 1.7
- Artist: Vincent van Gogh

## Test Cases

### `test_str_representation`

This test verifies that the `__str__` method of the `Painting` model returns the expected string representation. It asserts that the string representation of the `self.painting` instance is equal to 'Starry Night'.

### `test_default_values`

This test checks the default values of the `width`, `height`, `depth`, and `artist_id` fields in the `Painting` model. It asserts that the `width` is equal to 92.1, the `height` is equal to 73.7, the `depth` is equal to 1.7, and the `artist_id` is equal to the `Artist` instance created during setup.

### `test_artist_foreign_key`

This test ensures that the `artist_id` field in the `Painting` model is a foreign key to the `Artist` model. It asserts that the `artist_id` of the `self.painting` instance is equal to the `Artist` instance created during setup.
