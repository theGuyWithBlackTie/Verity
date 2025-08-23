INTRODUCTORY_SUMMARY = """Human: You are an assistant tasked with generating a short, high-level **introductory summary** for a document. The summary should feel like the **opening paragraph of an article or report**, giving the reader a clear idea of what the document is about — its main topic, purpose, and general scope — without going into details. The tone should be neutral, clear, and accessible, like explaining to a new reader what this document is likely about.
The document is being processed **page by page**, and you are receiving one page of text at a time. You are also given the **name of the document** from metadata, and if available, a **previously generated summary**. The inputs are given below:

<document_metadata>
{metadata}
</document_metadata>

<current_page_content>
{page_content}
</current_page_content>

<previously_generated_summary>
{previous_summary}
</previously_generated_summary>

## Your Tasks:
1. **Update or generate** a clear and concise introductory summary for the document based on the information currently available. You may reuse or refine the previous summary if appropriate.
   
2. **Evaluate** whether the current summary is sufficient to function as a **standalone introduction** to the document. Ask yourself:
   - Does this summary clearly explain what the document is generally about?
   - Does it feel like a logical introduction one might read at the beginning of a report or article?

## Output Format:
Provide your output in JSON format as shown below:
{{
    "summary": <Your summary here>,
    "is_summary_introductory_enough": <True or False>,
    "explanation": <Why do you think summary is introductory enough?>
}}
Assistant:
"""