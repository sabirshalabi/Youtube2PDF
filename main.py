from youtube_transcript_api import YouTubeTranscriptApi
from fpdf import FPDF
import requests


def get_transcript(url):
    video_id = url.split("=")[-1]
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    # Return transcript directly rather than string
    return transcript


def get_video_title(url):
    video_id = url.split("=")[-1]
    api_key = "AIzaSyBvh9D6v5ADBidazJISKJ7PW76UyJUIuw4"
    url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}"
    res = requests.get(url)
    data = res.json()
    return data["items"][0]["snippet"]["title"]


def create_pdf(full_text, filename):
    pdf = FPDF()
    pdf.add_page()

    # New formatting code
    pdf.set_font("Arial", "B", 15)
    pdf.set_text_color(0, 0, 0)
    pdf.multi_cell(0, 10, full_text, border=0, align='L')

    # Add page numbers
    pdf.set_y(-15)
    pdf.set_font('Arial', 'I', 8)
    pdf.set_text_color(128)
    pdf.cell(0, 10, f'Page {pdf.page_no()}/{{nb}}', align='C')

    pdf.output(filename)


# Main code
if __name__ == "__main__":

    url = input("Enter YouTube URL: ")

    # Get full text
    transcript = get_transcript(url)
    full_text = ""
    for result in transcript:
        full_text += result["text"] + " "

    title = get_video_title(url)
    pdf_name = f"{title}.pdf"

    # Pass full text
    create_pdf(full_text, pdf_name)

    print("Transcript downloaded and converted to PDF successfully!")
