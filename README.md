# 🩹 SPORTS-INJURY-TRACKER: Advanced Rehab & Safe-Dosage Ecosystem

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-streamlit-app-link.com) <!-- Placeholder for live app link -->
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?style=flat&logo=sqlite&logoColor=white)](https://www.sqlite.org/index.html)
[![Pandas](https://img.shields.io/badge/Data-Pandas-150458?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Visualization-Plotly%20Express-3F4040?style=flat&logo=plotly&logoColor=white)](https://plotly.com/python/plotly-express/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🎯 Project Overview

The **SPORTS-INJURY-TRACKER** is a robust, user-friendly application designed to empower individuals in managing their injury recovery journey and ensuring safe medication intake. It provides a centralized platform to log medication dosages, track pain levels, identify potential triggers, and monitor side effects, all while offering crucial safety warnings against over-dosage and medication overlaps.

This ecosystem simplifies the complex task of personal health tracking, offering valuable insights into recovery progression and medication efficacy through intuitive data visualization.

## 🚀 Key Features

*   **⚡ One-Click Injury Presets**: Accelerate data entry with predefined profiles for common conditions like "Acute Ankle Sprain" or "Lumbar Disc Back Pain," pre-filling medication, dosage, and pain levels.
*   **💊 Intelligent Medication Management**:
    *   **Dosage Limit Enforcement**: Automatically prevents exceeding maximum recommended daily dosages for medications (e.g., Ibuprofen, Acetaminophen).
    *   **Active Medication Clearance**: Displays real-time countdowns for medication clearance from the system, preventing accidental re-dosing.
    *   **NSAID Overlap Warnings**: Crucially alerts users if multiple Non-Steroidal Anti-Inflammatory Drugs (NSAIDs) are active concurrently, minimizing risk of gastric irritation.
*   **📊 Comprehensive Pain & Behavioral Analytics**:
    *   **Pain Progression Matrix**: Visualize your pain score trends over time with dynamic line charts, helping to understand recovery patterns.
    *   **Top Trigger Identification**: Automatically identifies and charts recurring pain triggers (e.g., "Long Sitting," "Stress," "Cold Weather").
    *   **Side Effect Tracker**: Monitors and summarizes reported side effects from medications, aiding in informed health decisions.
*   **🔒 Secure Local Data Storage**: All your health logs are securely stored in a local SQLite database, ensuring privacy and easy access.
*   **✨ Intuitive Streamlit Interface**: A clean, responsive, and easy-to-use graphical interface built with Streamlit for a seamless user experience.

## 📦 Installation Guide

To get the SPORTS-INJURY-TRACKER up and running on your local machine, follow these simple steps:

### Prerequisites

*   **Python 3.8+**
*   **Git** (for cloning the repository)

### Steps

1.  **Clone the Repository:**
    Navigate to your desired directory and clone the project:
    ```bash
    git clone https://github.com/your-username/SPORTS-INJURY-TRACKER.git
    cd SPORTS-INJURY-TRACKER
    ```

2.  **Create a Virtual Environment:**
    It's recommended to use a virtual environment to manage project dependencies:
    ```bash
    python -m venv venv
    ```

3.  **Activate the Virtual Environment:**
    *   **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```
    *   **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```

4.  **Install Dependencies:**
    Install all required Python packages using `pip`. Create a `requirements.txt` file in your project root with the following content:
    ```
    streamlit>=1.0.0
    pandas>=1.0.0
    plotly-express>=0.4.0
    ```
    Then, install them:
    ```bash
    pip install -r requirements.txt
    ```

## 🛠️ Usage

Once installed, running the SPORTS-INJURY-TRACKER is straightforward:

1.  **Ensure your virtual environment is active** (as per step 3 in Installation).

2.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

3.  Your web browser will automatically open to the Streamlit application (usually `http://localhost:8501`).

### How to Interact

*   **Log Entries**: Use the "One-Click Injury Presets & Intake" section on the left to select a preset or manually enter medication details, dosage, pain level, triggers, and side effects. Click "Log Entry to Local Database" to save.
*   **Monitor Warnings**: The "Active Medical Warning Controls" section will display active medication clearance times and any critical NSAID overlap warnings.
*   **View Analytics**: Scroll down to "Long-Term Pain Reduction & Behavioral Analytics" to see interactive charts visualizing your pain progression, top triggers, and side effect distribution.

## 🤝 Contributing

We welcome contributions to the SPORTS-INJURY-TRACKER project! Whether it's bug reports, feature requests, or code contributions, your input is valuable.

1.  **Fork** the repository.
2.  **Create a new branch** (`git checkout -b feature/your-feature-name`).
3.  **Make your changes**.
4.  **Commit your changes** (`git commit -m 'feat: Add new awesome feature'`).
5.  **Push to the branch** (`git push origin feature/your-feature-name`).
6.  **Open a Pull Request**.

Please ensure your code adheres to good practices and includes appropriate tests if applicable.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
