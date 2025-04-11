
# Project Setup Guide

Welcome! Follow these steps to set up your virtual environment and install project dependencies.

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-project.git
cd your-project
```

## 2. Create a Virtual Environment

Make sure you have Python installed (preferably 3.8+). Then create a virtual environment:

```bash
python -m venv venv
```

> **Tip:** On some systems, you might need to use `python3` instead of `python`.

## 3. Activate the Virtual Environment

- **On Windows:**

    ```bash
    venv\Scripts\activate
    ```

- **On macOS/Linux:**

    ```bash
    source venv/bin/activate
    ```

You should now see the virtual environment name (like `(venv)`) at the beginning of your terminal prompt.

## 4. Install Dependencies

Make sure your virtual environment is active, then run:

```bash
pip install -r requirements.txt
```

This will install all necessary packages listed in `requirements.txt`.

Type below command in the terminal 
pytest tests/test_login.py -v
pytest tests/test_pim.py -v
