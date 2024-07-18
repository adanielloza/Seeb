
// src/controllers/TaskController.ts
import axios from 'axios';
import { Task } from '../models/Task';

const API_URL = 'https://seeb-5.onrender.com/api/tasks';

export const getTasks = async () => {
    const response = await axios.get(API_URL);
    return response.data;
};
