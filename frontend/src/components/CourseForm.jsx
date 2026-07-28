import {useState} from "react";

function CourseForm({
    onSubmit,
    onCancel
}){

    const [name, setName] = useState("");
    const [semester, setSemester] = useState("");
    const [description, setDescription] = useState("");

    async function handleSubmit(e){
        e.preventDefault();

        await onSubmit({
            name,
            semester,
            description
        });
    }

    return (
        <form onSubmit={handleSubmit}>

            <input
                placeholder="Course Name"
                value={name}
                onChange={e=>setName(e.target.value)}
            />

            <input
                placeholder="Semester"
                value={semester}
                onChange={e=>setSemester(e.target.value)}
            />

            <textarea
                placeholder="Description"
                value={description}
                onChange={e=>setDescription(e.target.value)}
            />

            <button type="submit">
                Create Course
            </button>

        </form>
    )
}

export default CourseForm;