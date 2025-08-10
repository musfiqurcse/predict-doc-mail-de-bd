import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression

data = [
    ("21/07/2023", "05/08/2023", "10/08/2025"),
    ("08/07/2023", "20/07/2023", "10/07/2025"),
    ("18/06/2023", "07/07/2023", "10/06/2025"),
    ("03/06/2023", "17/06/2023", "23/04/2025"),
    ("24/05/2023", "02/06/2023", "10/03/2025"),
    ("12/05/2023", "24/05/2023", "02/02/2025"),
    ("22/04/2023", "11/05/2023", "17/01/2025"),
    ("04/04/2023", "21/04/2023", "17/11/2024")
]

def parse_date(date_str):
    return datetime.strptime(date_str, "%d/%m/%Y")

rows = []
for start, end, docmail in data:
    start_date = parse_date(start)
    end_date = parse_date(end)
    midpoint = start_date + (end_date - start_date) / 2
    docmail_date = parse_date(docmail)
    rows.append({
        "Midpoint_ordinal": midpoint.toordinal(),
        "DocMail_ordinal": docmail_date.toordinal()
    })

df = pd.DataFrame(rows)

# Train regression model by the given date.
X = df[["Midpoint_ordinal"]]
y = df["DocMail_ordinal"]
model = LinearRegression()
model.fit(X, y)

st.title("📅 Document Submission Email Receive Date Predictor ")
st.write("_[Only for Family Reunion Visa Applicant]_")
st.write("**_Note: This is not an official Document Submission Predictor. It is designed based on previous document submission responses from the German Embassy in Bangladesh._**")
today = datetime.today().date() - timedelta(days=730)
apply_date = st.date_input("Applied date for Appointment", min_value=today)

if st.button("Predict Doc Submission Email Date"):
    apply_ord = apply_date.toordinal()
    predicted_ord = model.predict([[apply_ord]])[0]
    predicted_date = datetime.fromordinal(int(predicted_ord))
    
    st.success(f"📬 Predicted DocMail Date: **{predicted_date.strftime('%d/%m/%Y')}**")
st.write('Disclaimer: You can estimate the month and year you will likely receive your document submission email. Note that this is not an official document submission email.')