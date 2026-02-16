# Streamlit Test App

A simple Streamlit application for testing and learning.

## Setup

1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```

2. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the App

```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

## Project Structure

```
streamlit-test/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .streamlit/
│   └── config.toml    # Streamlit configuration
├── .gitignore         # Git ignore file
└── README.md          # This file
```

## Features

- Interactive sidebar with user inputs
- Sample data visualization
- Metrics display
- Expandable sections
- Custom theme configuration
