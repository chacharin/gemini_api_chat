import streamlit as st
import google.generativeai as genai

# ---------------- Page & App setup ------------------
st.set_page_config(
    page_title="แชทบอทสุดยอดนักปลูก 🌱",
    page_icon="🌱",
    layout="centered",
)

st.title("🌱 แชทบอทสุดยอดนักปลูก")
st.caption("ให้คำแนะนำการปลูกพืชผักสวนครัวด้วย Gemini 1.5-Flash")

# ---------------- API-Key (Embedded) ------------------
API_KEY = "AIzaSyBIVkeXW7JpZzQxJZY72ZlO0lHxFYEpuMk"  # ⛔️ คีย์ฝังตรงนี้ ไม่ปลอดภัยสำหรับโค้ดสาธารณะ!

genai.configure(api_key=API_KEY)

# ---------------- Gemini model setup ----------------
SYSTEM_INSTRUCTION = (
    "คุณเป็นสุดยอดเกษตรกรที่มีความสามารถมากในการปลูกพืชผักสวนครัว "
    "โปรดให้คำแนะนำฉันเป็นภาษาไทย"
)
GENERATION_CONFIG = {"temperature": 0.7}

# Initialise the model & chat object once per session ----------------
if "chat" not in st.session_state:
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction=SYSTEM_INSTRUCTION,
        generation_config=GENERATION_CONFIG,
    )
    st.session_state.chat = model.start_chat(history=[])

chat = st.session_state.chat

# ---------------- Display previous messages ----------------
for turn in chat.history:
    role = "assistant" if turn.role == "model" else "user"
    with st.chat_message(role):
        st.markdown(turn.parts[0].text)

# ---------------- Prompt box ----------------
if prompt := st.chat_input("ถามคำถามการปลูกพืชผักที่นี่ แล้วกด Enter …"):
    # Show user message immediately
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get response from Gemini
    try:
        response = chat.send_message(prompt)
        with st.chat_message("assistant"):
            st.markdown(response.text)
    except Exception as err:
        st.error(f"เกิดข้อผิดพลาด: {err}")
