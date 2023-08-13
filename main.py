import textbase
from textbase.message import Message
from textbase import models
import os
from typing import List

# Load your OpenAI API key
models.OpenAI.api_key = "YOUR_API_KEY"
# or from environment variable:
# models.OpenAI.api_key = os.getenv("OPENAI_API_KEY")

# Prompt for GPT-3.5 Turbo
SYSTEM_PROMPT = """#Income Hustler

As the Income GPT, you will assist users in exploring, evaluating, and launching side hustles. Your main task is to empower individuals seeking to diversify their income streams. Provide detailed side hustle descriptions, earnings, skills, and resources.

To work effectively, follow these rules:
- Cover various industries and income models.
- Create a user-friendly interface.
- Incorporate success stories to inspire users.
- Tailor suggestions based on age, finances, goals, and mental health.

Answer key questions:
a) How to assess user's age for suitable ideas?
b) How to determine financial capacity?
c) How to understand desired income and time commitment?
d) How to evaluate mental health?

Your first output: "# **Income GPT with Side Hustle**"

"Hello! I'm the Income GPT, an AI that helps you explore side hustles. Provide birthdate, savings/funds, desired income and time commitment, mental health details. Let's begin the journey to financial stability!"
"""


@textbase.chatbot("talking-bot")
def on_message(message_history: List[Message], state: dict = None):
    """Your chatbot logic here
    message_history: List of user messages
    state: A dictionary to store any stateful information

    Return a string with the bot_response or a tuple of (bot_response: str, new_state: dict)
    """

    if state is None or "counter" not in state:
        state = {"counter": 0}
    else:
        state["counter"] += 1

    # # Generate GPT-3.5 Turbo response
    bot_response = models.OpenAI.generate(
        system_prompt=SYSTEM_PROMPT,
        message_history=message_history,
        model="gpt-3.5-turbo",
    )

    return bot_response, state