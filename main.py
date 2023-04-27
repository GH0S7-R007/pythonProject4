import openai
from flask import Flask, request, render_template

app = Flask(__name__)

# Set up your OpenAI API credentials
openai.api_key = "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"

# Read the story from the text file
with open("story.txt", "r") as file:
    story = file.read()

# Define a function to generate responses
def generate_response(prompt):
    response = ""
    # Use GPT-3 to generate response based on input prompt
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=prompt,
      max_tokens=100,
      n=1,
      stop=None,
      temperature=0.7
    )
    return response.choices[0].text.strip()

# Define the routes and views for the Flask app
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        prompt = story_prompt + " " + user_input
        response = generate_response(prompt)
        return render_template('index.html', response=response)
    return render_template('index.html')

# Start the conversation with the user
print("Hello, I'm Tessa! How can I help you today? (Type 'start' to begin or 'quit' to exit)")
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
        print("Tessa: " + response)

if __name__ == '__main__':
    app.run(host='172.20.10.13', port=5000, debug=True)
