import openai

# Set up your OpenAI API credentials
openai.api_key = "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"

# Read the story from the text file
with open("story.txt", "r") as file:
    story = file.read()

def generate_response(prompt):
    # Use GPT-3 to generate response based on input prompt
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=prompt,
      max_tokens=100,
      n=1,
      stop=None,
      temperature=0.7
    )
    if response.choices:
        output = response.choices[0].text.strip()
        return output
    else:
        print(f"OpenAI API error: {response}")
        return ""

# Start the conversation with the user
print("Hello im Tessa! How can I help you today?")
story_prompt = story + "\n\nAI Bot?:"

while True:
    user_input = input("User: ")
    if user_input.lower() == "quit":
        print("Tessa: Goodbye!")
        break
    elif "start" in user_input.lower():
        print("Tessa: Sure! Go ahead and ask me a question.")
    elif "009" in user_input.lower():
        print("Training mode is activated. You can say now")
        training_text = input(".| ")
        with open("story.txt", "a") as file:
            file.write(training_text)
        print("Okay! noted.")
    else:
        prompt = story_prompt + " " + user_input
        response = generate_response(prompt)
        if response:
            print("Tessa: " + response)
        else:
            print("Tessa: I'm sorry, I didn't understand. Can you please rephrase your question?")
