// src/components/Tasks.js
import React, { useState, useEffect } from 'react';
import { getTasks } from '../controllers/TaskController';
import TasksTable from '../components/tasksComponents';
import SearchBar from '../components/SearchBar';
import SubmitButton from '../components/SubmitButton';

const Tasks = () => {
    const [tasks, setTasks] = useState([]);
    const [searchTerm, setSearchTerm] = useState('');

    useEffect(() => {
        const fetchTasks = async () => { 
            try {
                const tasksData = await getTasks();
                setTasks(tasksData);
            } catch (error) {
                console.error(error);
            }
        };

        fetchTasks();
    }, []);

    const filteredTasks = tasks.filter(task =>
        task.difficulty.toLowerCase().includes(searchTerm.toLowerCase())
    );

    const handleSubmit = () => {
        alert('Submit button clicked!');
    };

    return (
        <div>
            <h1>Task List</h1>
            <SearchBar searchTerm={searchTerm} setSearchTerm={setSearchTerm} />
            <SubmitButton onClick={handleSubmit} label="Submit" />
            <TasksTable tasks={filteredTasks} />
        </div>
    );
}

export default Tasks;
