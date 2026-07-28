import api from "./client";

export const getCourseArtifacts = (courseId) =>
    api.get(`/artifacts/course/${courseId}`);

export const deleteArtifact = (artifactId) =>
    api.delete(`/artifacts/${artifactId}`);

export const generateCourseArtifact = (courseId, type) =>
    api.post(`/artifacts/gen/course/${courseId}/${type}`);

export const generateDocumentArtifact = (documentId, type) =>
    api.post(`/artifacts/gen/document/${documentId}/${type}`);