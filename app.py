import streamlit as st
from extractor import extract_financial_text
from analyzer import analyze_financials

st.title("Fundamental Analyzer (MVP)")

uploaded_file = st.file_uploader("Ladda upp en årsrapport (PDF)", type=["pdf"])

if uploaded_file:
    with st.spinner("Analyserar rapporten..."):
        raw_text = extract_financial_text(uploaded_file)
        metrics = analyze_financials(raw_text)

    if metrics:
        st.success("Analys klar!")
        st.subheader("Nyckeltal")
        for key, value in metrics.items():
            st.metric(label=key, value=value)
    else:
        st.warning("Kunde inte hitta tillräckligt med data i rapporten.")
