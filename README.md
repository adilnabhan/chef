# 🍳 KuriousChef — Django + React Recipe App

KuriousChef is a full-stack web application built with **Django (Backend)** and **React (Frontend)** that allows users to search, view, and explore recipes with detailed cooking instructions, ingredients, and tips.

---

## 🚀 Features

* 🔐 User Authentication (Login / Register)
* 🍲 Search Recipes (via API)
* 📖 View Recipe Details (ingredients, instructions, images)
* 🤖 AI Cooking Assistant (chat support for recipes & cooking help)
* ❤️ Save / Favorite Recipes *(optional if implemented)*
* 📱 Responsive UI (mobile + desktop)
* 🌐 REST API with Django REST Framework

---

## 🛠️ Tech Stack

**Frontend**

* React.js
* Axios
* CSS / Bootstrap (or your styling)

**Backend**

* Django
* Django REST Framework
* Python

**Database**

* SQLite (development)
* PostgreSQL (production recommended)

**Other**

* Spoonacular API (for recipes)
* Git & GitHub
* CORS Headers

---

## 📂 Project Structure

```
chef/
│
├── backend/        # Django Backend
│   ├── manage.py
│   ├── requirements.txt
│   └── ...
│
├── frontend/       # React Frontend
│   ├── package.json
│   └── ...
│
└── .gitignore
```

---

## ⚙️ How to Run Locally

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/chef.git
cd chef
```

---

### 2️⃣ Backend Setup (Django)

```bash
cd backend

python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # Linux/Mac

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

Backend runs at → **http://127.0.0.1:8000/**

---

### 3️⃣ Frontend Setup (React)

Open new terminal:

```bash
cd frontend
npm install
npm start
```

Frontend runs at → **http://localhost:3000/**

---

## 🔑 Environment Variables

Create `.env` file in backend:

```
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
SPOONACULAR_API_KEY=your_api_key
```

---

## 🌍 API Endpoints (Example)

* `/api/recipes/` → Get recipes
* `/api/login/` → User login
* `/api/register/` → User register

*(Modify based on your project)*

---

## 📦 Build for Production

```bash
cd frontend
npm run build
```

---

## 👨‍💻 Author

**Adil Nabhan**
GitHub: https://github.com/adilnabhan

---

## ⭐ Future Improvements

* Deploy to cloud (Render / AWS / Railway)
* Add Docker support
* Add user favorites & history
* Improve AI cooking assistant
* Add payment / premium recipes *(optional)*

---

## 📜 License

This project is for learning & educational purposes.
