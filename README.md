markdown
# Interactive Analytics Dashboard for ADX Daily Bulletin Data

## Overview
This project provides an interactive analytics dashboard for the ADX Daily Bulletin dataset. The dashboard enables users to visualize and interact with financial data from the Abu Dhabi Securities Exchange (ADX) for March 31, 2026. The dashboard includes features like market overviews, detailed company insights, trend analysis tools, and customizable alerts.

## Features
- **Market Overview Panel:** Visualizes key market metrics such as total market capitalization, trading volume, and more.
- **Detailed Company Insights:** Provides a sortable and filterable table with financial details for each company.
- **Trend Analysis Tools:** Trends in trading volume, values, and stock prices visualized through graphs and maps.
- **Custom Alerts:** Set up alerts for specific financial conditions.
- **Export and Sharing:** Download visualizations and data or share insights directly from the dashboard.

## Prerequisites
- Python 3.7+
- Flask
- Pandas
- Plotly

## Installation
1. Clone the repository:
   bash
   git clone https://github.com/your-repo/ADX-Dashboard.git
   cd ADX-Dashboard
   
2. Install required dependencies:
   bash
   pip install -r requirements.txt
   
3. Place the dataset `Daily Bulletins March 31.xlsx` in the root directory.

## Usage
1. Run the Flask application:
   bash
   python app.py
   
2. Open your browser and navigate to `http://127.0.0.1:5000` to access the dashboard.
3. Interact with the visualizations, explore company data, and analyze market trends.

## Contributing
We welcome contributions to enhance this project! Please feel free to submit issues or pull requests.

## License
This project is licensed under the MIT License.
