Get you API key from here == https://api.nasa.gov
Project Demo = https://astronomy-picture-of-the-day007.streamlit.app/



# Astronomy Picture of the Day (APOD) Viewer

A simple Streamlit web application that fetches and displays NASA's Astronomy Picture of the Day (APOD) using the
NASA APOD API. The app showcases the daily astronomy image or video along with its title, explanation, and metadata.

## Features

- Fetches the latest Astronomy Picture of the Day from NASA's APOD API.
- Displays high-definition images or embedded videos (if available).
- Shows the title, date, copyright information (if applicable), and a detailed explanation of the APOD.
- Responsive layout for better viewing on different screen sizes.

## Demo

You can try the app live https://astronomy-picture-of-the-day007.streamlit.app/.

![image](https://github.com/user-attachments/assets/48fe6d95-6002-4760-b255-73b0db0ae918)


## Installation

To run this app locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Nabanshu/Astronomy-Picture-of-the-Day..git
   cd Astronomy-Picture-of-the-Day
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your NASA API key:**
   - Get your API key from [NASA's API Portal](https://api.nasa.gov/).
   - Create a `.streamlit/secrets.toml` file in the project directory and add your API key:
     ```toml
     API_KEY = "your_api_key_here"
     ```

5. **Run the Streamlit app:**
   ```bash
   streamlit run main.py
   ```

6. **Open the app in your browser:**
   The app will be available at `http://localhost:8501`.

## Usage

- The app automatically fetches the latest APOD when opened.
- The image or video is displayed on the left, while the title and explanation are shown on the right.
- If the APOD is a video, it will be embedded directly in the app.

## Dependencies

- Python 3.7+
- Streamlit (`pip install streamlit`)
- Requests (`pip install requests`)


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to [NASA](https://nasa.gov/) for providing the APOD API.
- Built with [Streamlit](https://streamlit.io/).

