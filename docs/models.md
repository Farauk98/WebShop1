# Models Structure

## Artists:

| Attribute | Type | Description |
| -------- | -------- | -------- |
| title   | CharField   | The title of the artist.   |
| birth_date   | IntegerField   | The birth date of the artist (default: 0, nullable).  |
| death_date   | IntegerField   | The death date of the artist (default: 0, nullable).  |

## Painting:

| Attribute | Type | Description |
| -------- | -------- | -------- |
| title   | CharField   | The title of the painting.   |
| width   | FloatField   | The width of the painting (default: 0).  |
| height   | FloatField   | The height of the painting (default: 0).  |
| depth   | FloatField   | The depth of the painting (default: 0).  |
| artist_id   | ForeignKey   | The ID of the associated artist (nullable).  |
