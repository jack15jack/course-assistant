from ai.artifact_generators.base import ArtifactGenerator

from ai.prompts.exams import build_exam_prompt


class ExamGenerator(ArtifactGenerator):

    def generate(self, document_id)-> str:

        context = self.context_builder.build_exam_context(document_id)

        prompt = build_exam_prompt(context)

        return self.llm.generate(prompt)