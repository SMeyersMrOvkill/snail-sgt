# dialogue.py - Contains a conversation with a bot, along with various helper functions.

from typing import Union

class Formatter():
    """
    A class that provides formatting functionality for generating dialogue prompts.

    Args:
        template_query (Union[str, None]): The template for query prompts. Defaults to "{system}\n### Dialogue:\n{dialogue}\n\n### Response:".
        template_dialogue (Union[str, None]): The template for dialogue prompts. Defaults to "Q: {question}\nA: {answer} {suffix or ''}\n{stop_token}".
        suffix (str): The suffix to be added to the answer in dialogue prompts. Defaults to "".
        system (str): The system identifier for the bot. Defaults to "You are a helpful bot.".

    Attributes:
        templates (dict): A dictionary containing the templates for query and dialogue prompts.
        system (str): The system identifier for the bot.
        suffix (str): The suffix to be added to the answer in dialogue prompts.

    Methods:
        qa(question: str, answer: str) -> str: Formats a query prompt with the given question and answer.
        history(dialogue: list) -> str: Formats a history of dialogue prompts.
        prompt(history: list, stop_token: Union[str,None]) -> str: Formats a dialogue prompt with the given history and stop token.
    """
    def __init__(self, bot_name: str = "bot", template_query: Union[str, None] = "{system}\n### Dialogue:\n{dialogue}\n\n### Response:", template_dialogue: Union[str, None] = "Q: {question}\nA: {answer} {suffix or ''}\n{stop_token}", suffix: str = "", system: str = "You are a helpful bot."):
        self.bot = bot_name
        self.templates = {
            "query": template_query,
            "dialogue": template_dialogue,
        }
        self.system = system or ""
        self.suffix = suffix
    
    def qa(self, question: str, answer: str):
        return self.templates["query"].format(question=question, answer=answer)

    def history(self, dialogue: list):
        temp = ""
        for idx in range(0, len(dialogue), 2):
            user = self.history[idx]
            bot = self.history[idx + 1]
            temp += self.templates["history"].format(question=(user["content"] or "."), answer=bot["content"])
        if ((len(self.history) % 2) == 1) and bot:
            temp += "User: .\nBot:"
        return temp
    
    def prompt(self, history: list, stop_token: Union[str,None] = None):
        dialogue_history = history(dialogue=self.history(history), stop_token=stop_token or "")
        return "{system}\n### Dialogue:\n{dialogue}\n\n## Response:\nA:{stop_token}".format(system=self.system, dialogue=dialogue_history, stop_token=stop_token or "")

class Dialogue():
    """
    
    A class that represents a conversation with a bot.
    
    """
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
        return self.messages[-1]

    def response(self, response):
        self.messages.append({
            "role": "bot",
            "content": response
        })
        return self.messages[-1]

    def clear(self):
        self.messages = []
    
    def generate(self, raw_prompt: str, temp: float = 0.33, top_p: float = 0.95, top_k: int = 42, stop: Union[list,None] = None, max_tokens: int = 1536):
        """
        NOTE: Base class does nothing, see <REPO_ROOT>/examples/tci/phi2.ipynb for a simple, working example.
        Generates a response to the given prompt.

        Args:
            raw_prompt (str): The prompt to generate a response to.
            temp (float): The temperature of the response. Defaults to 0.33.
            top_p (float): The top p value of the response. Defaults to 0.95.
            top_k (int): The top k value of the response. Defaults to 42.
            stop (Union[list,None]): The stop tokens of the response. The 0th element is appended automatically to each dialogue step, if it exists. If empty and of type list, is assumed to be intentionally left empty. If this is None, it is assumed to be ["</s>", "\n\n", "<|end_of_text|>", "<|endoftext|>", "<|im_end|>", "###"], because these are the most commonly used stop tokens that do not interfere with ordinary chat applications.
        
        """
        # This is where a method should be, doing something.
        return self.response(raw_prompt, temp=temp, top_p=top_p, top_k=top_k, stop_token=(stop and stop[0]) or "")
    
    def __call__(self, message: str, flush: bool = False, temp_flush: bool = False, temp: float = 0.33, top_p: float = 0.95, top_k: int = 42, stop: Union[list,None] = None, max_tokens: int = 1536):
        if flush:
            self.clear()
        self.message(message)
        prompt = self.fmt.prompt(
            self.messages,
            stop_token=stop[0] or "",
        )
        try:
            return self.generate(prompt,
                temp=temp,
                top_p=top_p,
                top_k=top_k,
                stop=stop,
                max_tokens=max_tokens
            )
        except Exception as e:
            print(e)
            return None
    