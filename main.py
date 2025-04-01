from core import chatbot_genai, chatbot_genai_with_image
from textToSpeech import text_to_speech

def main():
    # Step 1: Speech to Text
    #text = speech_to_text()
    text = input("Type Anything:")
    
    if text:
        # Step 2: Chatbot response
        #response = chatbot_llm(text)
        #response = chatbot_genai(text)
        response = chatbot_genai_with_image(text, 'bill3.jpg')
        print("Chatbot response:", response)
        
        # Step 3: Text to Speech
        #text_to_speech(response)
        text_to_speech(response)

if __name__ == "__main__":
    main()
