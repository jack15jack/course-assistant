function Card({children}) {

    return (
        <div
            style={{
                background:"#fff",
                borderRadius:"12px",
                padding:"10px",
                marginBottom:"15px",
                boxShadow:"0 2px 8px rgba(0,0,0,.1)"
            }}
        >
            {children}
        </div>
    );
}

export default Card;