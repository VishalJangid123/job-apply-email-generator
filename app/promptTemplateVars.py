combined_prompt_tpl = """
From the Resume text for a job aspirant below, extract the following entities strictly as instructed:

 ### Person Entity Extraction
   - Look for **Person** entities and generate the information strictly as described:
     - Entity Definition: `label:'Person',id:string,role:string,description:string //Person Node`
     - `id` must be unique and alphanumeric.
     - `description` must be a crisp, short summary (not exceeding 100 characters).
     - Do not impute missing values or create fictitious data.
     - Do not focus on position, company, education, or skill-related information for this entity.
    

### Education Entity Extraction
   - Look for **Education** entities and generate the information strictly as described:
     - Entity Definition: `label:'Education',id:string,degree:string,university:string,graduationDate:string,score:string,url:string //Education Node`
     - `id` must be unique and alphanumeric.
     - Do not impute missing values or create fictitious data.

## Skill Entity Extraction
   - Look for **Skill** entities and generate the information strictly as described:
     - Entity Definition: `label:'Skill',id:string,name:string,level:string //Skill Node`
     - `id` must be unique and alphanumeric.
     - For the level of each skill, assign `expert` if experience is >5 years, `intermediate` if experience is between 2-5 years, and `beginner` if experience is less than 2 years.
     - Do not impute missing values or create fictitious data.

## Work Experience Entity Extraction
   - Look for **Work Experience** entities and generate the information strictly as described:
     - Entity Definition: `label:'WorkExperience',id:string,job_title:string,company:string,duration:string,responsibilities:string //WorkExperience Node`
     - `id` must be unique and alphanumeric.
     - For each role, return job title, company name, duration, and key responsibilities.
     - Do not impute missing values or create fictitious data.

## Certificate Entity Extraction
   - Look for **Certificate** entities and generate the information strictly as described:
     - Entity Definition: `label:'Certificate',id:string,certificate_name:string,issuing_organization:string,issue_date:string,url:string //Certificate Node`
     - `id` must be unique and alphanumeric.
     - Do not impute missing values or create fictitious data.

## Interpersonal Skills Entity Extraction
   - Look for **Interpersonal Skills** entities and generate the information strictly as described:
     - Entity Definition: `label:'InterpersonalSkill',id:string,name:string,level:string //InterpersonalSkill Node`
     - `id` must be unique and alphanumeric.
     - For interpersonal skills, assume `level` as `expert`, `intermediate`, or `beginner` based on the description.
     - Do not impute missing values or create fictitious data.

## Personal Projects Entity Extraction
   - Look for **Personal Projects** entities and generate the information strictly as described:
     - Entity Definition: `label:'PersonalProject',id:string,project_name:string,technologies:string,description:string,link:string //PersonalProject Node`
     - `id` must be unique and alphanumeric.
     - Do not impute missing values or create fictitious data.

### Resume Text:
{text}


"""