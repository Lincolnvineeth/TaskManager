# TaskOrganizer

## Description
TaskManager is a collaborative task management solution designed to help users efficiently manage their projects and tasks. It features a user-friendly interface built with Vue.js for the frontend and a robust Flask backend for handling API requests and database interactions.

## Project Structure

backend: This directory contains all the server-side code for the application.

app.py: The main entry point for the Flask application, where the app is initialized and routes are defined.
models.py: Contains the database models, defining the structure of the data (e.g., tasks).
routes.py: Defines the API endpoints for the application, handling incoming requests and returning responses.
config.py: Holds configuration settings for the Flask application, such as database connection details.
requirements.txt: A file listing all the Python packages required to run the backend.
frontend/: This directory contains all the client-side code for the application.

src: The source directory for the Vue.js application.
components: Contains reusable Vue components that represent different parts of the UI (e.g., task lists, folders, comments).
App.Vue: The root component of the Vue application, serving as the main entry point.
public: Contains static assets and the main HTML file.
index.html: The main HTML template where the Vue app is mounted.
tailwind.config.js: Configuration file for Tailwind CSS, which is used for styling the application.
package.json: Lists the Node.js dependencies required for the frontend, along with scripts for building and serving the application.
.gitignore: A file that specifies which files and directories should be ignored by Git, such as virtual environments and node modules.

README.md: A markdown file that provides an overview of the project, installation instructions, usage guidelines, and other relevant information.
