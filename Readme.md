Personality Classification Web Application
An intelligent web application that analyzes user responses to personality-based questions and classifies their personality type using machine learning techniques.

✨ Features
Clean and responsive web interface built with Flask and HTML/CSS.

Personality classification powered by K-Means clustering.

Dynamic visualization of results using Chart.js.

Easy to deploy, modular, and beginner-friendly.

🛠 Project Structure
graphql
Copy
Edit
├── app.py              # Main Flask application
├── Test.py             # Helper functions for result visualization
├── models/             # Machine Learning models
├── templates/          # HTML templates for frontend
├── static/css/         # CSS files for styling
├── questions.csv       # Dataset of personality questions
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
🚀 Getting Started
Prerequisites
Python 3.7+

pip (Python package manager)

Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/Abhishek26096/PERSONALITY-CLASSIFICATION-.git
cd PERSONALITY-CLASSIFICATION-
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # For Mac/Linux
venv\Scripts\activate      # For Windows
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the application:

bash
Copy
Edit
python app.py
Visit the application at:

arduino
Copy
Edit
http://localhost:5000
📊 Usage
Open the web app in your browser.

Answer all questions honestly.

Submit your responses.

View your personalized personality chart and insights.

📚 Technologies Used
Python

Flask

Machine Learning (K-Means Clustering)

HTML5, CSS3

Chart.js

🤝 Contributing
Contributions are welcome!
If you have ideas for improvements or new features:

Fork this repo.

Create a new branch (git checkout -b feature-idea).

Commit your changes.

Push your branch and open a Pull Request.

📄 License
This project is licensed under the MIT License.
