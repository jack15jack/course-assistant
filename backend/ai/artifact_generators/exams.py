from ai.artifact_generators.base import ArtifactGenerator

from ai.prompts.exams import build_exam_prompt


class ExamGenerator(ArtifactGenerator):

    def generate(self, scope: str, scope_id: int)-> str:

        context = self.context_builder.build_exam_context(scope, scope_id)

        prompt = build_exam_prompt(context)

        return self.llm.generate(prompt)