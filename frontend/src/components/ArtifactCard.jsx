function ArtifactCard({
    artifact,
    onDelete
}) {

    return (
        <div style={styles.card}>

            <h3>
                {artifact.title}
            </h3>

            <p>
                Type: {artifact.artifact_type}
            </p>

            <p>
                Created:
                {" "}
                {new Date(artifact.created_at).toLocaleDateString()}
            </p>

            <div style={styles.actions}>
                <button
                    href={`http://localhost:8000/artifacts/${artifact.id}/download`}
                    target="_blank"
                    rel="noreferrer"
                    style={styles.link}
                >
                    Download
                </button>

                <button
                    onClick={()=>onDelete(artifact.id)}
                    style={styles.delete}
                >
                    Delete
                </button>
            </div>
        </div>
    );
}

const styles = {
    card:{
        background:"#ffffff",
        borderRadius:"12px",
        padding:"1rem",
        boxShadow:"0 2px 8px rgba(0,0,0,.1)",
        marginBottom:"1rem"
    },
    actions:{
        display:"flex",
        gap:"10px"
    },
    link:{
        color:"#2563eb",
        textDecoration:"none"
    },
    delete:{
        background:"#dc2626",
        color:"white",
        border:"none",
        padding:"6px 12px",
        borderRadius:"6px",
        cursor:"pointer"
    }
};

export default ArtifactCard;