import os
import streamlit as st
import openai
import ai_template_style_transfer


def main():
    st.set_page_config(layout="wide")

    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        os.environ['OPENAI_API_KEY'] = st.text_input(
            label="OpenAI API key",
            type="password",
        )

        model = st.selectbox(
            "model", list(ai_template_style_transfer.openai.Models)
        )

        temperature = st.slider(
            label="Temperature",
            value=0.0,
            min_value=0.0,
            max_value=1.0,
            step=0.01,
        )

        ticket_description = st.text_area(
            label="Ticket Description", height=300, value=""
        )

    with col2:
        issue_template = ai_template_style_transfer.jira.issue_template
        template_content = st.text_area(
            value=issue_template.content, label="Template", height=500
        )
        issue_template.content = template_content

    with col3:
        ran = st.button(
            label="Style Transfer", use_container_width=True, type="primary"
        )
        if ran and len(ticket_description) > 0:
            try:
                with st.spinner("in progress"):
                    style_transferred = (
                        ai_template_style_transfer.transfer.jira_issue(
                            ticket_description,
                            model_name=model,
                            temperature=temperature,
                        )
                    )
            except Exception as e:
                style_transferred = e
            if isinstance(style_transferred, Exception):
                st.exception(style_transferred)
            elif isinstance(style_transferred, str):
                st.text_area(
                    label="Style Transferred",
                    value=style_transferred,
                    height=500,
                )
        elif len(ticket_description) == 0:
            st.info("No description provided")

        ran = False


if __name__ == "__main__":
    main()
