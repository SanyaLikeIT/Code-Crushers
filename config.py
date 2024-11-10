# config.py
from langchain.prompts import PromptTemplate
from langchain.llms import YandexGPT
from vectorstor import vectorsto

folder_path = '/Users/egornava/Desktop/work/coding/Hacks/LibrarySearcher2/Media_Digital'
vectorstore = vectorsto(folder_path)

llm = YandexGPT(
    iam_token="t1.9euelZqZnMmKj8uWj4zKi4zKjsbGi-3rnpWazZmMls6TmpWJk5eJlpDHi83l8_dfCkBG-e82XBhn_t3z9x85PUb57zZcGGf-zef1656Vmo-Ryp2Yzo-Plo7Nx8eSx8-R7_zF656Vmo-Ryp2Yzo-Plo7Nx8eSx8-R.39hKJU0oG-Lp0A5vIh4iQJyBqWEDQ4C56bFOvHwdYmNZXtIixB_JY96JCtvL4kZjUyVQAVlwRcaCdf8O6n-wDQ",
    folder_id="b1gjkg16e0o1ar19chvd"
)
# config.py
custom_system_prompt = """
Вы — помощник, который отвечает на вопросы на основе контекста. Пожалуйста, отвечайте строго в соответствии с предоставленным контекстом!
Если в контексте не упоминается концепт, не добавляйте общих знаний о нём! Не ссылайся на информацию из интернета! При ответе давай как можно больше статистики из данных файлов!
всегда ссылайся на реальные цисла! максимальная длина 3 предложения 

Question: {question}
Context: {context}
Answer:
"""

custom_prompt = PromptTemplate(
    input_variables=["context", "question"],
    template=custom_system_prompt
)
