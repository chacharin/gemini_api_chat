🧑‍💻 Basic AI Chatbot with Gemini – Lesson Workbook
===============================================

**Purpose** – นี่คือชุดบทเรียนสำหรับผู้เริ่มต้นสร้าง *AI Chatbot* ด้วยภาษา Python 3 และโมเดล **Gemini** ผ่านไลบรารี `google‑generativeai`  เรียนรู้ตั้งแต่สคริปต์แชทพื้นฐาน → เพิ่ม System Instruction → สร้าง GUI ด้วย **Streamlit**

------------------------------------------------------------
1. โครงไฟล์บทเรียน
------------------------------------------------------------
- `00-requirements.txt`  – รายการไลบรารี (`google-generativeai`, `streamlit`)
- `01-simple_chat.py`    – แชท CLI พื้นฐาน ไม่มี System Instruction
- `02-custom_chat.py`    – สาธิตการเพิ่ม **System Instruction & temperature** (ปรับบทบาทบอตได้ตามใจ)
- `03-streamlit_chat.py` – สร้าง **GUI** แชทแบบทันสมัยด้วย Streamlit

> *หมายเหตุ* ไฟล์ตัวอย่างฝัง API Key ไว้เพื่อความสะดวกในห้องเรียน **ห้าม** ใช้คีย์จริงในโค้ดสาธารณะ

------------------------------------------------------------
2. เตรียมเครื่องมือ (Windows 10/11)
------------------------------------------------------------
1) ติดตั้ง **Python 3.10** (เลือก *Add Python to PATH*) <https://www.python.org/downloads/release/python-3100/>  
2) ติดตั้ง **VS Code** และส่วนขยาย *Python* <https://code.visualstudio.com/download>

> เปิด *PowerShell* ด้วยสิทธิ์ Admin แล้วตั้งค่า Execution Policy ชั่วคราว:
> ```powershell
> Set-Executionpolicy -ExecutionPolicy RemoteSigned -Scope Process
> ```

------------------------------------------------------------
3. สร้าง Virtual Environment
------------------------------------------------------------
```powershell
python -m venv ai_chatbot
.\ai_chatbot\Scripts\Activate
```

------------------------------------------------------------
4. ติดตั้งไลบรารี
------------------------------------------------------------
```powershell
pip install -r 00-requirements.txt
```

------------------------------------------------------------
5. ตั้งค่า Gemini API Key (แนะนำวิธีปลอดภัย)
------------------------------------------------------------
- ใช้ Environment Variable หรือ `.streamlit/secrets.toml` แทนการฮาร์ดโค้ดคีย์

------------------------------------------------------------
6. รันสคริปต์ตามลำดับ
------------------------------------------------------------
A) สคริปต์แชทพื้นฐาน
```powershell
python 01-simple_chat.py
```
B) สคริปต์เพิ่ม System Instruction
```powershell
python 02-custom_chat.py
```
C) GUI Streamlit
```powershell
streamlit run 03-streamlit_chat.py
```
แล้วเปิดเบราว์เซอร์ที่ <http://localhost:8501>

------------------------------------------------------------
7. Deploy ชั่วคราวด้วย **ngrok**
------------------------------------------------------------
ต้องการให้เพื่อน/อาจารย์เข้าถึงแชทบอทจากภายนอก (โดยไม่ตั้งค่า Router):

1) ดาวน์โหลด & ติดตั้ง **ngrok** → <https://ngrok.com/download>
2) สมัครบัญชีเพื่อรับ **Authtoken** และเชื่อมโยงกับเครื่อง:
```powershell
ngrok config add-authtoken *******TOKEN*******
```
3) ในเทอร์มินัล **แยกอีกหน้าต่าง** ปล่อยให้ Streamlit รันตามข้อ 6C ก่อน  
4) เปิดพอร์ต 8501 ผ่าน ngrok:
```powershell
ngrok http 8501
```
5) จะเห็น URL รูปแบบ `https://<random domain name>.ngrok.io`  
   ส่งลิงก์นี้ให้ใครก็ได้เข้ามาทดสอบแชทบอทของคุณ ✨

> **Tip**: หากต้องการโดเมนสวย ๆ หรือรีไดเรกต์หลายพอร์ต ใช้บัญชีเสียเงินของ ngrok หรือบริการ Cloud อื่น ๆ

------------------------------------------------------------

Happy Learning & Happy Coding! 🚀

