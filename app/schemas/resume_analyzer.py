from langchain_openai import ChatOpenAI
from app.agents.resume_parser import resume_parser
from app.prompts.resume_prompt import prompt


llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

resume_chain = prompt | llm | resume_parser