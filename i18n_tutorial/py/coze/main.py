import os,sys, re, json
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

def translateMdFile(md_open, md_save, lang_ext):
  print('processing file:' + md_open)
  try:
    source_md = ''
    with open(md_open, "r", encoding="utf-8") as f:
      with open(md_save+'.'+lang_ext, "a+", encoding="utf-8") as target_file:
        target_file.truncate(0)

        source_md = f.read()

        response = chat([ HumanMessage(content="""
        # Instruction
        - translate the below MARKDOWN content into traditional chinese
        - skip the translation of the frontmatter
        """.strip()),
          HumanMessage(content="MARKDOWN=```" + source_md + "```")
          ])

        translated_md = response.content
        translated_md = re.sub(r'^MARKDOWN=```', '', translated_md)
        translated_md = re.sub(r'```$', '', translated_md)

        print(translated_md)
        target_file.write(translated_md)

  except Exception as E:
    print(E)

for root, dirs, files in os.walk("D:\\_workspace\\docusaurus-playlist\\i18n_tutorial\\docs"):
    for file in files:
        if file.endswith(".md"):
            print("md file found", os.path.join(root, file))
            md_open = os.path.join(root, file)
            translateMdFile(
                md_open, 
                md_open.replace('i18n_tutorial\\docs','i18n_tutorial\\i18n\\zh-Hans\\docusaurus-plugin-content-docs\\current'),
                "zh-Hans"  # append ext to file translated
            )
            # with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                # print(f.read())
