function LoadingSpinner() {
    return (
        <div style={styles.container}>
            <div style={styles.spinner}></div>
            <p>Loading...</p>
        </div>
    );
}

const styles = {
    container: {
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        padding: "2rem"
    },

    spinner: {
        width: "40px",
        height: "40px",
        border: "5px solid #ddd",
        borderTop: "5px solid #2563eb",
        borderRadius: "50%",
        animation: "spin 1s linear infinite"
    }
};

export default LoadingSpinner;