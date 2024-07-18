// src/components/tasksComponents.jsx
import React from 'react';

/**
 * @typedef {Object} Task
 * @property {number} id
 * @property {number} job_id
 * @property {number} user_id
 * @property {string} description
 * @property {string} difficulty
 * @property {number} estimatetime
 * @property {number} status_id
 * @property {string|null} donetime
 */

/**
 * @param {{ tasks: Task[] }} props
 */
const TasksTable = ({ tasks }) => {
    return (
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Job ID</th>
                    <th>User ID</th>
                    <th>Description</th>
                    <th>Difficulty</th>
                    <th>Estimated Time</th>
                    <th>Status ID</th>
                    <th>Done Time</th>
                </tr>
            </thead>
            <tbody>
                {tasks.map(task => (
                    <tr key={task.id}>
                        <td>{task.id}</td>
                        <td>{task.job_id}</td>
                        <td>{task.user_id}</td>
                        <td>{task.description}</td>
                        <td>{task.difficulty}</td>
                        <td>{task.estimatetime}</td>
                        <td>{task.status_id}</td>
                        <td>{task.donetime ? task.donetime : 'N/A'}</td>
                    </tr>
                ))}
            </tbody>
        </table>
    );
}

export default TasksTable;
