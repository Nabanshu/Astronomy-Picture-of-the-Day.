Get you API key from here == https://api.nasa.gov
Project Demo = https://astronomy-picture-of-the-day007.streamlit.app/

Astronomy Picture of the Day (APOD) Streamlit App

Overview

This project is a Streamlit-based web application that fetches and displays NASA's Astronomy Picture of the Day (APOD) using NASA's APOD API. The application provides a visually appealing interface to explore daily astronomical images along with their metadata.

Features

Fetches the latest Astronomy Picture of the Day from NASA's APOD API.

Displays images or videos with relevant metadata, including date and copyright information (if available).

Provides an informative explanation of the image/video.

User-friendly Streamlit interface with a wide layout for better visualization.

Installation

To run this project locally, follow these steps:

Clone the repository:

git clone https://github.com/your-username/apod-streamlit.git
cd apod-streamlit

Install the required dependencies:

pip install -r requirements.txt

Set up your API key:

Obtain a free API key from NASA API.

Store it securely in a .streamlit/secrets.toml file:

[API_KEY]
api_key = "your_nasa_api_key_here"

Run the application:

streamlit run app.py

Code Explanation

The main application (app.py) follows these steps:

Sets the Streamlit page configuration.

Requests data from NASA's APOD API.

Parses and displays the image or video along with its details.

Handles missing or unavailable content gracefully.

Dependencies

Ensure you have the following Python packages installed:

streamlit

requests

You can install them using:

pip install streamlit requests

Usage

Simply run the application and enjoy daily astronomical content!

License

This project is open-source and available under the MIT License.

Acknowledgments

NASA APOD API for providing stunning space imagery.

Streamlit for enabling quick web app development.

Feel free to contribute and improve this project!
