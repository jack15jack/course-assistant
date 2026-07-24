def build_studyguide_prompt(context):

    return f"""
You are creating a study guide for a university student preparing for an exam.

Produce a concise but comprehensive study guide.

Requirements:

Organize by topic.

For each topic include:

• Key concepts
• Important definitions
• Important formulas
• Common mistakes
• Relationships to other topics
• Things students commonly forget

Emphasize material likely to appear on an exam.

If procedures exist, convert them into step-by-step lists.

Keep explanations concise.

Return Markdown only.

Course Material:

{context}
"""