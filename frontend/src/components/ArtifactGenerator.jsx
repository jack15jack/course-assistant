import { useState } from "react";
import api from "../api/client"

function ArtifactGenerator({
    courseId,
    documents,
    refresh
}) {

    const [scope,setScope] = useState("course");
    const [documentId,setDocumentId] = useState(null);
    const [type,setType] = useState("notes");


    async function generate(){
        let id = scope==="course" ? courseId : documentId;
        await api.post(`/artifacts/gen/${scope}/${id}/${type}`);
        refresh();
    }

    return (
        <div>
            <select
            value={scope}
            onChange={e=>setScope(e.target.value)}
            >
                <option value="course">
                Course
                </option>

                <option value="document">
                Document
                </option>
            </select>
           
            {
            scope==="document" &&

            <select onChange={e=>setDocumentId(e.target.value)}>
            {
                documents.map(d=>(
                <option key={d.id} value={d.id}>
                {d.filename}
                </option>
                ))
            }
            </select>
            }

            <select
            value={type}
            onChange={e=>setType(e.target.value)}
            >
                <option value="notes">
                Notes
                </option>

                <option value="studyguide">
                Study Guide
                </option>

                <option value="formula">
                Formula Sheet
                </option>

                <option value="exam">
                Exam
                </option>
            </select>

            <button onClick={generate}>
            Generate
            </button>

        </div>
    )
}

const styles={
    card:{
        padding:"1rem",
        background:"#f8fafc",
        borderRadius:"12px",
        display:"flex",
        flexDirection:"column",
        gap:"10px"
    }
};

export default ArtifactGenerator;