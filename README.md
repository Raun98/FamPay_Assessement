# FamPay_Assessement
An API that can fetch latest videos from Youtube in reverse chronological order.

# Basic Requirements:

- Server should call the YouTube API continuously in background (async) with some interval (say 10 seconds) for fetching the latest videos for a predefined search query and should store the data of vid eos (specifically these fields - Video title, description, publishing datetime, thumbnails URLs and any other fields you require) in a database with proper indexes.
- A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
- It should be scalable and optimised.

# Setup Guide:

- Start by cloning this project to your computer.
- Install dependencies using `pip install -r requirements.txt` in your terminal.
- As the project runs on YouTube's Data v3 API, an API key is required. It can be obtained by [clicking here](https://developers.google.com/youtube/v3/getting-started)
- Navigate to the settings.py file, find the settings variable **GOOGLE_API_KEYS = [ ... ]**, and adding your __API_KEY__ to this list.
- Open two terminals __parallelly__, on both of them change directory to the *_Fampay_assessment-master/fampay-assessment/fampayWebsite_* directory. There should be a _manage.py_ file in this folder.
- On one terminal window, run `python3 manage.py process_tasks`
- On the other terminal window, run `python3 manage.py runserver`

Django returns a URL to your local host, follow that to find the dashboard.

Thank you for reading! :book: :heart:
