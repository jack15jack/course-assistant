from ai.artifact_generators.base import ArtifactGenerator

from ai.prompts.formulas import build_formula_prompt


class FormulaGenerator(ArtifactGenerator):

    def generate(self, scope: str, scope_id: int)-> str:

        context = self.context_builder.build_formula_context(scope, scope_id)

        prompt = build_formula_prompt(context)

        return self.llm.generate(prompt)