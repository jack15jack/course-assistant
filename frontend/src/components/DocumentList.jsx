import DocumentCard from "./DocumentCard";


function DocumentList({
    documents = [],
    onProcess,
    onDelete,
    refresh
}) {

    return (
        <section>

            <h2>
                Documents
            </h2>

            {documents.length === 0 && (
                <p>
                    No documents uploaded.
                </p>
            )}

            {documents.map(doc => (
                <DocumentCard
                    key={doc.id}
                    document={doc}
                    onProcess={onProcess}
                    onDelete={onDelete}
                    refresh={refresh}
                />
            ))}
        </section>
    );
}

export default DocumentList;