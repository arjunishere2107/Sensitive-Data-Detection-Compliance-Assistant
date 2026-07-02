import os
import requests
import streamlit as st
import pandas as pd

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Sensitive Data Assistant",
    page_icon="🛡",
    layout="wide"
)

st.markdown("""
<style>
.main{
    padding-top:2rem;
}
.stButton>button{
    width:100%;
    border-radius:10px;
    height:45px;
    font-weight:bold;
}
.stDownloadButton>button{
    width:100%;
    border-radius:10px;
    height:45px;
    background:#0E9F6E;
    color:white;
}
div[data-testid="metric-container"]{
    background:#f8f9fa;
    border:1px solid #e6e6e6;
    padding:15px;
    border-radius:12px;
}
</style>
""", unsafe_allow_html=True)

st.title("🛡 Sensitive Data Detection & Compliance Assistant")
st.caption("Upload a document • Detect sensitive information • Generate compliance reports • Chat with your document")

uploaded_file = st.file_uploader(
    "📂 Upload PDF / TXT / CSV",
    type=["pdf", "txt", "csv"]
)

if uploaded_file:

    files = {
        "file": (
            uploaded_file.name,
            uploaded_file.getvalue()
        )
    }

    with st.spinner("🔍 Analyzing document..."):

        response = requests.post(
            f"{BACKEND_URL}/upload/",
            files=files
        )

    if response.status_code == 200:

        result = response.json()

        st.success("✅ Analysis Completed Successfully")

        risk = result["detections"]["summary"]["overall_risk"]

        if risk == "High":
            st.error("🚨 High Risk Document")
        elif risk == "Medium":
            st.warning("⚠ Medium Risk Document")
        else:
            st.success("✅ Low Risk Document")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("📄 File", result["filename"])
        c2.metric("📝 Characters", result["characters"])
        c3.metric("🧩 Chunks", result["chunks"])
        c4.metric("🛡 Risk", risk)

        st.divider()

        st.subheader("🔍 Sensitive Data Detection")

        detections = result["detections"]["detections"]

        if detections:

            df = pd.DataFrame(detections)

            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True
            )

        else:

            st.success("🎉 No sensitive information detected.")

        st.divider()

        st.subheader("🤖 AI Compliance Summary")

        st.info(result.get("summary", "Summary unavailable."))

        st.divider()

        with st.expander("📄 Document Preview"):

            st.text(result["preview"])

        st.divider()

        st.subheader("💬 Chat with Document")

        question = st.text_input(
            "Ask a question about the uploaded document"
        )

        if st.button("Ask AI"):

            if question.strip():

                payload = {
                    "document_id": result["document_id"],
                    "question": question
                }

                chat = requests.post(
                    f"{BACKEND_URL}/chat/",
                    json=payload
                )

                if chat.status_code == 200:

                    st.success(chat.json()["answer"])

                else:

                    st.error(chat.text)

        st.divider()

        st.subheader("📥 Download Compliance Report")

        report_path = result.get("report")

        if report_path:

            absolute_path = os.path.abspath(
                os.path.join("..", "backend", report_path)
            )

            if os.path.exists(absolute_path):

                with open(absolute_path, "rb") as pdf:

                    st.download_button(
                        "⬇ Download PDF Report",
                        pdf,
                        file_name="Compliance_Report.pdf",
                        mime="application/pdf"
                    )

    else:

        st.error(response.text)