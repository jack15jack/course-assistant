import api from "./client";

export const getCourseArtifacts = (courseId) =>
    api.get(`/artifacts/course/${courseId}`);

export const deleteArtifact = (artifactId) =>
    api.delete(`/artifacts/${artifactId}`);

export const generateArtifact = (scope, scopeId, type) =>
    api.post(`/artifacts/gen/${scope}/${scopeId}/${type}`);

export default api;
