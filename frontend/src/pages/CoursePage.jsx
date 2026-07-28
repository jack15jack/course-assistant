import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

import { getCourse } from "../api/courses";
import { deleteArtifact, getCourseArtifacts } from "../api/artifacts";
import { uploadDocument, processDocument, deleteDocument } from "../api/documents";

import api from "../api/client";
import Card from "../components/Card";
import Section from "../components/Section";

function CoursePage() {

    const { id } = useParams();

    const [course, setCourse] = useState(null);
    const [artifacts, setArtifacts] = useState([]);
    const [selectedFile, setSelectedFile] = useState(null);
    const [fileInputKey, setFileInputKey] = useState(0);
    const [uploading, setUploading] = useState(false);
    

    useEffect(() => {
        loadCourse();
        loadArtifacts();
    }, []);

    async function loadCourse() {
        const res = await getCourse(id);
        setCourse(res.data);
    }

    async function loadArtifacts() {
        const res = await getCourseArtifacts(id);
        setArtifacts(res.data);
    }

    async function handleUpload() {
        if (!selectedFile) return;

        setUploading(true);

        try {
            await uploadDocument(id, selectedFile);
            loadCourse();
        } finally {
            setUploading(false);
            setSelectedFile(null);
        }
    }

    async function handleProcess(documentId) {
        await processDocument(documentId);
        setTimeout(loadCourse, 1500);
    }

    async function generateCourseArtifact(id, type) {
        await generateCourseArtifact(id, type);
        setTimeout(loadArtifacts, 1500);
    }

    async function generateDocumentArtifact(id, type) {
        await generateDocumentArtifact(id, type);
        setTimeout(loadArtifacts, 1500);
    }

    async function handleDeleteDocument(documentId) {
        await deleteDocument(documentId);
        setTimeout(loadCourse, 1500);
    }

    async function handleDeleteArtifact(artifactId) {
        await deleteArtifact(artifactId);
        setTimeout(loadArtifacts, 1500);
    }

    if (!course) {
        return <div>Loading...</div>;
    }

    return (
        <div
        style={{
            minHeight:"100vh",
            background:"#f5f7fb",
            padding:"40px"
        }}
        >

            <h1>{course.name}</h1>

            <hr />

            <h2>Upload Document</h2>

            <input
                key={fileInputKey}
                type="file"
                onChange={(e) => setSelectedFile(e.target.files[0])}
            />

            <button
                disabled={uploading || !selectedFile}
                onClick={handleUpload}
            >
                {uploading ? "Uploading..." : "Upload"}
            </button>

            <hr />

            <Section title="Documents">
            {
            course.documents?.map(document => (

            <Card key={document.id}>

            <h3>
                {document.filename}
            </h3>

            <p>
                Status: {document.status}
            </p>

            <button onClick={() => handleProcess(document.id)}>
                Process
            </button>

            <button onClick={() => handleDeleteDocument(document.id)}>
                Delete
            </button>

            </Card>
            ))
            }
            </Section>

            <hr />

            <Section title="Generated Materials">

            <button onClick={() => generateCourseArtifact(course.id, "notes")}>
                Notes
            </button>

            <button onClick={() => generateCourseArtifact(course.id, "studyguide")}>
                Study Guide
            </button>

            <button onClick={() => generateCourseArtifact(course.id, "formula")}>
                Formula Sheet
            </button>

            <button onClick={() => generateCourseArtifact(course.id, "exam")}>
                Practice Exam
            </button>

            {
            artifacts.map(artifact => (

            <Card key={artifact.id}>

            <h3>
            {artifact.title}
            </h3>

            <p>
            {artifact.scope} • {artifact.artifact_type}
            </p>

            <button 
            href={`http://localhost:8000/artifacts/${artifact.id}/download`}
            target="_blank"
            rel="noreferrer"
            >
                Download
            </button>

            <button onClick={() => handleDeleteArtifact(artifact.id)}>
                Delete
            </button>

            </Card>
            ))
            }
            </Section>

        </div>
    );
}

export default CoursePage;