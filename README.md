# UBS Hackathon Project

## 🚀 Overview
This project was built for the UBS Hackathon.  
It is a Python FastAPI application that runs locally using **Uvicorn**.

---

## 📦 Requirements
- Python 3.9 or above
- Pip package manager

Install dependencies with:

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt` yet, here’s a minimal one for FastAPI:

```txt
fastapi
uvicorn
```

---

## ▶️ Running the Project

### Option 1: Run directly
```bash
python -m uvicorn app:app --reload --host 127.0.0.1 --port 8000
```

### Option 2: Use helper file
If you don’t want to type the long command every time, you can run:

- **Windows**: double-click `run.bat`  
- **Linux/Mac**: run `./run.sh` (after `chmod +x run.sh`)  
- **Cross-platform**: `python run.py`

---

## 🗂️ Project Structure
```
.
├── app/                 # Main application folder
│   ├── __init__.py
│   ├── main.py          # Entry point (FastAPI app)
│   └── ...              # Other modules
├── requirements.txt     # Dependencies
├── run.bat              # Windows start script
├── run.sh               # Linux/Mac start script
├── run.py               # Python wrapper for uvicorn
├── .gitignore           # Ignored files
└── README.md            # Project documentation
```

---

## 🛠️ Development Notes
- The API will be live at:  
  👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

- Interactive API docs available at:  
  👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
