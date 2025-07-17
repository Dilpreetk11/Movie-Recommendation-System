# Movie Recommender System

This is a Streamlit-based Movie Recommender System that suggests similar movies and displays their posters using the TMDb API.

## Features

* Select a movie from a dropdown.
* Get top 5 movie recommendations with posters.
* Interactive web interface.

## Setup

1.  **Prerequisites:** Ensure Python 3.x is installed.
2.  **Clone/Download:** Get `app.py`, `movies_dict.pkl`, `similarity.pkl`, `README.md`, and `requirements.txt` into one directory.
3.  **Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate # Windows: `venv\Scripts\activate`
    ```
4.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  Ensure `movies_dict.pkl` and `similarity.pkl` are in the same directory.
2.  Run the app:
    ```bash
    streamlit run app.py
    ```
3.  Access the application in your browser (usually `http://localhost:8501`).

## Data Files

The system uses `movies_dict.pkl` (movie data) and `similarity.pkl` (similarity matrix) for recommendations. These are essential and must be present.

## API Key

The TMDb API key is hardcoded. For production, obtain your own key and store it securely (e.g., environment variables).

