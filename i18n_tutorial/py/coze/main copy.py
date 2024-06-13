import os,sys
from pprint import pprint

from langchain_core.messages import AIMessage, HumanMessage
from langchain_community.chat_models.coze import ChatCoze

COZE_API_KEY = os.getenv("COZE_API_KEY", "")
BOT_ID = os.getenv("BOT_ID", "")

chat = ChatCoze(
    coze_api_base="https://api.coze.com",
    coze_api_key=COZE_API_KEY,
    bot_id=BOT_ID,
    user="123",
    conversation_id="",
    streaming=False
)

response = chat([
  HumanMessage(content="""
# Instruction

Please take care the below information :

**Background Information**

Louis is a boy live in Hong Kong
""".strip()),
  HumanMessage(content="[YES:NO] Is Louis live in Hong Kong ?")
  ])

pprint(response.content)
