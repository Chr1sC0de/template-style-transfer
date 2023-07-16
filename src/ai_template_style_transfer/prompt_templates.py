from langchain import PromptTemplate
from triple_quote_clean import TripleQuoteCleaner

tqc = TripleQuoteCleaner()

style_transfer_issue = PromptTemplate(
    input_variables=["description", "template"],
    template=tqc
    << """
    You are a helpful ai assistant. The software engineering team requires well
    formatted and templated jira tickets to ensure

        - Efficiency
        - Clarity and comprehensibility
        - Improved searchability
        - Reduced training time
        - Easier prioritization
        - Reporting and analytics
        - Predictability
        - Better audit trails
        - Quality control
        - Enhanced collaboration
        - Workflow automation

    The following is a description for an `issue` jira ticket:


    {description}


    please convert the description to the following template


    {template}


    templated description:
    """,
)
