from ai.artifact_generators.base import BaseGenerator

from ai.prompts.notes import build_notes_prompt


class NotesGenerator(BaseGenerator):

    def generate(self, document_id):

        context = self.context_builder.build_full_context(
            document_id
        )

        prompt = build_notes_prompt(context)

        return self.llm.generate(prompt)