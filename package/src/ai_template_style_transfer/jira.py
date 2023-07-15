from dataclasses import dataclass
import re
from typing import List
from triple_quote_clean import TripleQuoteCleaner


tqc = TripleQuoteCleaner()


@dataclass
class Template:
    content: str
    checks: List[str]

    def validate(self, results: str):
        for check in self.checks:
            if len(re.findall(check, results)) == 0:
                return f"{check} not in {results}"
        return "passed"


issue_template = Template(
    checks=[
        "Narrative",
        "As a",
        "I want",
        "Acceptance Criteria",
        "Given",
        "When",
        "Then",
    ],
    content=(
        tqc
        << """
        *Narrative*

        As a ...

        I want ...

        *Acceptance Criteria*

        Given ...

        When ...

        Then ...
        """
    ),
)
