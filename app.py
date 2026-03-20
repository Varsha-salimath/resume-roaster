import streamlit as st
import google.generativeai as genai
import pdfplumber
import os
from dotenv import load_dotenv
import html
import re
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

load_dotenv()

st.set_page_config(
    page_title="Resume Roaster ✨",
    page_icon="🔥",
    layout="wide",
)

st.markdown("""
<style>
    h1 {
        color: #ff4b4b;
        text-align: center;
        font-weight: 800;
        letter-spacing: -1px;
    }
    .tagline {
        text-align: center;
        font-size: 1.1rem;
        color: #a0a0a0;
        margin-bottom: 2rem;
    }
    /* Force word wrapping to prevent continuous text from breaking columns and overlapping */
    .stMarkdown, p, li, span, h1, h2, h3 {
        overflow-wrap: break-word !important;
        word-wrap: break-word !important;
        word-break: break-word !important;
    }
    /* Subtle container background */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #12141a;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>Resume Roaster 🔥</h1>", unsafe_allow_html=True)
st.markdown("<p class='tagline'>We roast it so recruiters don't have to</p>", unsafe_allow_html=True)

api_key = os.getenv("GEMINI_API_KEY")

st.sidebar.title("⚙️ Settings")
if not api_key:
    api_key = st.sidebar.text_input("Gemini API Key", type="password", help="Get yours at aistudio.google.com/app/apikey")
    if not api_key:
        st.warning("Please enter your Gemini API Key in the sidebar or `.env` file to begin.")
        st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.5-flash')

def extract_text(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
    return text

def create_pdf(text):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    styles = getSampleStyleSheet()
    style = styles['Normal']
    style.fontSize = 11
    style.leading = 14
    
    story = []
    safe_text = html.escape(text)
    safe_text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', safe_text)
    safe_text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', safe_text)
    
    paragraphs = safe_text.split('\n\n')
    for p in paragraphs:
        p = p.replace('\n', '<br/>')
        story.append(Paragraph(p, style))
        story.append(Spacer(1, 12))
        
    doc.build(story)
    pdf_value = buffer.getvalue()
    buffer.close()
    return pdf_value

st.sidebar.header("📤 Upload Resume")
uploaded_file = st.sidebar.file_uploader("Must be a PDF format", type=["pdf"])

if uploaded_file is not None:
    st.sidebar.success("Upload successful!")
    
    if st.sidebar.button("Roast & Rewrite 🔥", type="primary"):
        with st.spinner("Extracting text from your PDF..."):
            resume_text = extract_text(uploaded_file)
            
        if len(resume_text.strip()) < 50:
            st.error("Could not extract enough text from the PDF. Is it an image-based PDF?")
            st.stop()

        # Added gap="large" to give columns breathing room
        col1, col2 = st.columns(2, gap="large")
        
        # Enhanced prompts for readability
        roast_prompt = f"You are a brutally honest but helpful career coach. Roast this resume. Point out weak phrases, vague bullets, missing metrics, and ATS red flags. Break your feedback down into short, highly readable bullet points with bold headers. Be funny but constructive. Here is the resume:\n\n{resume_text}"
        rewrite_prompt = f"You are an expert resume writer. Rewrite this resume with stronger action verbs, quantified achievements, and professional tone. Keep the same experiences but make them shine. Provide a clean, airy structure with bullet points. Do not write huge paragraphs. Here is the resume:\n\n{resume_text}"
        
        with col1:
            st.subheader("🔥 The Roast")
            # Using a scrollable, bordered container so it doesn't get infinitely long
            with st.container(height=650, border=True):
                with st.spinner("Generating brutally honest feedback... 😬"):
                    try:
                        roast_resp = model.generate_content(roast_prompt)
                        st.markdown(roast_resp.text)
                    except Exception as e:
                        st.error(f"Error: {e}")
                    
        with col2:
            st.subheader("✨ The Rewrite")
            # Using a scrollable, bordered container
            with st.container(height=650, border=True):
                with st.spinner("Polishing your experience... 🪄"):
                    try:
                        rewrite_resp = model.generate_content(rewrite_prompt)
                        rewritten_content = rewrite_resp.text
                        st.markdown(rewritten_content)
                    except Exception as e:
                        st.error(f"Error: {e}")
            
            # Export buttons placed outside the scrollable container for easy access
            st.write("### 📥 Download Improved Version")
            d_col1, d_col2 = st.columns(2)
            with d_col1:
                st.download_button(
                    label="📄 Download TXT",
                    data=rewritten_content if 'rewritten_content' in locals() else "",
                    file_name="Rewritten_Resume.txt",
                    mime="text/plain",
                    use_container_width=True
                )
            with d_col2:
                try:
                    if 'rewritten_content' in locals():
                        pdf_bytes = create_pdf(rewritten_content)
                        st.download_button(
                            label="📥 Download PDF",
                            data=pdf_bytes,
                            file_name="Rewritten_Resume.pdf",
                            mime="application/pdf",
                            use_container_width=True
                        )
                except Exception as e:
                    st.error(f"Failed to generate PDF: {e}")
else:
    st.info("👈 Please upload your PDF resume from the sidebar to begin.")
