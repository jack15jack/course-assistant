import api from "./client";

export const getCourses = () =>
    api.get("/courses");

export const getCourse = (id) =>
    api.get(`/courses/${id}`);

export const createCourse = (course) =>
    api.post("/courses", course);

export const updateCourse = (id, course) =>
    api.post(`/courses/${id}`, course);

export const deleteCourse = (id) =>
    api.delete(`/courses/${id}`);