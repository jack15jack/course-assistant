import api from "./client";

export const uploadDocument = (courseId, file) => {
    const formData = new FormData();
    formData.append("file", file);

    return api.post(`/documents/${courseId}`, formData, {
        headers: {
            "Content-Type": "multipart/form-data",
        },
    });
};

export const deleteDocument = (documentId) =>
    api.delete(`/document/${documentId}`);

export const processDocument = (documentId) =>
    api.post(`/jobs/documents/${documentId}`);