# Models Structure

## Artists:

| Attribute | Type | Description |
| -------- | -------- | -------- |
| title   | CharField   | The title of the artist.   |
| birth_date   | IntegerField   | The birth date of the artist (default: 0, nullable).  |
| death_date   | IntegerField   | The death date of the artist (default: 0, nullable).  |

## Painting:

* title (CharField): the title of the painting, with a maximum of 200 characters.

* width (FloatField): the width of the painting.

* height (FloatField): the height of the painting.

* depth (FloatField): the depth of the painting.

* artist_id (ForeignKey): a foreign key to the Artists model, representing the * 

* artist responsible for painting the artwork.