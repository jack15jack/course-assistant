import { useEffect, useState } from "react";
import { getCourses, createCourse, deleteCourse } from "../api/courses";
import { Link } from "react-router-dom";

import CourseCard from "../components/CourseCard"
import CourseForm from "../components/CourseForm"

function HomePage(){

    const [courses,setCourses] = useState([]);
    const [showForm,setShowForm] = useState(false);

    useEffect(()=>{
        loadCourses();
    },[]);

    async function loadCourses(){
        const res = await getCourses();
        setCourses(res.data);
    }

    async function handleDelete(courseId){
        await deleteCourse(courseId);
        loadCourses();
    }

    async function handleCreate(data){
        await createCourse(data);
        setShowForm(false);
        loadCourses();
    }

    return (
        <div className="page">
            <h1>
                Courses
            </h1>

            <button onClick={()=>setShowForm(true)}>
                Add Course
            </button>

            {showForm &&
                <CourseForm
                    onSubmit={handleCreate}
                />
            }

            {courses.map(course=>(
                <CourseCard
                    key={course.id}
                    course={course}
                    onDelete={handleDelete}
                    onEdit={handleEdit}
                />
            ))}
        </div>
    )
}

export default HomePage;