import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load('model.pkl')

st.title("🏠 House Price Prediction App")

st.write("Enter house details below to predict the price:")

# 🧮 Numeric inputs
MSSubClass = st.number_input("MSSubClass (building class)", min_value=0, step=1)
LotArea = st.number_input("Lot Area (sq ft)", min_value=0)
OverallCond = st.number_input("Overall Condition (1-10)", min_value=1, max_value=10)
YearBuilt = st.number_input("Year Built", min_value=1800, max_value=2025)
YearRemodAdd = st.number_input("Year Remodeled", min_value=1800, max_value=2025)
BsmtFinSF2 = st.number_input("Basement Finished SF (Part 2)", min_value=0)
TotalBsmtSF = st.number_input("Total Basement SF", min_value=0)

# 🏘️ MSZoning (One-hot encoded)
st.subheader("MSZoning")
MSZoning_options = ['C (all)', 'FV', 'RH', 'RL', 'RM']
MSZoning_selected = st.selectbox("Select MSZoning", MSZoning_options)
MSZoning = [1 if MSZoning_selected == option else 0 for option in MSZoning_options]

# 🏘️ LotConfig
st.subheader("Lot Configuration")
LotConfig_options = ['Corner', 'CulDSac', 'FR2', 'FR3', 'Inside']
LotConfig_selected = st.selectbox("Select LotConfig", LotConfig_options)
LotConfig = [1 if LotConfig_selected == option else 0 for option in LotConfig_options]

# 🏗️ BldgType
st.subheader("Building Type")
BldgType_options = ['1Fam', '2fmCon', 'Duplex', 'Twnhs', 'TwnhsE']
BldgType_selected = st.selectbox("Select BldgType", BldgType_options)
BldgType = [1 if BldgType_selected == option else 0 for option in BldgType_options]

# 🪟 Exterior1st
st.subheader("Exterior Material")
Exterior1st_options = [
    'AsbShng', 'AsphShn', 'BrkComm', 'BrkFace', 'CBlock', 'CemntBd',
    'HdBoard', 'ImStucc', 'MetalSd', 'Plywood', 'Stone', 'Stucco',
    'VinylSd', 'Wd Sdng', 'WdShing'
]
Exterior1st_selected = st.selectbox("Select Exterior1st", Exterior1st_options)
Exterior1st = [1 if Exterior1st_selected == option else 0 for option in Exterior1st_options]

# 🧩 Combine all inputs
input_data = [
    MSSubClass, LotArea, OverallCond, YearBuilt, YearRemodAdd,
    BsmtFinSF2, TotalBsmtSF,
    *MSZoning,
    *LotConfig,
    *BldgType,
    *Exterior1st
]

# 🔮 Predict
if st.button("Predict House Price"):
    input_array = np.array([input_data])  # shape (1, n_features)
    prediction = model.predict(input_array)
    st.success(f"🏷️ Predicted House Price: ₹{prediction[0]:,.2f}")
