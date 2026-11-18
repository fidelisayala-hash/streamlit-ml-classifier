# Machine Learning Web App

An interactive machine learning application built with **Streamlit** that enables users to explore datasets, visualize features, train classification models, and evaluate performance through a simple web interface.

The application demonstrates the practical application of supervised machine learning concepts using popular datasets from **scikit-learn**, while providing a user-friendly environment for experimentation with different classification algorithms and hyperparameters.

---

## Overview

This project allows users to:

- Explore real-world classification datasets
- Visualize feature distributions and data characteristics
- Train machine learning models interactively
- Compare classifier performance
- Adjust model hyperparameters in real time
- Evaluate predictions using classification accuracy

The application is designed as a hands-on learning tool for understanding the machine learning workflow, from data exploration to model evaluation.

---

## Key Features

### Dataset Exploration

Users can select from three well-known datasets:

- **Iris Dataset** – Multiclass flower species classification
- **Breast Cancer Dataset** – Binary classification of malignant and benign tumors
- **Wine Dataset** – Multiclass classification of wine varieties

### Interactive Visualizations

The application provides exploratory data analysis through:

- Box plots for feature distribution analysis
- Histograms for understanding variable frequencies
- Dataset summaries including:
  - Number of samples
  - Number of features
  - Number of target classes

### Machine Learning Models

The following classification algorithms are implemented:

#### K-Nearest Neighbors (KNN)

A distance-based supervised learning algorithm that classifies observations according to the majority class among their nearest neighbors.

**Configurable Parameter**
- Number of Neighbors (K)

#### Support Vector Machine (SVM)

A powerful classification algorithm that identifies an optimal decision boundary between classes.

**Configurable Parameter**
- Regularization Parameter (C)

### Model Evaluation

After training, the application displays:

- Model predictions
- Classification accuracy score
- Selected classifier information

---

## Technology Stack

| Technology | Purpose |
|------------|---------|
| Streamlit | Interactive web application framework |
| Scikit-learn | Machine learning algorithms and datasets |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical computing |
| Matplotlib | Data visualization |
| Seaborn | Statistical data visualization |
| Python | Core programming language |

---

## Project Structure

```text
machine-learning-web-app/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/machine-learning-web-app.git
cd machine-learning-web-app
```

### Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment:

**Windows (PowerShell)**

```powershell
.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt)**

```cmd
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Launch the Streamlit application locally:

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## Workflow

1. Select a dataset from the sidebar.
2. Explore the dataset and visualizations.
3. Choose a classification algorithm.
4. Adjust hyperparameters.
5. Train the model.
6. Review predictions and model accuracy.

---

## Learning Objectives

This project demonstrates practical knowledge of:

- Machine Learning Fundamentals
- Classification Algorithms
- Data Visualization
- Exploratory Data Analysis (EDA)
- Model Training and Evaluation
- Hyperparameter Tuning
- Interactive Application Development with Streamlit

---

## Future Enhancements

Potential improvements include:

- Additional classification algorithms
- Confusion matrix visualization
- Precision, Recall, and F1-score metrics
- Principal Component Analysis (PCA) visualization
- Cross-validation support
- User-uploaded datasets
- Model comparison dashboard

---

## License

This project is intended for educational and portfolio purposes. Feel free to fork, modify, and extend the application for your own learning and experimentation.