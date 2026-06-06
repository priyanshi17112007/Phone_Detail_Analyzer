# 📱 Phone Detail Analyzer

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black.svg)
![API](https://img.shields.io/badge/API-Integration-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A modern **OSINT-inspired Phone Number Analysis Platform** built with **Python, Flask, HTML, CSS, and JavaScript**. The application validates phone numbers, retrieves telecom metadata, and presents results through a responsive web dashboard.

Designed as a portfolio project to demonstrate **API integration, backend development, frontend interaction, and secure application architecture**.

---

# 🌟 Features

### ✅ Phone Number Validation

* Verify whether a phone number is valid.
* Support for international formats.
* Automatic formatting and normalization.

### ✅ Carrier Information

* Detect telecom operator.
* Display carrier metadata when available.
* Identify country and region details.

### ✅ Real-Time API Integration

* Fetch live data from external phone lookup services.
* Dynamic result rendering without page reloads.
* Fast and responsive user experience.

### ✅ Secure Configuration Management

* API keys stored separately from source code.
* Sensitive credentials protected using `.gitignore`.
* Modular configuration structure.

### ✅ User-Friendly Dashboard

* Clean and responsive interface.
* Instant search results.
* Mobile-friendly design.

---

# 🏗️ Project Structure

```text
Phone_Detail_Analyzer/
│
├── app.py
│   ├── Flask application
│   ├── API routes
│   └── Business logic
│
├── config.py
│   ├── API credentials
│   └── Environment configuration
│
├── requirements.txt
│   └── Project dependencies
│
├── templates/
│   └── index.html
│
└── README.md
```
# ⚙️ Technology Stack

| Technology   | Purpose               |
| ------------ | --------------------- |
| Python       | Backend Development   |
| Flask        | Web Framework         |
| HTML5        | Structure             |
| CSS3         | Styling               |
| JavaScript   | Dynamic Functionality |
| REST APIs    | Phone Data Retrieval  |
| Git & GitHub | Version Control       |

---

# 🚀 Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/priyanshi17112007/Phone_Detail_Analyzer.git
cd Phone_Detail_Analyzer
```

## 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 4️⃣ Configure API Keys

Create a file named:

```python
config.py
```

Add:

```python
class Config:
    API_KEY = "YOUR_API_KEY"
    API_URL = "YOUR_API_ENDPOINT"
```

## 5️⃣ Run Application

```bash
python app.py
```

Visit:

```text
http://127.0.0.1:5000
```

---

# 📊 Application Workflow

```text
User Input
    │
    ▼
Phone Number Submission
    │
    ▼
Flask Backend
    │
    ▼
External Lookup API
    │
    ▼
Process Response
    │
    ▼
Generate Results
    │
    ▼
Display on Dashboard
```

---

# 🔒 Security Practices

* API keys excluded from GitHub.
* Configuration separated from application logic.
* Secure environment variable support.
* Input validation before API requests.
* Error handling for failed API calls.

---

# 🎯 Learning Outcomes

This project demonstrates:

* REST API Integration
* Flask Development
* Frontend & Backend Communication
* JSON Handling
* Secure Credential Management
* Responsive Web Design
* Project Structuring Best Practices

---

## 🔮 Future Scope & Enhancements

* [ ] Display phone number owner's name using verified lookup services.
* [ ] Detect carrier/operator information more accurately.
* [ ] Show number type (Mobile, Landline, VoIP, Business).
* [ ] Add spam and fraud risk detection.
* [ ] Save previous searches for quick access.
* [ ] Export search results as PDF reports.
* [ ] Integrate multiple phone lookup APIs for better accuracy.
* [ ] Add user login and personal search history.
* [ ] Create a modern analytics dashboard with charts.
* [ ] Support bulk phone number verification from CSV files.
* [ ] Add real-time country and region detection.
* [ ] Build a REST API version for developers.
* [ ] Deploy the application on cloud platforms.
* [ ] Add AI-powered insights and recommendations.

# 📜 License

This project is licensed under the MIT License.

---

# 👩‍💻 Author
Priyanshi Sharma
Agentic AI Developer | Python Programmer | API Integration Enthusiast | Open Source Contributor
If you found this project useful, consider giving it a ⭐ on GitHub.
