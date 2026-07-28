function DocumentCard({
    document,
    onProcess,
    onDelete,
    refresh
}){
    return (
        <div className="card">

            <h3>
            {document.filename}
            </h3>

            <p>
            Status:
            {document.status}
            </p>

            <button onClick={() => onProcess(document.id)}>
            Process
            </button>

            <button onClick={() => onDelete(document.id)}>
            Delete
            </button>
        </div>
    )
}

export default DocumentCard;