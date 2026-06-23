import ollama

MODEL_NAME='phi3'

def generate_marketing_copy_local(product_name: str, product_desc: str, platform: str, tone: str, temperature: float = 0.7, top_p: float = 0.9):

    prompt_template = f"""
    You are an expert copywriter. Your task is to write a highly engaging marketing copy.
    
    Product Name: {product_name}
    Product Description: {product_desc}
    Target Platform: {platform}
    Desired Tone: {tone}
    
    Requirements:
    - Tailor the formatting, length, and style specifically for {platform}.
    - Maintain a {tone} tone throughout the text.
    - Include relevant call-to-actions (CTAs) or hashtags if appropriate for the platform.
    
    Marketing Copy:
    """

    response=ollama.generate(
        model=MODEL_NAME,
        prompt=prompt_template,
        options={'temperature':temperature,
                 'top_p':top_p})
    return response['response']

if __name__ == "__main__":
    name = "SmartDesk 2.0"
    desc = "An ergonomic standing desk with built-in wireless charging and automated posture reminders."
    target_platform = "LinkedIn"
    desired_tone = "Professional and Innovative"
    
    print("Generating copy locally via Ollama...\n")
    result = generate_marketing_copy_local(
        product_name=name,
        product_desc=desc,
        platform=target_platform,
        tone=desired_tone,
        temperature=0.9,
        top_p=0.9
    )
    
    print("="*40)
    print(f"Generated Copy for {target_platform}:")
    print("="*40)
    print(result)