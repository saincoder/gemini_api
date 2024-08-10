import google.generativeai as genai

GOOGLE_API_KEY = "AIzaSyDxoT2zDA4MmX8bRA41HAaSDAOEgg19gNI"

genai.configure(api_key=GOOGLE_API_KEY)

#Model initiation
model = genai.GenerativeModel('gemini-1.5-flash')

#Create function for get response

def getResponse(user_input):
    response = model.generate_content(user_input)
    return response.text

# user input

user_input = input('Enter your Prompts:')

model_reponse = getResponse(user_input)
print(model_reponse)
