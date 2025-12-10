import joblib
import streamlit as st 

model = joblib.load("models/model_logistic_reggression.pkl")
tfidf = joblib.load("models/tfidf_vectorizer.pkl")

st.title("Aplikasi Klasifikas Komentar")
st.write("Aplikasi Gabut Aja Ini Mah")
input.text_area("Masukan Komentar Anda!")

if st.buttom("Prediksi")
    if input.strip() == "":
        st.warning("Tolong Komentar Jangan Kosong")
    else:
        vector = tfidf.transform([input])
        prediction = model.prdict(vector)[0]

        label_mapping = {
            0: "Negatif"
            1: "Positif"
        }
        st.subheader("Hasil Analisis Komentar")
        st.write("**Sentiment Anda:**", label_mapping.get(prediction, prediction))
        