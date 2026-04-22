# Zebu Asset Tracker

### 1. What is this?
A simple, professional tool for tracking animation assets (like shots and characters). It uses a **Next.js** frontend to manage the data and a **Flask (Python)** backend to store and verify information. It's built to be fast, stable, and easy to understand for technical interviews.

---

### 2. How to Setup

#### Backend (Flask)
1. Navigate to the `backend` folder.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the server:
   ```bash
   python3 app.py
   ```
   *The backend will run on `http://127.0.0.1:5002`.*

#### Frontend (Next.js)
1. Navigate to the frontend folder.
2. Install nodes:
   ```bash
   npm install
   ```
3. Start the app:
   ```bash
   npm run dev
   ```

---

### 3. About the APIs

The API follows a **RESTful structure**. This means instead of having random URLs for everything, we group actions by "Resources."

- **`/api/assets` (GET/POST)**: Used for listing all assets or adding a brand-new one.
- **`/api/assets/<id>` (PUT/DELETE)**: Used for updating or deleting a specific asset by its ID.
- **`/api/run-tests` (GET)**: A specialized diagnostic route that runs the system health check and returns a report.

**Why I chose this structure?**
I chose this RESTful design because it keeps the API clean and predictable. It is a reliable way to organize data actions and ensures the app is easy to maintain.

---

### 4. Project Architecture

The project is split into two independent parts:
- **Client-Side (Frontend)**: Handles the "look and feel" (UI) and user interactions.
- **Server-Side (Backend)**: Handles the logic, data storage, and automated testing.

They talk to each other using **JSON** over Port 5002. This separation makes the app more stable because the frontend doesn't need to know *how* the data is stored—it just asks the API for it.

---

### 5. Design Pattern and Tradeoffs

#### Pattern: In-Memory CRUD
The app uses a **Global List** in Python to store data instead of a heavy database like MySQL or SQL Server.

**Why I chose this (The Tradeoff):**
- **Pros**: It's incredibly fast, requires zero configuration, and works immediately on any machine. It proves the system logic is correct without the overhead of a database.
- **Cons**: Since the data is in "RAM memory," it is lost when the server restarts. 

**My Decision**: I traded "Persistence" for "Simplicity and Stability." In a heavy production app, I would swap out the Python list for a database like PostgreSQL, but for this project, **simplicity is the safest and most reliable choice.**
