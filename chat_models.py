

import anthropic

from chat_flow.normal_flow import salesAgent

class anthropic_salesAgent(salesAgent):
    def __init__(self, MODEL, KEY):

        if MODEL == 'claude':
            MODEL="claude-3-opus-20240229"
        super().__init__(MODEL, KEY)
        
        self.client=anthropic.Anthropic(api_key=self.KEY)

    def talk_to_seller(self, query, history):
        history += [{
            "role": "user", 
            "content": query
        }]


        stream = self.client.messages.stream(
            max_tokens=1024,
            messages=history,
            model=self.MODEL,
        ) 

        for r in stream.text_stream:
            yield r
            

import google.generativeai as genai

from chat_flow.normal_flow import salesAgent

class gemini_salesAgent(salesAgent):
    def __init__(self, MODEL, KEY):

        if MODEL == 'gemini':
            MODEL='gemini-pro'
        super().__init__(MODEL, KEY)
        genai.configure(api_key=KEY)
        self.chat = genai.GenerativeModel(self.MODEL).start_chat(history=[])

    def talk_to_seller(self, query, _):

        response = self.chat.send_message(query, stream=True)
        
        for r in response:
            yield r.text  
        
      