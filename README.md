# YouTube API Data Scraping Script

## Overview
This Python script utilizes the YouTube API to extract detailed data from a specified channel. The extracted information includes video title, publication date, likes, comments, views, and video duration. The data is then processed, including calculating the video age in days, the ratio of likes to views rounded to three decimals, and the ratio of comments to views rounded to four decimals. The resulting dataset is saved in a CSV file named 'youtube_data.csv'.

## Prerequisites
Ensure you have the necessary Python libraries installed by running the following commands:
```bash
pip install google-api-python-client
pip install isodate
```

## Usage
Replace placeholders 'YourAPIkey' and 'DesiredChannelID' with your YouTube API key and the ID of the target channel, respectively.
Execute the script.

## Detailed Steps
Import required libraries for CSV handling, Google API interaction, and parsing video durations.
Define a function get_youtube_data to retrieve data from a specified YouTube channel using the provided API key and channel ID.
Define a function save_to_csv to save the retrieved data to a CSV file.
If the script is executed directly, set API key and channel ID, fetch YouTube data, and save it to 'youtube_data.csv'.
Import pandas and datetime libraries for further data manipulation.
Load the dataset from 'youtube_data.csv'.
Create a function calculate_video_age to compute the age of each video in days based on its publication date.
Apply the calculate_video_age function to create a new column 'VideoAge(Days)' in the DataFrame.
Add two new columns: 'Like/Views Ratio' and 'Comments/Views Ratio', representing the ratios of likes to views and comments to views, respectively.
Round the ratios for better readability.
Convert the 'Duration(seconds)' column to an integer data type.
Display the resulting DataFrame.
Save the updated DataFrame to the original CSV file.

## Notes
Ensure the API key is obtained from Google Developers under "Youtube Data API."
The script assumes the availability of necessary Python libraries and a stable internet connection.
You can change the number of videos you want do download to your liking. 400 is just an example.
