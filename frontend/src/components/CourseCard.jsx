import {Link} from "react-router-dom";

function CourseCard({course, onDelete}){

    return (
        <div className="card">
            <h2>
            {course.name}
            </h2>

            <p>
            {course.semester}
            </p>

            <Link to={`/courses/${course.id}`}>
            Open Course
            </Link>

            <button onClick={()=>onDelete(course.id)}>
                Delete
            </button>
        </div>
        )
    }

export default CourseCard;