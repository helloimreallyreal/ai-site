from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/summary", methods=["GET"])
def summarize():
    query = request.args.get("q")
    if not query:
        return jsonify({"error": "No query"}), 400

    # Use DuckDuckGo to get info
    ddg_url = f"https://api.duckduckgo.com/?q={query}&format=json&no_html=1"
    res = requests.get(ddg_url).json()
    text = res.get("AbstractText", "No summary found")

    # Placeholder: add Gemini or LLaMA logic here later
    return jsonify({
        "query": query,
        "summary": text
    })

if __name__ == "__main__":
    app.run()
