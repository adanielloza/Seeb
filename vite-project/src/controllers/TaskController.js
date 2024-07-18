
// src/controllers/TaskController.ts
import axios from 'axios';
import { Task } from '../models/Task';

const API_URL = 'http://127.0.0.1:5000/api/tasks';

export const getTasks = async () => {
    const response = await axios.get(API_URL);
    return response.data;
};
