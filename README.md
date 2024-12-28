# DecAI Prognosis

DecAI Prognosis is a machine learning-powered application designed to predict the 10-year risk of mortality based on user-provided health parameters. This tool provides an intuitive interface for healthcare professionals and researchers to make data-driven predictions using pre-trained models.

---

## Features

- **Interactive Interface**: User-friendly interface created with Streamlit.
- **Customizable Inputs**: Accepts a variety of health-related inputs such as age, blood pressure, cholesterol levels, and more.
- **Prediction**: Provides a binary output indicating whether an individual is at risk or not at risk of mortality in the next 10 years.
- **Data Logging**: Saves user inputs and predictions to a CSV file for future analysis.
- **Dark Theme**: Modern, dark-themed design for better user experience.

---

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/makiatulmsyr17/decai-prognosis.git
   cd decai-prognosis
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

4. Open your web browser and navigate to `http://localhost:8501`.

---

## Usage

1. Enter the required health parameters in the input fields:
   - Age
   - Pulse Pressure
   - Systolic and Diastolic Blood Pressure
   - Serum Cholesterol
   - Sedimentation Rate
   - Gender
   - Serum Albumin

2. Click the **Predict** button to see the result.
3. To reset all inputs, click the **🔄** button.

---

## Model

The predictive model used in this application is trained on a dataset of health indicators. It employs a supervised learning algorithm to classify individuals into two categories:

- **At Risk of Mortality**
- **Not at Risk of Mortality**

---


## Contributions

We welcome contributions to improve DecAI Prognosis. Please fork the repository, create a new branch for your feature, and submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For questions or feedback, please contact:
- **Developer**: Makiatul Musyaropah
- **Email**: makiatulmusyaropah@gmail.com

## Link deployment
https://decaiprognosis.streamlit.app/

