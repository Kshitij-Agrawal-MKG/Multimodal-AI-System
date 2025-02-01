from groq import Groq
from visionai import generate_image_caption, extract_text

def generate_image_description(image_path, user_request):
    prompt = """Given the following description of an image, provide an output tailored to the user’s needs. The output could be a concise summary , a creative description, or a detailed analytical report, depending on the user's specific request. Make sure the response aligns with the style and tone indicated in the user prompt. Do not generate any comment on the based of color and if ask in user request simply say no by requesting it. The optical Character Recognition of image is also provided incude that also. Image-Description:"""
    image = generate_image_caption(image_path)
    ocr = extract_text(image_path)
    result = f"{prompt}{image}Optical Character Recognition: {ocr} User-Request: {user_request}"

    api = "ENTER YOUR API KEY"
    client = Groq(api_key=api)
    completion = client.chat.completions.create(
        model="llama-3.3-70b-specdec",
        messages=[{"role": "user", "content": result}],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    output = ""
    for chunk in completion:
        output += chunk.choices[0].delta.content or ""
    return output
