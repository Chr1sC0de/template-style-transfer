import re

from triple_quote_clean import TripleQuoteCleaner

from ai_template_style_transfer import transfer

tqc = TripleQuoteCleaner()

description = (
    tqc
    << """
    *Background*

    Solution files uploaded into AWS will be loaded into Databricks tables. We
    will assume that the ground truth for the data loaded into Databricks will
    match the output from a set of local extraction samples. (i.e. the
    extraction end to end on a local device. Note I am assuming that the local
    extraction has already been sufficiently tested). For each loaded table, for
    each row, metadata columns will be added showing the file source and
    ingestion time.

    *Method*

    using the added meta-data columns,

    - we will confirm that all source files are ingested into Databricks
    - ensure that when compared to a local extraction.
        - row counts match.
        - all data matches.
        - no duplicates are found.

    *Narrative*

    As a Validator, I want to ensure the data is accurate and consistent with
    the ground truth from local extraction samples.

    *Acceptance Criteria*

    Given solution files are uploaded into AWS and loaded into Databricks
    tables, When comparing the data in Databricks with local extraction samples,
    Then the following conditions should be

    met:

    - All source files are ingested into Databricks using the added metadata
      columns
    - Row counts match between Databricks tables and local extraction samples *
      All data matches between Databricks tables and local extraction samples
    - No duplicate records are found in Databricks tables*
    """
)

assertion_failed_message = "template conditions not met"


def test_transfer__jira_issue():
    style_transferred = transfer.jira_issue(description).lower()

    print(style_transferred)

    assert (
        len(re.findall("as a", style_transferred)) > 0
    ), assertion_failed_message

    assert (
        len(re.findall(r"\\*narrative\\*", style_transferred)) > 0
    ), assertion_failed_message

    assert (
        len(re.findall("i want", style_transferred)) > 0
    ), assertion_failed_message

    assert (
        len(re.findall(r"\\*acceptance criteria\\*", style_transferred)) > 0
    ), assertion_failed_message

    assert (
        len(re.findall("given that", style_transferred)) > 0
    ), assertion_failed_message

    assert (
        len(re.findall("when the", style_transferred)) > 0
    ), assertion_failed_message

    assert (
        len(re.findall("then the", style_transferred)) > 0
    ), assertion_failed_message


if __name__ == "__main__":
    test_transfer__jira_issue()
