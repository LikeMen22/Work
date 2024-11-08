# Work
Practical Test for Dalibor Jaroš.

1) Create an HTML page with one input field
✔️ Yes, I have created an HTML page with an input field where you can type a keyword. It also includes a button to trigger the search functionality.

2) Enter a keyword into the input field
✔️ Yes, you can enter a keyword (e.g., "Python") into the input field.

3) Receive search results from Google's first page (organic results only) in a machine-readable structured format (excluding HTML and without using Google API)
✘ Partially. Currently, the search results are mock data generated within the application. These results simulate what you would see from Google search results, but they are not real Google results. We can’t fetch actual Google search results directly without using their API or a web scraping method (which has legal and technical concerns). The current results are simulated for testing purposes.

✔️ However, you can download these results in a machine-readable format like JSON if you choose to add that feature.

4) Host the application somewhere on the internet where we can test it
✘ Not done yet. We haven't deployed the app online yet. You could deploy it to platforms like Heroku or PythonAnywhere for free hosting, or use Ngrok for temporary local testing but i tested on solely on pc using Python and HTML so.

5) Record a video where you explain the functionality of the code and solution
✘ Not done yet. You will need to record a video explaining how the application works, how to run it, and any key points about the code. You can use tools like Vidyard or Loom for quick screen recordings. I currently dont have time but ill leave explanation down below. If you think i have passing grade i can make the video later.

6) Include the source code and send it via email
✔️ I will be sending private github link instead.

What Needs to Be Done:

Real Google Search Results: To get real Google search results, you'd need to use web scraping or a third-party service. However, scraping Google can violate their terms of service, so am not gonna do that.

Explanation:

1. Application Overview
This application is a simple Flask-based web app that simulates a search engine. When a user enters a keyword into the input field, the application generates mock search results based on that keyword. These results are displayed in a list below the input field, simulating what one might expect to see on a search results page.

Although the search results are mock data (simulated for testing purposes), they mimic the kind of results you would expect from a search engine, such as a title and URL.

2. How the Application Works
Here’s a breakdown of how the app functions:

User Input:

The user opens the HTML page and is presented with an input field where they can type in a keyword (e.g., "Python").
Search Action:

When the user types a keyword and clicks the "Search" button, the app sends the keyword to the server via a POST request.
Server Logic (Python/Flask):

The server receives the POST request with the keyword, processes it, and generates a list of mock search results. These results are constructed dynamically using the keyword the user entered.
The server then sends back the mock results in JSON format.
Displaying Results:

The results are displayed on the page below the input field. Each result has a title and a URL that are based on the user’s keyword.
Optional Feature:

While the current app does not save the results, we can add a feature to allow users to download these results in a machine-readable format (like JSON).
3. How to Run the Application Locally
Install Python: Make sure Python (3.6 or higher) is installed on your system.

Clone or Download the Project Files:

You need the project files, which include the app.py (Flask code) and the HTML file. If the files are shared with you as a zip, extract them to a folder.
Install Flask:

Open a terminal (command prompt) and navigate to the project folder.
Run this command to install Flask:
bash
Zkopírovat kód
pip install flask
Run the Application:

In the same terminal, run the application with the following command:
bash
Zkopírovat kód
python app.py
The Flask server will start, and you will see a message indicating the app is running on http://127.0.0.1:5000.
Open the Application in a Browser:

Open your browser and go to http://127.0.0.1:5000. You should see the input field where you can enter a search keyword.
Test the App:

Type a keyword (e.g., "Python") into the input field and click "Search". Mock search results will appear below the input field.
4. Breakdown of the Code
The code consists of two main parts: the HTML front-end and the Flask back-end.

HTML Page (index.html):

The HTML file contains:
A simple form with an input field (<input type="text">) for the user to type in a keyword.
A button (<button>) that triggers the search.
A section (<div>) where the search results are displayed after the search action.
Flask Server (app.py):

Flask Setup:
We create a Flask app using Flask(__name__).
The server listens for a POST request to the /search endpoint.
Handling Search Requests:
The search function (@app.route('/search', methods=['POST'])) retrieves the keyword from the incoming request using request.get_json().
A list of mock results is generated by using the keyword in the titles and URLs of the results.
The mock results are then sent back to the client in JSON format using jsonify().
Client-Side (JavaScript):

The HTML file uses JavaScript (via the Fetch API) to send the keyword to the Flask server when the "Search" button is clicked. It sends the request as a POST with the entered keyword.
The response is processed and displayed as search results on the webpage.
