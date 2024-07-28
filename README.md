# Image-Color-Palette-Generator
The Image Color Palette Generator is a web application that allows users to upload an image and extract a color palette from it.


The application displays the uploaded image and the extracted colors with their hex codes.

Libraries and Frameworks Used
    Flask: For setting up the web server, handling requests, and rendering HTML templates.
    Werkzeug: For secure handling of file uploads.
    WTForms and Flask-WTF: For creating and validating web forms, and handling file uploads.
    Pillow: For image processing tasks like opening, resizing, and converting images.
    NumPy: For converting images to numerical arrays for processing.
    Scikit-learn: For applying the KMeans clustering algorithm to extract dominant colors.
    Matplotlib.colors: For converting RGB color values to hex codes.
    HTML/CSS: For creating and styling the web page.
    Key Features
    Image Upload: Users can upload image files (PNG, JPG, JPEG, GIF).
    Color Extraction: Extracts up to 10 dominant colors using KMeans clustering and displays them with hex codes.
    Dynamic Form Handling: Upload button is disabled until an image is selected, ensuring proper user interaction flow.
    How It Works
    Image Upload: The user uploads an image which is securely saved on the server.
    Color Extraction: The image is processed to extract dominant colors which are then converted to hex codes.
    Display Results: The uploaded image and the extracted colors are displayed on the webpage.
