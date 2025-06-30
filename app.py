from flask import Flask, render_template, request
from newspaper import Article
from transformers import pipeline

app = Flask(__name__)

# Load summarization pipeline once when app starts
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

@app.route("/", methods=["GET", "POST"])
def index():
    title = ""
    summary = ""
    error = ""

    if request.method == "POST":
        url = request.form.get("url", "").strip()
        if not url:
            error = "Please enter a valid URL."
        else:
            try:
                article = Article(url)
                article.download()
                article.parse()
                text = article.text

                if not text:
                    error = "No article text found."
                else:
                    # Hugging Face models limit input length (~1024 tokens)
                    max_input_length = 1000  # approx chars, can tweak if needed
                    truncated_text = text[:max_input_length]

                    # Summarize
                    summary_list = summarizer(truncated_text, max_length=130, min_length=30, do_sample=False)
                    summary = summary_list[0]['summary_text']
                    title = article.title

            except Exception as e:
                error = f"Error processing the article: {str(e)}"

    return render_template("index.html", title=title, summary=summary, error=error)


if __name__ == "__main__":
    app.run(debug=True)
