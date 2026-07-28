function CourseHeader({ course }) {

    return (
        <section className="course-header">

            <h1>
                {course.name}
            </h1>

            <p>
                {course.description}
            </p>

            <span>
                {course.semester}
            </span>

        </section>
    );
}

const styles={
    header:{
        background:"#2563eb",
        color:"white",
        padding:"2rem",
        borderRadius:"16px",
        marginBottom:"2rem"
    }
};

export default CourseHeader;