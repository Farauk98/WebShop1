## index(request)

**Description:** This function is a view for the webshop index. It returns an HTTP response with the message "Hello, world. You're at the webshop index."

**Path:** `/`

**HTTP Method:** GET

**Parameters:** Not applicable

**Response:** 
- Status: 200 OK
- Body: "Hello, world. You're at the webshop index."

---

## ArtistsView(View)

### get(self, request)

**Description:** Retrieves data from the "https://api.artic.edu/api/v1/artists" API endpoint and saves it in the database. Prints the title, birth date, and death date of each artist received from the API. Creates or updates Artist objects with the retrieved data.

**Path:** `/artists/`

**HTTP Method:** GET

**Parameters:** Not applicable

**Response:** 
- Status: 200 OK
- Body: "Obiekty Artists zostały zaktualizowane."

---

## ArtistsCreateView(View)

### get(self, request)

**Description:** Initializes an empty ArtistsForm and renders a form.html template with the form.

**Path:** `/artists/create/`

**HTTP Method:** GET

**Parameters:** Not applicable

**Response:** 
- Status: 200 OK
- Body: Rendered HTML form

### post(self, request)

**Description:** Validates the ArtistsForm with the data received in the request. If the form is valid, it saves the form data as a new Artists object and returns an HTTP response with the message "Obiekty Artists zostały dodane." If the form is invalid, it renders the form.html template with the form to display validation errors.

**Path:** `/artists/create/`

**HTTP Method:** POST

**Parameters:** Form data

**Response:** 
- If form is valid:
  - Status: 200 OK
  - Body: "Obiekty Artists zostały dodane."
- If form is invalid:
  - Status: 200 OK
  - Body: Rendered HTML form with validation errors

---

## ArtistSelectView(View)

### get(self, request)

**Description:** Retrieves all Artists objects from the database and renders a select.html template with the artists' objects and the object_type set to 'artists'.

**Path:** `/artists/select/`

**HTTP Method:** GET

**Parameters:** Not applicable

**Response:** 
- Status: 200 OK
- Body: Rendered HTML template with artists' objects

### post(self, request)

**Description:** Retrieves the selected artist's ID from the request and redirects to the 'delete-object' view with the object_type set to 'artists' and object_id set to the selected artist's ID. If no artist is selected, it returns an HTTP response with the message "Nie wybrano żadnego artysty."

**Path:** `/artists/select/`

**HTTP Method:** POST

**Parameters:** Object ID (artist_id)

**Response:** 
- If artist_id is provided:
  - Status: 302 Found (Redirect)
  - Location: URL for 'delete-object' view with object_type='artists' and object_id set to the artist_id
- If artist_id is not provided:
  - Status: 200 OK
  - Body: "Nie wybrano żadnego artysty."

---

## PaintingsView(View)

### get(self, request)

**Description:** Retrieves data from the "https://api.artic.edu/api/v1/artworks" API endpoint and saves it in the database. Retrieves the title, width, height, depth, and artist ID for each artwork received from the API. Creates or updates Painting objects with the retrieved data.

**Path:** `/paintings/`

**HTTP Method:** GET

**Parameters:** Not applicable

**Response:** 
- Status: 200 OK
- Body: "Obiekty Artworks zostały zaktualizowane."

---

## PaintingsCreateView(View)

### get(self, request)

**Description:** Initializes an empty PaintingsForm and renders a form.html template with the form.

**Path:** `/paintings/create/`

**HTTP Method:** GET

**Parameters:** Not applicable

**Response:** 
- Status: 200 OK
- Body: Rendered HTML form

### post(self, request)

**Description:** Validates the PaintingsForm with the data received in the request. If the form is valid, it saves the form data as a new Painting object and returns an HTTP response with the message "Obiekty Paintings zostały dodane." If the form is invalid, it renders the form.html template with the form to display validation errors.

**Path:** `/paintings/create/`

**HTTP Method:** POST

**Parameters:** Form data

**Response:** 
- If form is valid:
  - Status: 200 OK
  - Body: "Obiekty Paintings zostały dodane."
- If form is invalid:
  - Status: 200 OK
  - Body: Rendered HTML form with validation errors

---

## PaintingSelectView(View)

### get(self, request)

**Description:** Retrieves all Painting objects from the database and renders a select.html template with the paintings' objects and the object_type set to 'paintings'.

**Path:** `/paintings/select/`

**HTTP Method:** GET

**Parameters:** Not applicable

**Response:** 
- Status: 200 OK
- Body: Rendered HTML template with paintings' objects

### post(self, request)

**Description:** Retrieves the selected painting's ID from the request and redirects to the 'delete-object' view with the object_type set to 'paintings' and object_id set to the selected painting's ID. If no painting is selected, it returns an HTTP response with the message "Nie wybrano żadnego obrazu."

**Path:** `/paintings/select/`

**HTTP Method:** POST

**Parameters:** Object ID (painting_id)

**Response:** 
- If painting_id is provided:
  - Status: 302 Found (Redirect)
  - Location: URL for 'delete-object' view with object_type='paintings' and object_id set to the painting_id
- If painting_id is not provided:
  - Status: 200 OK
  - Body: "Nie wybrano żadnego obrazu."

---

## ObjectDeleteView(View)

### get(self, request, object_type, object_id)

**Description:** Deletes the object with the specified object_type and object_id from the database. If the object_type is 'paintings', it retrieves the Painting object with the matching ID. If the object_type is 'artists', it retrieves the Artists object with the matching ID. Then, it deletes the object and returns an HTTP response with the message "Obiekt {object_type.capitalize()} został usunięty."

**Path:** `/delete/<str:object_type>/<int:object_id>/`

**HTTP Method:** GET

**Parameters:** 
- object_type (string): Type of the object to delete ('paintings' or 'artists')
- object_id (integer): ID of the object to delete

**Response:** 
- Status: 200 OK
- Body: f"Obiekt {object_type.capitalize()} został usunięty."