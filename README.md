# YouTube-Video-Manager
A simple **Command Line Interface (CLI) application** built using **Python** and **MongoDB** that allows users to manage YouTube videos.
This project demonstrates **CRUD operations** (Create, Read, Update, Delete) using **PyMongo** with proper **exception handling**.

---

## 🚀 Features

- Add new videos
- List all videos
- Update existing videos
- Delete videos
- MongoDB Atlas cloud database integration
- Exception handling for invalid inputs and database errors

---

## 🛠️ Technologies Used

- Python 3
- MongoDB Atlas
- PyMongo
- BSON ObjectId
- Virtual Environment (venv)

---

## 📂 Project Structure

youtube-manager/
│
├── main.py # Main application file
├── README.md # Project documentation
├── venv/ # Virtual environment (not pushed to GitHub)
└── .gitignore


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/youtube-manager.git
cd youtube-manager
2️⃣ Create and activate virtual environment
python -m venv venv
Windows

venv\Scripts\activate
Mac / Linux

source venv/bin/activate
3️⃣ Install dependencies
pip install pymongo
4️⃣ Configure MongoDB Atlas
Create a MongoDB Atlas cluster

Add a database user

Whitelist your IP (0.0.0.0/0)

Update the connection string in the code:

MongoClient("mongodb+srv://<username>:<password>@cluster0.mongodb.net/ytmanager")
⚠️ Do NOT expose credentials in production. Use environment variables.

▶️ How to Run the Application
python main.py
📋 Menu Options
1. List all videos
2. Add a new video
3. Update a video
4. Delete a video
5. Exit
🧪 Example Document in MongoDB
{
  "_id": ObjectId("65b8e9f1c8a1d3c7a4e2b9aa"),
  "name": "Python MongoDB Tutorial",
  "time": "15:30"
}
❗ Error Handling
The application handles:

Invalid MongoDB ObjectId

Database connection errors

Empty user input

Unexpected runtime errors

📌 Learning Outcomes
Python–MongoDB integration

CRUD operations using PyMongo

Exception handling in Python

CLI application design

Working with MongoDB Atlas

📈 Future Improvements
Input validation for video time format

Logging instead of print statements

Environment variable support for credentials

Web version using Flask or FastAPI
