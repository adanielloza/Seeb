Web Engineering - User Management System
This project forms the foundational phase of system development, integrating essential functionalities that allow users to interact effectively with the platform. It supports user registration, login, and extensive user management features. Authenticated users can perform CRUD (Create, Read, Update, Delete) operations on user data, delivering a robust and efficient user management experience.

Introduction
This web application represents a comprehensive solution designed to manage and secure user data effectively. Utilizing Flask as the server framework and SQLite for database management, this project focuses on creating a secure environment where user interactions are both safe and efficient. The system employs hashed passwords and cookies to ensure that routes and user sessions are securely managed, providing a reliable and user-friendly interface for administrative tasks.

Technologies Being Used
Backend
Flask: Serves as the backbone of the web application, handling requests and responses, routing, and server-side logic.
SQLite: Used for database management, it stores and retrieves all user data as requested by the application logic, ensuring robust data handling.
Frontend
The project utilizes HTML, CSS, and JavaScript to deliver a responsive and intuitive user interface, providing users with a seamless interaction experience.

Security
Hashed Passwords: To enhance security, the application implements hashed passwords, ensuring that user credentials are stored securely in the database.
Cookies: Used for managing sessions and maintaining user state across different pages of the application.
Packages
Flask-Login: Manages user authentication, providing tools for logging in and out users from the application.
Flask-Migrate: Used for handling SQLAlchemy database migrations for Flask applications.
Flask-Bcrypt: Provides hashing utilities for Flask applications to help safely store user passwords.
MVC Architecture
The project follows the MVC (Model-View-Controller) architectural pattern, which separates the application logic into three interconnected components. This pattern helps in organizing the codebase, making it more modular and easier to maintain.

![alt text](image.png)

Model
The Model represents the data layer of the application. It defines the structure of the database and includes the logic for retrieving and storing data.

Models: User, Task, Job, Status
Database: SQLite

View
The View represents the presentation layer of the application. It is responsible for rendering the user interface and displaying the data retrieved from the model.

Templates: HTML files that render the user interface (e.g., users.html, jobs.html, tasks.html, bonificacion.html)

Controller
The Controller handles the input from the user, processes it, and returns the appropriate output. It acts as an intermediary between the Model and the View.

Controllers: user_controller.py, task_controller.py, job_controller.py, status_controller.py, bonificacion_controller.py, login_controller.py

Routes --> app.py
Routes define the URL patterns and map them to the respective controllers. They determine what code to execute when a user accesses a specific URL.


Login
This version substantially enhances the security framework of the system by integrating a sophisticated login mechanism. Instead of using JWT, this system employs hashed passwords for verifying user credentials, ensuring that stored passwords are not in plain text, thereby fortifying the security against unauthorized access.

![alt text](image-1.png)

To login:

user: admin
password: admin

Admin
Admin Dashboard
The Admin has the capability to perform CRUD operations on Users, Jobs, Tasks, and Bonifications. Each section (Users, Jobs, Tasks, Bonifications) will have its own interface for creating, reading, updating, and deleting entries.

![alt text](image-2.png)

### Frontend (Vite + React)

In this project, we have integrated a Vite + React frontend to enhance the user interface and provide a seamless interaction experience. Here is a breakdown of the components and their functionalities:

#### Controllers
**TaskController.ts**

The `TaskController.ts` file contains the logic to fetch tasks data from the backend API. Axios is used to send a GET request to the Flask server and retrieve the tasks data.

#### Components
**Tasks.js**

The `Tasks.js` component is responsible for rendering the list of tasks. It fetches the tasks data using the `getTasks` function from the `TaskController`, and then filters the tasks based on the search term. It also includes a search bar to filter tasks by their difficulty and a submit button for additional functionality.

**App.js**

The `App.js` file sets up the main application and routing. It uses React Router to define routes and render the `Tasks` component at the root path.

**SearchBar.jsx**

The `SearchBar.jsx` component provides an input field for users to search and filter tasks. It updates the `searchTerm` state based on user input, which is then used to filter the tasks displayed in the `Tasks` component.

By following these steps and utilizing these components, the project integrates a Vite + React frontend to provide a dynamic and responsive user interface.

### Why Use Vite in This Project?

Vite is a modern frontend build tool that offers significant advantages over traditional build tools like Webpack or Parcel. Here are some reasons why Vite was chosen for this project:

1. **Faster Development Builds:**
   - Vite leverages native ES modules in the browser, which means it doesn't need to bundle the entire application during development. This results in extremely fast cold starts and hot module replacement (HMR), significantly improving development speed and efficiency.

2. **Optimized Production Builds:**
   - Vite provides a highly optimized build process for production using Rollup. This ensures that the final application is as small and performant as possible, with features like tree-shaking and code-splitting out of the box.

3. **Simpler Configuration:**
   - Vite comes with sensible defaults and a simplified configuration system. It supports various frameworks (like React, Vue, and Svelte) and can be extended with plugins, making it easier to set up and maintain compared to more complex configurations required by other tools.

4. **Built-in Support for Modern JavaScript:**
   - Vite has built-in support for modern JavaScript features and TypeScript, making it easy to use the latest language features without additional configuration. This aligns well with the goals of the project, which aims to provide a modern and efficient development experience.

5. **Hot Module Replacement (HMR):**
   - Vite’s HMR is designed to be fast and efficient, allowing for instant updates without losing the application state. This feature is particularly beneficial during development as it enhances productivity by providing immediate feedback on code changes.

6. **Out-of-the-box Support for CSS and CSS Preprocessors:**
   - Vite supports CSS and popular CSS preprocessors like Sass and Less. This makes it easy to manage styles in a modular and maintainable way, enhancing the overall developer experience.

7. **Reduced Build Times:**
   - Vite’s approach of pre-bundling dependencies using esbuild results in drastically reduced build times compared to traditional tools. This is especially beneficial for large projects with many dependencies.

8. **Enhanced Developer Experience:**
   - With features like instant server start, optimized build performance, and minimal configuration, Vite significantly enhances the overall developer experience. This allows developers to focus more on building features rather than dealing with build tool configurations and performance issues.

By using Vite, this project benefits from improved development speed, optimized production builds, and a better developer experience, making it a suitable choice for modern web development.

### Setting Up Vite in the Project

1. **Navigate to the `vite-project` directory:**
    ```sh
    cd vite-project
    ```

2. **Install the dependencies:**
    ```sh
    npm install
    ```

3. **Run the Vite development server:**
    ```sh
    npm run dev
    ```

By following these steps, you can set up and start the Vite development server for this project, leveraging its benefits for an improved development workflow.
