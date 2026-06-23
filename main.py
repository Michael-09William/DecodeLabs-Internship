import ollama

# 1. Model
MODEL_NAME = 'phi3'

# 2. Memory Setting
chat_history = []
MAX_HISTORY_TURNS = 15

print(f"🤖 [DecodeLabs] Stateful LOCAL Chatbot ({MODEL_NAME}) Loaded successfully!")
print('Write EXIT to ending the session\n' + "-"*40)

while True:
    # 3. Structural Validation Gate
    user_input = input('You: ').strip()

    if user_input.upper() == 'EXIT':
        print('Sess/ion Ended.')
        break
    if not user_input:
        print('⚠️ [Guard Gate]: The Request Is Empty! The Sending Is Blocked')
        continue

    # 4. Ingest & Append
    chat_history.append({
        "role": "user",
        "content": user_input
    })

    try:
        # 5. Transmit
        response = ollama.chat(
            model=MODEL_NAME,
            messages=chat_history
        )
        
        model_reply = response['message']['content']

        print(f"\nAI: {model_reply}\n" + "-"*40)
        
        # 7. Append AI Reply 
        chat_history.append({
            "role": "assistant", 
            "content": model_reply
        })

        # 8. Memory Management
        if len(chat_history) > (MAX_HISTORY_TURNS * 2):
            chat_history = chat_history[2:]

    except Exception as e:
        print(f"❌ Error Occurred: {e}")
        chat_history.pop()