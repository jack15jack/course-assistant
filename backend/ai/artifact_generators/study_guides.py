from ai.artifact_generators.base import BaseGenerator

from ai.prompts.study_guides import build_studyguide_prompt

class NotesGenerator(BaseGenerator):

    def generate(self, document_id):

        context = self.context_builder.build_concise_context(document_id)

        prompt = build_studyguide_prompt(context)

        return self.llm.generate(prompt)