# dialogue.py - Contains a conversation with a bot, along with various helper functions.

from typing import Union

class Formatter():
    
    def __init__(self, template_query: Union[str, None] = "{system}\n### Dialogue:\n{dialogue}\n\n### Response:", template_dialogue: Union[str, None] = "Q: {question}\nA: {answer} {suffix or ''}\n\n", suffix: str = "", system: str = "You are a helpful bot."):
        self.templates = {
            "query": template_query,
            "dialogue": template_dialogue,
        }
        self.system = system or ""
        self.suffix = suffix
    
    def qa(self, question: str, answer: str):
        return self.templates["query"].format(question=question, answer=answer)

    def history(self, history: list):
        temp = ""
        for idx in range(0, len(history), 2):
            user = history[idx]
            bot = history[idx + 1]
            temp += self.templates["history"].format(question=user["content"], answer=bot["content"])
        if ((len(history) % 2) == 1) and bot:
            temp += "User: .\nBot:"
        return temp
    def prompt(self, query: str, history: list, stop_token: Union[str,None] = None):
        return self.system + "\n" + self.history(history, stop_token) + "\n" + query + self.suffix

class Dialogue():

    def __init__(self, bot_name: str = "bot", user_name: str = "user", dialogue_id: str = "dlgabc123", dialogue_name: str = "New Dialogue", formatter: Formatter = None):
        """Initializes a new Dialogue object."""
        self.bot = bot_name
        self.user = user_name
        self.dialogue_id = dialogue_id
        self.messages = []
        self.fmt = formatter or Formatter()

    def message(self, message):
        self.messages.append({
            "role": "user",
            "content": message
        })

    def response(self, response):
        self.messages.append({
            "role": "bot",
            "content": response
        })

    def clear(self):
        self.messages = []
    