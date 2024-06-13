#!/usr/bin/env python

"""
This script initializes a chatbot, logs in, creates a new conversation,
sets a system prompt and asks a question to the chatbot.
"""

import os, sys, re
from pprint import pprint

from hugchat import hugchat
from hugchat.login import Login


# Import the necessary modules and classes

# Email and password of the user
email = "testhelloworld04@gmail.com"
password = "TgUGLRcL1qCMbmP"

# Directory to store the cookies
cookie_path_dir = "./cookies"

def initialize_chatbot(email, password, cookie_path_dir):
    """
    Initialize the chatbot.

    Args:
        email (str): Email of the user.
        password (str): Password of the user.
        cookie_path_dir (str): Directory to store the cookies.

    Returns:
        obj: ChatBot object.
    """

    sign = Login(email, password)
    cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)
    chatbot = hugchat.ChatBot(cookies=cookies, default_llm=2)
    models = chatbot.get_available_llm_models()
    print(models[5])
    # print(chatbot.get_active_llm_index())
    chatbot.new_conversation(switch_to = True)

    return chatbot


def create_new_conversation_and_set_system_prompt(chatbot):
    """
    Create a new conversation and set a system prompt.

    Args:
        chatbot (obj): ChatBot object.
    """

    chatbot.new_conversation(switch_to=True, system_prompt="reply \"Peter\" when user asks \"what is your name ?\"")
    chatbot.share_conversation()

def ask_question_to_chatbot(chatbot, question):
    """
    Ask a question to the chatbot.

    Args:
        chatbot (obj): ChatBot object.

    Returns:
        tuple: reply and sharelink.
    """

    reply = chatbot.chat(question )

    # Non stream
    reply.wait_until_done()

    sharelink = chatbot.share_conversation()
    return reply, sharelink


def save_cookies_and_print_results(chatbot, reply, sharelink):
    """
    Save the cookies and print the results.

    Args:
        chatbot (obj): ChatBot object.
        reply (str): Reply from the chatbot.
        sharelink (str): Sharelink of the conversation.
    """

    sign = Login(email, password)
    sign.save_cookies(cookie_path_dir)
    print(reply)
    print(sharelink)
    pprint(chatbot.get_conversation_info().history)


def translateMdFile(md_open, md_save, lang_ext):
  try:
    source_md = ''
    with open(md_open, "r", encoding="utf-8") as f:
      with open(md_save+'.'+lang_ext, "a+", encoding="utf-8") as target_file:
        source_md = f.read()

        # Initialize the chatbot
        chatbot = initialize_chatbot(email, password, cookie_path_dir)

        # Create a new conversation and set a system prompt
        create_new_conversation_and_set_system_prompt(chatbot)

        # Ask a question to the chatbot
        question = """
        # Instruction
        - translate the below MARKDOWN content into traditional chinese
        - skip the translation of the frontmatter, leave it as it is
        - skip the translation of the code blocks, leave it as it is

        MARKDOWN=```
        {source_md}
        ```
        """.strip().replace("{source_md}", source_md)
        reply, sharelink = ask_question_to_chatbot(chatbot, question)

        translated_md = reply
        translated_md = re.sub(r'^MARKDOWN=```', '', str(translated_md))
        translated_md = re.sub(r'```$', '', str(translated_md))

        print(translated_md)
        target_file.truncate(0)
        target_file.write(translated_md)

  except Exception as e:
    print(e)
    pass


for root, dirs, files in os.walk("D:\\_workspace\\docusaurus-playlist\\i18n_tutorial\\docs"):
    continue
    for file in files:
        if file.endswith(".m1d"):
            print("md file found", os.path.join(root, file))
            md_open = os.path.join(root, file)
            translateMdFile(
                md_open,
                md_open.replace('i18n_tutorial\\docs','i18n_tutorial\\i18n\\zh-Hans\\docusaurus-plugin-content-docs\\current'),
                "zh-Hans"  # append ext to file translated
            )

        if file.endswith(".md1x"):
            print("md file found", os.path.join(root, file))
            md_open = os.path.join(root, file)
            translateMdFile(
                md_open,
                md_open.replace('i18n_tutorial\\docs','i18n_tutorial\\i18n\\zh-Hans\\docusaurus-plugin-content-docs\\current'),
                "zh-Hans"  # append ext to file translated
            )

        if file.endswith(".json"):
            print("md file found", os.path.join(root, file))
            md_open = os.path.join(root, file)
            translateMdFile(
                md_open,
                md_open.replace('i18n_tutorial\\docs','i18n_tutorial\\i18n\\zh-Hans\\docusaurus-plugin-content-docs\\current'),
                "zh-Hans"  # append ext to file translated
            )

            # with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                # print(f.read())

translateMdFile(
    "D:\\_workspace\\docusaurus-playlist\\i18n_tutorial\\i18n\\zh-Hans\\docusaurus-plugin-content-docs\\current.json",
    "D:\\_workspace\\docusaurus-playlist\\i18n_tutorial\\i18n\\zh-Hans\\docusaurus-plugin-content-docs\\current.json.zh-Hans",
    "zh-Hans"  # append ext to file translated
)
