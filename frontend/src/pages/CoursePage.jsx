import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

import LoadingSpinner from "../components/LoadingSpinner";
import UploadDocument from "../components/UploadDocument";
import DocumentList from "../components/DocumentList";
import DocumentCard from "../components/DocumentCard";
import ArtifactGenerator from "../components/ArtifactGenerator";
import ArtifactList from "../components/ArtifactList"
import CourseHeader from "../components/CourseHeader"
import { getCourse } from "../api/courses";
import { deleteArtifact, getCourseArtifacts} from "../api/artifacts"
import { uploadDocument, processDocument, deleteDocument } from "../api/documents"

function CoursePage(){

    const { id } = useParams();
    const [course, setCourse] = useState(null);
    const [artifacts, setArtifacts] = useState([]);

    useEffect(()=>{
        load();
    },[]);

    async function load(){
        const courseRes = await getCourse(id);
        const artifactRes = await getCourseArtifacts(id);
        setCourse(courseRes.data);
        setArtifacts(artifactRes.data);
    }

    async function handleUpload(file) {
        await uploadDocument(id, file);
        await load();
    }

    async function handleProcess(documentId) {
        await processDocument(documentId);
        load();
    }

    async function handleDeleteDocument(documentId) {
        await deleteDocument(documentId);
        load();
    }

    async function handleDeleteArtifact(artifactId) {
        await deleteArtifact(artifactId);
        load();
    }

    if(!course)
    return <LoadingSpinner/>;

    return (

    <div className="page">

        <CourseHeader
        course={course}
        />

        <UploadDocument
        onUpload={handleUpload}
        />

        <DocumentList
        documents={course.documents}
        onProcess={handleProcess}
        onDelete={handleDeleteDocument}
        refresh={load}
        />

        <ArtifactGenerator
        courseId={course.id}
        documents={course.documents}
        refresh={load}
        />

        <ArtifactList
        artifacts={artifacts}
        onDelete={handleDeleteArtifact}
        refresh={load}
        />

    </div>
    )
}

export default CoursePage;