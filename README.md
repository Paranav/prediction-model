---

# 🏠 Prediction Model

A simple **Linear Regression-based prediction API** that estimates house prices using **rooms** and **square footage (sqft)** as input features.
The model learns weights (`rooms_weight`, `sqft_weight`, `bias`) during training and uses them for predictions.

---

## 🚀 Setup

Clone the repository and set up the environment:

```bash
git clone https://github.com/Paranav/prediction-model.git
cd prediction-model

# Activate virtual environment
venv\Scripts\activate.bat

# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn app:app --host <host> --port <port>
```

---

## 📌 API Endpoints

### 1️⃣ Get Current Weights

Returns the trained weights (`rooms_weight`, `sqft_weight`, `bias`).

**Endpoint:**

```
GET /api/v1/weights
```

**Example:**

```bash
curl --location 'http://localhost:8005/api/v1/weights'
```

---

### 2️⃣ Predict Price

Predicts house price using given **rooms** and **sqft** values.

**Endpoint:**

```
GET /api/v1/predict_price?rooms=<int>&sqft=<float>
```

**Example:**

```bash
curl --location 'http://localhost:8005/api/v1/predict_price?rooms=4&sqft=5000'
```

---

### 3️⃣ Train Model

Trains the model with a CSV file containing `rooms`, `sqft`, `price` columns.

**Endpoint:**

```
POST /api/v1/train
```

**Example:**

```bash
curl --location 'http://localhost:8005/api/v1/train' \
--form 'file=@"/C:/Users/kpara/OneDrive/Desktop/data.csv"'
```

---

### 4️⃣ Reset Weights

Resets the model weights to initial values.

**Endpoint:**

```
POST /api/v1/weights/reset
```

**Example:**

```bash
curl --location 'http://localhost:8005/api/v1/weights/reset'
```

---

## 🧮 Mathematical Model

The house price is predicted using the equation:

```
price = (rooms_weight × rooms) + (sqft_weight × sqft) + bias
```

---
