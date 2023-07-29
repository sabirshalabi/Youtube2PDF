# youtube2pdf

youtube2pdf is a Flask web app that generates PDF transcripts from YouTube videos. 

## Features

- Enter a YouTube URL and the app will download the video transcript
- Preview the transcript directly on the web app  
- Download the full transcript as a PDF file

## Usage

1. Clone the repo

```
git clone https://github.com/yourname/youtube2pdf
```

2. Install dependencies

```
pip install -r requirements.txt 
```

3. Set the environment variable

```
export FLASK_APP=app.py
```

4. Run the app

```
flask run
```

5. Navigate to http://localhost:5000

6. Paste a YouTube URL and click "Get Transcript"

7. Preview the transcript or download as PDF

## Deployment

This app can be deployed to any service that supports Python apps like Heroku, AWS Elastic Beanstalk, App Engine, etc.

An example Dockerfile is included for Docker deployment.

## Built With

- [Flask](https://flask.palletsprojects.com/) - Web framework
- [youtube_transcript_api](https://github.com/jdepoix/youtube-transcript-api) - YouTube transcript scraper
- [FPDF](https://pyfpdf.readthedocs.io/en/latest/) - PDF generation

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Hat tip to anyone whose code was used
- Inspiration
- etc