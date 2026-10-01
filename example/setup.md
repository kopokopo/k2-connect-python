# K2 Connect Python Example — Setup

This guide explains how to set up and run the K2 Connect Python example locally.

## Requirements

Make sure you have:

* Python 3
* `pip`
* Git
* A Kopo Kopo developer account with API credentials
  * Client ID
  * Client secret
  * Api Key

Check your Python installation:

```bash
python3 --version
```

On some systems, use:

```bash
python --version
```

---

## 1. Clone the repository

```bash
git clone https://github.com/kopokopo/k2-connect-python.git
cd k2-connect-python/example
```

---

## 2. Create a virtual environment

Create a Python virtual environment inside the example directory:

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

Once activated, your terminal should show something similar to:

```text
(.venv) $
```

---

## 3. Install dependencies


Install the example's dependencies:

```bash
pip install -r ../requirements.txt
```

---

## 4. Configure Kopo Kopo credentials

The example requires Kopo Kopo API credentials.

Create a local environment file:

```bash
touch .env
```

Do **not** commit this file to Git.

Add your credentials to `.env` using the variable names expected by the example:

```dotenv
CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
API_KEY=your_api_key
BASE_URL=https://sandbox.kopokopo.com/
```

---


## 5. Run the example

With the virtual environment activated:

```bash
python app.py
```

For example, if the entry point is `app.py`:

```bash
python app.py
```

---
