import openai
import random
import time

openai.api_key = "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"

def generate_random_text():
    decision = input("Enter a prompt for the AI model to generate text: ")
    textSize = random.randint(80, 140)
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=decision, 
        max_tokens=textSize,
        n=1,
        stop=None,
        temperature=random.uniform(0.5, 1.0)
    )

    response.choices[0].text = "".join(response.choices[0].text.splitlines())
    time.sleep(0.5)
    #replace b` with b' to fix the error
    
    
    return str(response.choices[0].text.strip().encode('utf-8').decode('utf-8'))


print(generate_random_text())