function Section({title, children}) {

    return (
        <section style={{
            marginTop:"20px"
        }}>

            <h2>{title}</h2>

            {children}

        </section>
    );
}

export default Section;