from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI

from ai_template_style_transfer import jira, prompt_templates
from ai_template_style_transfer.openai import Models

required_input_variables = ["description", "template"]

max_retries = 100


def generic(
    description: str,
    template: jira.Template,
    transfer_prompt: PromptTemplate,
    model_name: Models = Models.GPT4,
    temperature=0,
) -> str:
    assert all(
        variable in transfer_prompt.input_variables
        for variable in required_input_variables
    ), f"transfer prompt requires {required_input_variables}"

    prompt = transfer_prompt.format(
        description=description, template=template.content
    )
    llm = ChatOpenAI(model_name=model_name, temperature=temperature)

    prediction = llm.predict(prompt)

    retry = 0

    while True:
        retry += 1
        if retry > max_retries:
            raise "max retries exceeded"
        validation = template.validate(prediction)
        if validation == "passed":
            return prediction
        else:
            prediction = llm.predict(f"{validation}\n\nretry\n\n{prompt}")


def jira_issue(
    description: str, model_name: Models = Models.GPT4, temperature=0
) -> str:
    return generic(
        description,
        jira.issue_template,
        prompt_templates.style_transfer_issue,
        model_name=model_name,
        temperature=temperature,
    )
