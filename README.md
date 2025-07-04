## Third-Party Risk Assessment (TPRA) Project

## 📌 Project Overview
The **Third-Party Risk Assessment (TPRA) Project** is designed to evaluate and mitigate security, compliance, and operational risks posed by external vendors. It provides a structured framework, automated assessment tools, and risk reporting mechanisms to help organizations manage vendor risks efficiently.

## 🚀 Features
- ✅ **Vendor Risk Checklist** – Standardized evaluation questions for consistency.
- ⚙️ **Automated Risk Scoring** – Python-based scoring of vendor responses.
- 🔐 **Compliance Frameworks Support** – Aligned with NIST, ISO 27001, SOC 2, GDPR, and HIPAA.
- 📊 **Risk Dashboard** – Jupyter Notebook for interactive risk visualization.
- 🛠️ **Configurable Parameters** – YAML-driven risk calculation logic.

## 📂 Repository Structure
```
third-party-risk-assessment/
│── README.md               # Project overview & setup instructions
│── LICENSE                 # Open-source license
│── .gitignore              # Ignore unnecessary files
│── docs/                    # Documentation & reports
│   ├── TPRA-Guide.md        # Step-by-step risk assessment guide
│   ├── Vendor-Risk-Checklist.md  # Vendor assessment checklist
│   ├── Compliance-Frameworks.md  # Compliance standards breakdown
│── src/                     # Scripts & automation
│   ├── risk_assessment.py   # Python script for risk evaluation
│   ├── risk_dashboard.ipynb # Jupyter Notebook for risk visualization
│── data/                    # Sample vendor data & reports
│   ├── vendors_sample.csv   # Example vendor data
│   ├── risk_scores.json     # Sample risk scores
│── configs/                 # Config files
│   ├── settings.yaml        # Risk scoring parameters
│── reports/                 # Risk assessment reports
│   ├── sample_assessment.pdf # Example assessment report
```

## 🔧 Installation & Setup
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Jupyter Notebook
- Pandas, NumPy, Matplotlib (for data processing & visualization)

### Clone the Repository
```bash
git clone https://github.com/tebellombhele/TPRA-Project.git
cd TPRA-Project
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## 🛠 Usage
### 1️⃣ Running Risk Assessment
Execute the script to analyze vendor risk levels:
```bash
python src/risk_assessment.py
```

### 2️⃣ Visualizing Risk Scores
Open Jupyter Notebook to generate a risk dashboard:
```bash
jupyter notebook src/risk_dashboard.ipynb
```

## 📖 Documentation
Refer to the [docs](./docs) folder for detailed guides on risk assessment, compliance frameworks, and best practices.

## 🤝 Contributing
We welcome contributions! To contribute:
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit changes and push.
4. Submit a pull request.

## 📜 License
This project is licensed under the [MIT License](LICENSE).