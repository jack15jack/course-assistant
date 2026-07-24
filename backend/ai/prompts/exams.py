def build_exam_prompt(context):

    return f"""
You are writing a university-level practice exam.

Create a realistic exam covering all major topics.

Requirements:

Include a balanced mix of:

• Multiple choice
• Short answer
• Problem solving
• Conceptual questions
• True/False (sparingly)

Include:

• Difficulty ranging from easy to challenging.
• Coverage of every major topic.
• Questions requiring application rather than memorization whenever possible.
• Numerical problems when formulas are present.

After all questions provide a complete answer key with explanations.

Do not mention that this is AI generated.

Return Markdown only.

Course Material:

{context}
"""