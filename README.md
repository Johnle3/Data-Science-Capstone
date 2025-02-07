# Census Grants Tool Project

This capstone project develops a web-based tool that supports novice grant applicants (SLaNT users) by providing the top 100 relevant Census Bureau statistics with features like filtering, trend visualizations, and exportable graphics.

## Repository Structure

- **ConnectToCensusAPI.ipynb**: Jupyter Notebook with API connection code
- **LICENSE**: Project license
- **README.md**: This file
- **requirements.txt**: Python package dependencies

## Progress & Milestones

- **Project Initialization**: Created repository, established structure, set up README.
- **Census API Key Setup**: Reviewed the Census API User Guide, obtained and integrated the API key via a `.env` file using `python-dotenv`.
- **API Integration & Testing**: Developed basic API request functions and tested endpoints.
- **Front-End & Visualization Prototyping**: Designed wireframes and began data visualizations.

## Setup Instructions

### Prerequisites

- Python 3.7+
- Jupyter Notebook (or JupyterLab)
- A valid Census API key

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/Data-Science-Capstone.git
   cd Data-Science-Capstone
Install Dependencies:

bash
Copy
pip install -r requirements.txt
Configure Your API Key:

Create a .env file in the project root with:
env
Copy
CENSUS_API_KEY=YOUR_CENSUS_API_KEY
Ensure .env is added to your .gitignore.
Running the Project
Launch Jupyter Notebook:

bash
Copy
jupyter notebook
Then open and run the ConnectToCensusAPI.ipynb notebook.

Future Work
Enhance data filtering and visualization features.
Develop a fully interactive web interface.
Implement user authentication and personalized dashboards.
