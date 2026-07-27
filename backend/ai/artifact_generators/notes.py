from ai.artifact_generators.base import ArtifactGenerator

from ai.prompts.notes import build_notes_prompt


class NotesGenerator(ArtifactGenerator):

    def generate(self, scope: str, scope_id: int)-> str:

        context = self.context_builder.build_full_context(scope, scope_id)

        prompt = build_notes_prompt(context)

        return self.llm.generate(prompt)