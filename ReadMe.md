# FastAPI + Next.js Workout Routine Application

This application is a web-based workout routine manager built using Python's FastAPI, Pydantic, SQLAlchemy, and Next.js.

## Running the Project Locally

Follow these steps to set up and run the project on your local machine:

1. **Clone the Repository**: 
   Clone this repository and navigate into its directory.

2. **Create a Virtual Environment**: 
   ```bash
   python3.9 -m venv venv
   ```

3. **Activate the Virtual Environment**: 
   - For macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - For Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Install Requirements**: 
   Install the necessary dependencies by running:
   ```bash
   pip install -r requirements.txt
   ```

5. **Start the FastAPI Server**: 
   Launch the application with:
   ```bash
   uvicorn api.main:app --reload
   ```

6. **Set Up the Next.js Client**: 
   Open a new terminal window and navigate to the `nextjs` folder.

7. **Install Client Dependencies**: 
   Run the following command to install the required packages:
   ```bash
   npm install
   ```

8. **Run the Next.js Development Server**: 
   Start the client application with:
   ```bash
   npm run dev
   ```

9. **Testing the Application**: 
   You can test the project by creating workouts and configuring routines. 