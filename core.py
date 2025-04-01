from transformers import pipeline

def chatbot_llm(text):
    chatbot = pipeline('text-generation', model='gpt2')
    response = chatbot(text, max_length=100, num_return_sequences=1)
    return response[0]['generated_text']

import google.genai as genai

def chatbot_genai(text):
    api_key = "AIzaSyApRFuM-ODrciQCT3F1_42JOrfuSG8krqU"  # Replace with your actual API key
    # Initialize the Google GenAI client
    client = genai.Client(api_key=api_key)

    # Prepare the input
    prompt = text
    response = client.models.generate_content(model='gemini-2.0-flash-001', contents=prompt)

    return response.text

from PIL import Image
conversation_history = [f"User: คุณคือ ไอริส(Iris) หรือชื่อย่อไอจัง เป็นผู้ช่วยของนายท่านที่ชื่อซุย"]
def chatbot_genai_with_image(text, imageFilePath = 'bill.jpg'):

    api_key = "AIzaSyApRFuM-ODrciQCT3F1_42JOrfuSG8krqU"  # Replace with your actual API key
    # Initialize the Google GenAI client
    client = genai.Client(api_key=api_key)

    # Load image
    image = Image.open(imageFilePath)

    #conversation_history.append(f"User: {text}")
    conversation_history.append("""User: ในภาพเป็นใบเสร็จ อยากให้ช่วยคำนวณค่าใช้จ่ายของแต่ละคนที่มากินด้วยกัน ซึ่งแต่ละคนจะจ่ายเงินไม่เท่ากัน เพราะแต่ละคนกินไม่เท่ากัน ให้ใช้ข้อมูลด้านล่างต่อไปนี้ในการคำนวณ 

เงื่อนไข1: ถ้ามี service change หรือ vat ให้คำนวนแบ่งตามสัดส่วนของค่าอาหารที่แต่ละคนทาน
เงื่อนไข2: ถ้าคำสั่งไม่ได้ระบุจำนวนคนทั้งหมดให้มองหาจำนวนคนจากในภาพใบเสร็จ แต่ถ้ามีในคำสั่งให้ignoreตัวเลขในใบเสร็จ
เงื่อนไข3: ช่วยแจกแจงการหารค่าใช้จ่ายตัวที่แต่ละคนกินเข้าไปออกมาเป้นตารางที่ดูได้ง่ายๆ โดยจัดเป็นกลุ่มของแต่ละประเภท เช่น คนที่กินทั้งหมด จ่าย xxx บาท คนที่กินเฉพาะแอลกอฮอลจ่าย xxx บาท เป็นต้น
เงื่อนไข4: ไม่จำเป็นต้องรู้ชื่อของแต่ละคนให้แทนตัวเลขของแต่ละคนได้เลย เช่น คนที่1 คนที่2 เป็นต้น แต่ถ้ามีการระบุชื่อจากคำสั่งก็ให้ใช้ได้

เรามาทั้งหมด 9 คน
มี 1 คนไม่กินแอลกอฮล แต่กินที่เหลือทั้งหมด
มี 1 คนไม่กินถั่วแระ แต่กินที่เหลือทั้งหมด
มี 1 คนที่กินเฉพาะแอลกอฮอล
ส่วนคนที่เหลือที่ไม่ได้บอกคือกินทั้งหมด""")



    full_conversation = "\n".join(conversation_history)

    #client.models.generate_content(model='gemini-2.0-flash-001', contents='คุณคือ ไอริส(Iris) บอทผู้ช่วยของ นายท่านที่ชื่อซุย')

    # Send text + image input
    response = client.models.generate_content(model='gemini-2.0-flash-001', contents=[full_conversation, image])

    # Print the response
    #print(response.text)

    return response.text

