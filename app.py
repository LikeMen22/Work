from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# HTML content for the frontend
html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Search App</title>
</head>
<body>
    <h1>Vyhledávač</h1>
    <input type="text" id="keyword" placeholder="Zadejte klíčové slovo">
    <button onclick="search()">Vyhledat</button>
    <pre id="results"></pre>
    <script>
        async function search() {
            const keyword = document.getElementById('keyword').value;
            const response = await fetch('/search', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ keyword })
            });
            const data = await response.json();
            const results = data.results;  // Extract results from the response
            let output = '';
            results.forEach(result => {
                output += `<a href="${result.url}" target="_blank">${result.title}</a><br>`;
            });
            document.getElementById('results').innerHTML = output;
        }
    </script>
</body>
</html>
'''

# Route for the home page "/"
@app.route('/')
def index():
    return render_template_string(html_content)

# Route for search functionality "/search"
@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()  # Get the JSON data sent via POST
    keyword = data.get("keyword", "")  # Extract the keyword from the request

    # Simulate search results
    mock_results = [
        {"title": f"{keyword} - Výsledek {i+1}", "url": f"https://example.com/{keyword}/{i+1}"}
        for i in range(10)  # Generate 10 results
    ]
    return jsonify({"results": mock_results})  # Return the results as JSON

if __name__ == '__main__':
    app.run(debug=True)

