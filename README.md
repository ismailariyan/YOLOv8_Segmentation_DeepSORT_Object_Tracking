
# 🚗 Vehicle Speed Estimation and Detection Flask App

## 📋 Project Overview

This project aims to estimate vehicle speed and detect vehicles using the YOLOv8 model. The model was trained on data sourced from RoboFlow, and the entire training process was carried out in Google Colab. The frontend of the application was built using the Flask framework. The application can count the number of cars based on their direction and store this information. while it estimates the speed of the detected vehicles.

## 📑 Table of Contents

- [Project Overview](#-project-overview)
- [Installation](#-installation)
- [Usage](#-usage)
- [Model Training](#-model-training)
- [Frontend Development](#-frontend-development)
- [Technologies Used](#-technologies-used)
- [Demo Video](#-demo-video)

## 🛠️ Installation

To run this project locally, follow these steps:

1. **Clone the repository:**
    ```sh
    git clone https://github.com/ismailariyan/vehicle-overspeeding-detection-flaskapp.git
    ```

2. **Navigate to the project directory:**
    ```sh
    cd vehicle-overspeeding-detection-flaskapp
    ```

3. **Create a virtual environment and activate it:**
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

4. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

## 🚀 Usage

1. **Start the Flask application:**
    ```sh
    python ultralytics\yolo\v8\segment\app.py
    ```

2. **Open your web browser and go to `http://127.0.0.1:5000`.**

3. **Upload a video file to detect vehicles and estimate their speed.**

## 🧠 Model Training

The YOLOv8 model was trained using a dataset from RoboFlow.

## 🌐 Frontend Development

The frontend was built using the Flask framework. Here is a brief overview of the steps:

## 🛠️ Technologies Used

- **YOLOv8** for vehicle detection and speed estimation
- **RoboFlow** for dataset sourcing
- **Google Colab** for model training
- **Flask** for the web framework
- **Python** for backend development
- **HTML/CSS** for frontend design

## 🎥 Demo Video

![Demo Video](https://github.com/ismailariyan/vehicle-overspeeding-detection-flaskapp/blob/0692dff29e955fee37e4d2a241093779b133e755/runs/detect/train/final.gif)

