from ai.artifact_generators.base import BaseGenerator

from ai.prompts.exams import build_exam_prompt


class NotesGenerator(BaseGenerator):

    def generate(self, document_id):

        context = self.context_builder.build_exam_context(document_id)

        prompt = build_exam_prompt(context)

        return self.llm.generate(prompt)