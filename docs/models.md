# Models Structure

## Artists:

* title (CharField): the title of the artist, with a maximum of 200 characters.

* birth_date (DateField): the artist's birth date.

* death_date (DateField): the artist's death date.

## Painting:

* title (CharField): the title of the painting, with a maximum of 200 characters.

* width (FloatField): the width of the painting.

* height (FloatField): the height of the painting.

* depth (FloatField): the depth of the painting.

* artist_id (ForeignKey): a foreign key to the Artists model, representing the * 

* artist responsible for painting the artwork.