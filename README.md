# Gemini API Math & Drawing Recognition

## Description

This project is a web application that utilizes Google's Gemini API to recognize and interpret user inputs. Users can:

- Draw images, and the application will define the drawn object.
- Write or draw mathematical equations, and the system will provide answers along with explanations.

The project is built using:

- *React.js* for the frontend
- *Tailwind CSS* for styling
- *Python* for backend processing
- *Gemini API* for AI-powered interpretation and response generation

## Features

- *Drawing Recognition*: Identify and define drawn objects.
- *Mathematical Equation Solver*: Solve equations and provide detailed explanations.
- *Seamless UI*: Built with React.js and styled using Tailwind CSS for a smooth user experience.
- *AI Integration*: Uses the Gemini API for intelligent interpretation.

## Installation

### Prerequisites

Ensure you have the following installed:

- Node.js & npm
- Python

### Backend Setup (Python)

Clone the repository:

```sh
git clone [https://github.com/your-username/gemini-math-draw.git
cd gemini-math-draw](https://github.com/Manvendra200125/MSN-AI-Gemini-Clone)

python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate

pip install -r requirements.txt

GEMINI_API_KEY=your_api_key_here

python server.py

npm install

npm start
