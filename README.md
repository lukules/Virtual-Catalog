# Virtual Car Catalog with Automated Vehicle Classification
## Project Overview

This project is a full-stack web application developed as part of my engineering thesis. The application serves as a virtual car catalog designed for automotive dealerships or enthusiasts. Its unique feature is the automated classification of uploaded vehicle images, leveraging machine learning to determine the vehicle type, body type, and brand, with the possibility of detecting the model.

The project integrates a React-based frontend with a Django backend that uses PostgreSQL as the database. It incorporates machine learning models to classify vehicles based on their images, making it easier to populate the catalog.
# Key Features

    Automated Vehicle Classification:
        Users can upload images of vehicles, and the system will automatically classify the vehicle type (car, truck, bus, motorcycle), body type (SUV, sedan, coupe, etc.), and in some cases, the brand.
        The system uses pre-trained EfficientNetB7 models and other custom models for image classification.

    User Authentication:
        Secure user authentication with Django REST Framework.
        Users can create accounts, log in, and manage their vehicle catalog.

    Car Catalog Management:
        Users can view, add, update, or delete vehicles from their personalized catalog.
        The catalog allows users to filter vehicles by various attributes like brand, vehicle type, body type, and production year.

    React Frontend:
        The frontend is developed using React and Material-UI for a modern and responsive user experience.
        Users can easily navigate between sections like the car catalog, car recognition, and contact forms.
        Includes features like filters, dialogs for editing vehicle information, and real-time updates.

    Django Backend:
        The backend is built using Django and Django REST Framework (DRF) to handle API requests and manage data.
        PostgreSQL is used as the database for reliable data storage.
        The backend handles image uploads, predictions using TensorFlow models, and user authentication.

    Machine Learning Integration:
        EfficientNetB7 is used for vehicle type prediction.
        Custom-trained models are used for car body type classification (e.g., SUV, sedan, etc.).
        The predictions are made in real-time, and the results are displayed on the frontend.

    Manual Testing:
        The entire system was thoroughly tested to ensure the accuracy of vehicle classification and the smooth functioning of the web application.

# Technology Stack

    Frontend: React, Material-UI
    Backend: Django, Django REST Framework
    Database: PostgreSQL
    Machine Learning Models: TensorFlow, Keras, EfficientNetB7
    Image Processing: Pillow for handling image uploads and processing.

# Application Structure
## Frontend (React)

    Main Components:
        Navbar: Navigation bar that allows users to move between different sections of the application.
        Main: The homepage, which gives users an overview of the platform.
        Recognize: The car recognition page where users can upload photos of vehicles for classification.
        Catalog: A personalized vehicle catalog that users can manage by adding, editing, or removing vehicles.
        Contact: A contact page for inquiries.

    Routing: The application uses react-router-dom for routing, allowing users to navigate between different pages:
        / - Home page
        /recognize - Vehicle recognition page
        /catalog - User's vehicle catalog
        /contact-us - Contact page

## Backend (Django)

    Endpoints:
        /api/account/: Handles user authentication (registration, login).
        /api/vehicles/: Manages vehicle operations such as adding to the catalog, deleting, and updating vehicles. Also handles image classification.

    Vehicle Classification: The backend integrates TensorFlow models for vehicle classification:
        EfficientNetB7 for vehicle type prediction.
        A custom car body type model for detailed classification of car types (e.g., sedan, SUV, coupe, etc.).

# How the Classification Works

    Image Upload: Users upload images via the frontend.
    Image Preprocessing: The image is resized and preprocessed on the backend using Pillow and TensorFlow preprocessing functions.
    Prediction: The pre-trained model predicts the vehicle type, while the custom model predicts the car body type for cars.
    Display Results: The predictions are sent back to the frontend and displayed to the user along with probabilities for each class.

# Testing

The application was tested across different environments and scenarios to ensure reliability and accuracy:

    Manual Testing was conducted to evaluate the functionality of user registration, vehicle classification, and catalog management.
    Machine Learning Model Testing: The vehicle classification models were tested using various real-world images to validate accuracy across different vehicle types and conditions.
