# Census Grants Tool Project

This project is a capstone aimed at developing a web-based tool that supports novice grant applicants (SLaNT users) by providing them with the top 100 most relevant Census Bureau statistics.

## Project Overview

- **Objective:**  
  Identify and display the top 100 most relevant Census Bureau statistics to assist grant applicants, with features such as data filtering, trend visualizations, and exportable graphics.
  
- **Key Features:**  
  - Direct integration with the Census Bureau API for live data retrieval.
  - Filtering options (geography, year, topical domains, etc.).
  - Clear data definitions and citations.
  - User-friendly, exportable data visualizations.

## Progress Tracking and Changelog

Below is a running log of our project milestones and updates:

### [YYYY-MM-DD] Project Initialization
- Created project repository.
- Established initial project structure.
- Set up the README file for tracking purposes.

### [YYYY-MM-DD] Census API Key Setup
- **Reviewed Documentation:**  
  Went through the [Census API User Guide](https://www.census.gov/data/developers/guidance/api-user-guide.html) to understand endpoints and parameters.
  
- **Obtained API Key:**  
  - Signed up for the API key at the [Census API Key Signup](https://api.census.gov/data/key_signup.html).
  - Noted the limitation of one key per email address. For development and testing, either use a shared project key or individual keys as needed.

- **Integrated API Key into the Project:**  
  - Created a `.env` file in the project root with the following entry:
    ```
    CENSUS_API_KEY=YOUR_CENSUS_API_KEY
    ```
  - Implemented code to load the API key securely using the `python-dotenv` package.

### [YYYY-MM-DD] API Integration and Testing
- Developed basic API request functions using the `requests` library.
- Implemented error handling and logging for API requests.
- Tested endpoints with sample queries (e.g., retrieving population data for a specific state).

### [YYYY-MM-DD] Front-End & Visualization Prototyping
- Designed initial wireframes and concept pitch for the web-based tool.
- Started integrating data visualizations using libraries such as D3.js or Plotly.

## Setup Instructions

### Prerequisites
- Python 3.7 or higher
- Required libraries:
  - `requests`
  - `python-dotenv`
- A valid Census API key (see instructions below).

### Obtaining and Configuring the Census API Key

1. **Sign Up for an API Key:**
   - Visit the [Census API Key Signup](https://api.census.gov/data/key_signup.html) page.
   - Enter your email and request your API key (note the one-key-per-email limitation).

2. **Store Your API Key Securely:**
   - Create a file named `.env` in the project root.
   - Add the following line to your `.env` file:
     ```
     CENSUS_API_KEY=YOUR_CENSUS_API_KEY
     ```
   - **Note:** Make sure this file is included in your `.gitignore` to avoid committing sensitive information.

3. **Access the API Key in Your Code:**

   Example in Python:

   ```python
   import os
   from dotenv import load_dotenv
   import requests

   # Load environment variables from .env file
   load_dotenv()

   # Retrieve the API key from the environment variable
   API_KEY = os.getenv("CENSUS_API_KEY")
   if not API_KEY:
       raise ValueError("CENSUS_API_KEY not set in the .env file.")

   # Define the base URL and parameters for the API request
   base_url = "https://api.census.gov/data/2020/acs/acs5"
   params = {
       "get": "NAME,B01003_001E",  # Example: NAME and total population estimate
       "for": "state:06",          # Example: California (state code 06)
       "key": API_KEY
   }

   # Make the API request
   response = requests.get(base_url, params=params)
   if response.status_code == 200:
       data = response.json()
       print(data)
   else:
       print(f"Error: {response.status_code}")
