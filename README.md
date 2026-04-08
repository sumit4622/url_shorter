# 🔗 URL Shortener Project

A robust URL shortening service built with **Django 5.x** and **Python**. This project features a full CI/CD pipeline, automated testing, and a clean backend architecture.

---

## 🚀 Features
* **Short Link Generation:** Converts long URLs into manageable short links.
* **Redirection:** High-speed redirection to the original URL.
* **Analytics:** Tracks total clicks for each link.
* **CI Integration:** Automated testing on every push via GitHub Actions.
* **Responsive UI:** Clean templates for link management.

## 🛠️ Tech Stack
* **Backend:** Django, Django Rest Framework (DRF)
* **Database:** SQLite (Development)
* **Environment:** Ubuntu Linux
* **CI:** GitHub Actions

---

## 📁 Project Structure
```text
.
├── .github/workflows/   # CI/CD Pipeline (GitHub Actions)
├── url_shorter/         # Django Project Root
│   ├── manage.py        # Project Management Script
│   └── ...              # Apps and Settings
├── requirement.txt      # Project Dependencies
└── venv/                # Local Virtual Environment (Ignored by Git)
