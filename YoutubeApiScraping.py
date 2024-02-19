# Creazione del Dataset tramite Google API Scraping
pip install google-api-python-client
pip install isodate

# Importo la libreria csv per salvare il Dataset in formato csv una volta scaricati i dati
import csv

# Importo la libreria per interfacciarsi con le API di Google
from googleapiclient.discovery import build

# Importo la libreria per rendere la durata del video in un formato più leggibile
from isodate import parse_duration


# Definisco una funzione per ottenere dati da un canale Youtube
def get_youtube_data(api_key, channel_id, max_results=400):
    # Importo l'oggetto youtube con la chiave api fornita
    youtube = build("youtube", "v3", developerKey=api_key)

    # Ottengo l'ID della playlist degli upload del canale
    channel_response = youtube.channels().list(
        part="contentDetails",
        id=channel_id
    ).execute()

    # Estraggo l'ID della playlist degli upload
    uploads_playlist_id = channel_response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

    # Ottengo gli ultimi 400 video della playlist degli upload
    data = []

    next_page_token = None

    while len(data) < max_results:
        # Ottengo i dettagli dei video nella playlist
        request = youtube.playlistItems().list(
            part="snippet",
            playlistId=uploads_playlist_id,
            maxResults=min(50, max_results - len(data)),
            pageToken=next_page_token
        )

        # Eseguo la richiesta
        response = request.execute()

        # Ciclo for che ottiene dettagli aggiuntivi per ciascun video
        for item in response["items"]:
            video_id = item["snippet"]["resourceId"]["videoId"]

            # Ottengo ulteriori dettagli per ciascun video
            video_details = youtube.videos().list(
                part="snippet,contentDetails,statistics",
                id=video_id
            ).execute()

            # Estraggo le informazioni desiderate per ciascun video
            video_title = video_details["items"][0]["snippet"]["title"]
            video_date = video_details["items"][0]["snippet"]["publishedAt"]
            video_likes = video_details["items"][0]["statistics"].get("likeCount", 0)
            video_comments = video_details["items"][0]["statistics"].get("commentCount", 0)
            video_views = video_details["items"][0]["statistics"].get("viewCount", 0)
            video_duration = parse_duration(video_details["items"][0]["contentDetails"]["duration"]).total_seconds()

            # Aggiungo i dati del video alla lista
            data.append({
                "VideoTitle": video_title,
                "VideoDate": video_date,
                "nLikes": video_likes,
                "nComments": video_comments,
                "nViews": video_views,
                "Duration(seconds)": video_duration
            })

        next_page_token = response.get("nextPageToken")

        if not next_page_token:
            break

    return data


# Definisco una funzione per salvare i dati in un file csv
def save_to_csv(data, filename="youtube_data.csv"):
    # Salvo i dati nel file csv specificato
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ["VideoTitle", "VideoDate", "nLikes", "nComments", "nViews", "Duration(seconds)"]

        # Inizializzo il writer per il file CSV
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Scrivo l'header
        writer.writeheader()

        # Scrivo i dati nel file CSV
        writer.writerows(data)


# Verifico se lo script è eseguito direttamente
if __name__ == "__main__":
    # Sostituisci api_key e channel_id con la tua API key e l'ID del canale desiderato
    api_key = "AIzaSyB7Jnanmwa1gEC--MilXixLCnqKuWg2YF8"
    channel_id = "UCX6OQ3DkcsbYNE6H8uQQuVA"

    # Ottengo i dati dal canale YouTube
    youtube_data = get_youtube_data(api_key, channel_id)

    # Salvo i dati nel file CSV
    save_to_csv(youtube_data)

    # Stampo un messaggio indicando che lo scraping è andato a buon fine
    print("Lo scraping è andato a buon fine, il Dataset è stato creato e salvato nel file 'youtube_data.csv'.")
