import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import pickle

# Load dataset
df = pd.read_csv("customer_purchase_data.csv")

# Encode categorical features
le_device = LabelEncoder()
le_ref = LabelEncoder()
df['Device'] = le_device.fit_transform(df['Device'])
df['Referral'] = le_ref.fit_transform(df['Referral'])

# Features and target
X = df.drop('Purchased', axis=1)
y = df['Purchased']

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save model and encoders
with open("model.pkl", "wb") as f:
    pickle.dump((model, le_device, le_ref), f)
