# QuickRead - Article Summarizer 🌐✂️

For my CS50 final project, I created a web-based application called AI Article Summarizer, which leverages artificial intelligence to simplify long-form online content into concise, readable summaries. This tool is especially useful for students, researchers, and professionals who regularly consume news or academic material and need to distill key points quickly without going through entire texts.

The motivation behind this project stemmed from the increasing volume of online content and the limited time users have to read it. With the rising accessibility of powerful natural language processing (NLP) models, I wanted to explore how these AI tools could be applied to real-world use cases. Text summarization is a common NLP task, and it seemed like an ideal challenge to tackle using the tools and programming skills I’ve acquired throughout the CS50 course.

Functionality
The AI Article Summarizer accepts a URL as input, fetches the article’s main content using web scraping, processes the extracted text using an AI model, and returns a short summary to the user. It’s built using the Flask web framework in Python, which manages routing, form input, and response rendering. For scraping, the app uses the newspaper3k library, a robust tool for parsing article content, removing boilerplate, and cleaning HTML noise.

Once the article content is obtained, it’s passed to a transformer-based summarization model from Hugging Face’s transformers library—specifically, models like facebook/bart-large-cnn or t5-small. These models are capable of understanding large amounts of text and generating meaningful abstractive summaries, not just shortened versions of the text.

The app interface is kept minimal and clean, following modern web design principles. Users are greeted with a logo, a short title, a URL input box, and a “Summarize” button. After submission, the app fetches and displays the article’s title and its AI-generated summary.

Technology Stack
Frontend: HTML, CSS (with minimal custom styling), Jinja2 templates

Backend: Python with Flask

NLP/AI: Hugging Face Transformers (transformers, torch)

Web Scraping: newspaper3k, lxml, nltk

Deployment Ready: Works locally and can be deployed on platforms like Render or Codespaces

To ensure performance and minimize complexity, the summarization is done using a pre-trained model loaded directly from Hugging Face's model hub. While the response time may vary depending on model size, inference happens within a few seconds even without GPU acceleration.

Challenges and Learning Outcomes
One of the early challenges I faced was integrating AI models with real-time user input. Working with Hugging Face's transformers was straightforward, but I had to manage dependencies like torch, nltk, and lxml, and ensure that the required tokenizer data (e.g., punkt) was properly downloaded to avoid runtime errors.

Another learning point was understanding the difference between extractive summarization and abstractive summarization. While earlier versions of the app simply shortened the article (extractive), this final version uses transformer-based models that generate entirely new sentences that capture the article’s essence, making it much more intelligent and useful.

Additionally, I learned to handle errors gracefully, such as invalid URLs, missing article content, or network issues during scraping or inference. I also experimented with multiple AI models to balance performance and summary quality, including t5-small for quicker results and bart-large-cnn for more accurate outputs.

Use Cases and Impact
The tool has several practical applications:

Students can use it to summarize academic articles or blog posts for quick reference.

Professionals can use it to scan news or reports without reading full articles.

Researchers can test it with various domains to extract key points from papers or online resources.

As content continues to grow online, such summarization tools can significantly reduce information overload and make knowledge more accessible.

Future Improvements
Although the current version works well, there are several improvements I’d like to explore:

GPU Acceleration: Enable local GPU inference for faster summarization

Multiple Model Choices: Let users pick between models based on speed vs. accuracy

PDF/Text Upload: Allow users to upload documents directly, not just URLs

Downloadable Output: Enable users to export summaries as PDF or text files

Mobile Optimization & UI Enhancements: Make the interface even more responsive and professional-looking

Conclusion
This project was a great culmination of everything I learned in CS50—from routing and HTML templating to integrating advanced machine learning models into a web app. It challenged me to combine frontend and backend development with real-world APIs and AI systems, while also focusing on user experience and performance.

The AI Article Summarizer is a functional, scalable, and practical tool that applies CS50 principles to solve a modern problem using modern technology.

# Features

- Web scraping using `newspaper3k`
- Summarization via Hugging Face Transformers (e.g., `facebook/bart-large-cnn`)
- Error handling for invalid or long URLs

# How to Run

1. **Clone this repo**
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the app:
    ```bash
    python app.py
    ```


