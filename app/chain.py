import os
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
import promptTemplateVars
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq( temperature = 0, groq_api_key = os.getenv("GROQ_API_KEY"), model_name = 'llama-3.1-70b-versatile')

    def scrape_from_web(self, link):
        loader = WebBaseLoader(link)
        page_data = loader.load().pop().page_content
        return page_data
    
    def extract_resume(self, resume_text):
        person_prompt_tpl= PromptTemplate.from_template(promptTemplateVars.combined_prompt_tpl)
        person = person_prompt_tpl | self.llm
        person_extract = person.invoke({'text': resume_text})
        return person_extract.content
        # json_parser = JsonOutputParser()
        # res = json_parser.parse(person_extract.content)
        # return res

    def extract_job_desc(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]
        


    def write_email(self, job_description, resume):
        prompt_email = PromptTemplate.from_template(
            """
            ### RESUME
            {resume}
            
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            Your job is to write a cold email to the company regarding the job mentioned above describing the capability of candiate resume in fulfilling their needs.
            Do not add any fictious data only relevent the resume mentioned above 
            Do not provide a preamble.
            ### EMAIL (NO PREAMBLE):

            """
        )
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job_description), 'resume': resume})
        return res.content
    

if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))