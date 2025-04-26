# นำเข้าไลบรารีที่จำเป็นสำหรับใช้งาน Google Generative AI
import google.generativeai as genai

# --- การตั้งค่าคอนฟิกเริ่มต้น ---
API_KEY = "คีย์จาก google ai studio"  # กำหนดคีย์ API ที่ใช้สำหรับยืนยันตัวตนกับบริการของ Google

# ตั้งค่าการใช้งานไลบรารีด้วย API Key ที่กำหนดไว้
genai.configure(api_key=API_KEY)

# เลือกโมเดลที่ต้องการใช้งาน ตัวอย่างนี้ใช้ 'gemini-1.5-flash' ที่สามารถใช้ได้ฟรี
model = genai.GenerativeModel('gemini-1.5-flash')

# เริ่มต้นสร้างเซสชันแชทใหม่ โดย history=[] หมายถึงไม่มีประวัติการสนทนาก่อนหน้า
chat = model.start_chat(history=[])

# แสดงข้อความแจ้งเตือนผู้ใช้ว่าเริ่มต้นใช้งานแชทกับ Gemini แล้ว หากต้องการออกให้พิมพ์ 'quit'
print("กำลังสนทนากับ Gemini (พิมพ์ 'quit' เพื่อออกจากโปรแกรม)...")

# วนลูปรับข้อความจากผู้ใช้ทีละบรรทัด และส่งไปที่โมเดลเพื่อรับคำตอบ
while (prompt := input("คุณ: ").strip()) != 'quit':
    # ส่งข้อความที่ผู้ใช้ป้อนให้โมเดลประมวลผลและตอบกลับ
    response = chat.send_message(prompt)
    # แสดงผลคำตอบที่ได้รับจากโมเดล Gemini
    print(f"Gemini: {response.text}")

# เมื่อผู้ใช้พิมพ์ 'quit' โปรแกรมจะออกจากลูปและแสดงข้อความสิ้นสุดการสนทนา
print("จบการสนทนาแล้ว.")
