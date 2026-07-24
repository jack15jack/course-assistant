from ai.artifact_generators.base import ArtifactGenerator

from ai.prompts.study_guides import build_studyguide_prompt

class StudyGuideGenerator(ArtifactGenerator):

    def generate(self, document_id)-> str:

        context = self.context_builder.build_concise_context(document_id)

        prompt = build_studyguide_prompt(context)

        return self.llm.generate(prompt)