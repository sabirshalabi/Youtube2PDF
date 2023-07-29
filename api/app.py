from flask import Flask, render_template, request, send_file
from main import get_transcript, get_video_title, create_pdf
import os
import re

app = Flask(__name__, template_folder='../templates')

transcript = None
file_name = None

@app.route('/', methods=['GET', 'POST'])
def home():
    global transcript
    global file_name
    if request.method == 'POST':
        url = request.form.get("url")
        if not re.match(r'https?://(www\.)?youtube.com/watch\?v=\w+', url):
            return render_template('index.html', error="Invalid YouTube URL")
        transcript = get_transcript(url)
        full_text = " ".join([res["text"] for res in transcript])
        preview = full_text[:500] + "..."
        title = get_video_title(url)
        file_name = f"{title}.pdf"
        create_pdf(full_text, file_name)
        return render_template('index.html', transcript=preview)
    return render_template('index.html')


@app.route('/download', methods=['GET', 'POST'])
def download():
    global file_name
    file_path = f"./{file_name}"
    return send_file(file_path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
