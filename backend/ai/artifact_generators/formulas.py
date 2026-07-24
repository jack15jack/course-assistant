from ai.artifact_generators.base import BaseGenerator

from ai.prompts.formulas import build_formula_prompt


class NotesGenerator(BaseGenerator):

    def generate(self, document_id):

        context = self.context_builder.build_formula_context(document_id)

        prompt = build_formula_prompt(context)

        return self.llm.generate(prompt)