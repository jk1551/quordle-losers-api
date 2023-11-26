# Quordle Losers API 🎮

Welcome to the Quordle Losers API, your gateway to fascinating data insights from the Quordle game! 🧠🔤

## Endpoints

### Insert a New Score
- **Endpoint:** `/scores`
  - **Method:** POST
  - **Description:** Add a new score to the Quordle game.
  - **Request Body:**
    ```json
    {
      "userId": 123,
      "score": 42
    }
    ```
  - **Response:**
    ```json
    {
      "message": "Score added successfully"
    }
    ```

### Retrieve All Scores
- **Endpoint:** `/scores`
  - **Method:** GET
  - **Description:** Get all scores recorded in the Quordle game.
  - **Response:**
    ```json
    [
      {"id": 1, "userId": 123, "scoreDate": "2023-11-25", "score": 42},
      {"id": 2, "userId": 456, "scoreDate": "2023-11-25", "score": 37},
      ...
    ]
    ```

### Retrieve Scores by User ID
- **Endpoint:** `/scores/{user_id}`
  - **Method:** GET
  - **Description:** Get scores for a specific user in the Quordle game.
  - **Path Parameters:**
    - `user_id` (int): The ID of the user.
  - **Response:**
    ```json
    [
      {"id": 1, "userId": 123, "scoreDate": "2023-11-25", "score": 42},
      {"id": 5, "userId": 123, "scoreDate": "2023-11-24", "score": 35},
      ...
    ]
    ```

## Getting Started
To interact with the Quordle Losers API, follow these steps:

1. **Run the API:**
   ```bash
   uvicorn main:app --reload
