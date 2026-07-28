import ArtifactCard from "./ArtifactCard";


function ArtifactList({
    onDelete,
    artifacts
}) {

    return (
        <section>

            <h2>
                Generated Artifacts
            </h2>

            {artifacts.length === 0 && (
                <p>
                    No artifacts generated.
                </p>
            )}

            {artifacts.map(artifact => (
                <ArtifactCard
                    key={artifact.id}
                    artifact={artifact}
                    onDelete={onDelete}
                />
            ))}

        </section>
    );
}

export default ArtifactList;