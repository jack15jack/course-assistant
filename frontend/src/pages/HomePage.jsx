import { useEffect, useState } from "react";
import { getCourses } from "../api/courses";
import { Link } from "react-router-dom";

function HomePage() {

    const [courses, setCourses] = useState([]);

    useEffect(() => {
        loadCourses();
    }, []);

    async function loadCourses() {
        const res = await getCourses();
        setCourses(res.data);
    }

    return (
        <div>
            <h1>Courses</h1>
            {courses.map(course => (
                <div key={course.id}>
                    <Link to={`/course/${course.id}`}>
                        {course.name}
                    </Link>
                </div>
            ))}
        </div>
    );
}

export default HomePage;