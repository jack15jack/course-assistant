def build_formula_prompt(context):

    return f"""
Generate a formula sheet.

For every formula include:

• Formula name
• Equation
• Variable definitions
• Units (if applicable)
• When to use the formula
• Assumptions
• Common mistakes

If a derivation is short and useful, include it.

Group related formulas together.

Do not include long explanations.

Return Markdown only.

Course Material:

{context}
"""