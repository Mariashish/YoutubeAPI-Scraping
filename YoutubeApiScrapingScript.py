{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e13e6601-4095-4151-af11-696470f0e1d0",
   "metadata": {
    "collapsed": true,
    "jupyter": {
     "outputs_hidden": true
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: google-api-python-client in c:\\users\\danii\\anaconda3\\lib\\site-packages (2.108.0)Note: you may need to restart the kernel to use updated packages.\n",
      "\n",
      "Requirement already satisfied: google-auth-httplib2>=0.1.0 in c:\\users\\danii\\anaconda3\\lib\\site-packages (from google-api-python-client) (0.1.1)\n",
      "Requirement already satisfied: google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0.dev0,>=1.31.5 in c:\\users\\danii\\anaconda3\\lib\\site-packages (from google-api-python-client) (2.14.0)\n",
      "Requirement already satisfied: uritemplate<5,>=3.0.1 in c:\\users\\danii\\anaconda3\\lib\\site-packages (from google-api-python-client) (4.1.1)\n",
      "Requirement already satisfied: google-auth<3.0.0.dev0,>=1.19.0 in c:\\users\\danii\\anaconda3\\lib\\site-packages (from google-api-python-client) (2.23.4)\n",
      "Requirement already satisfied: httplib2<1.dev0,>=0.15.0 in c:\\users\\danii\\anaconda3\\lib\\site-packages (from google-api-python-client) (0.22.0)\n",
      "Requirement already satisfied: protobuf!=3.20.0,!=3.20.1,!=4.21.0,!=4.21.1,!=4.21.2,!=4.21.3,!=4.21.4,!=4.21.5,<5.0.0.dev0,>=3.19.5 in c:\\users\\danii\\anaconda3\\lib\\site-packages (from google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0.dev0,>=1.31.5->google-api-python-client) (4.25.1)\n",
      "Requirement already satisfied: requests<3.0.0.dev0,>=2.18.0 in c:\\users\\danii\\anaconda3\\lib\\site-packages (from google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0.dev0,>=1.31.5->google-api-python-client) (2.27.1)\n",
      "Requirement already satisfied: googleapis-common-protos<2.0.dev0,>=1.56.2 in c:\\users\\danii\\anaconda3\\lib\\site-packages (from google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0.dev0,>=1.31.5->google-api-python-client) (1.61.0)\n",
      "Requirement already satisfied: cachetools<6.0,>=2.0.0 in c:\\users\\danii\\anaconda3\\lib\\site-packages (from google-auth<3.0.0.dev0,>=1.19.0->google-api-python-client) (4.2.2)\n",
      "Requirement already satisfied: pyasn1-modules>=0.2.1 in c:\\users\\danii\\anaconda3\\lib\\site-packages (from google-auth<3.0.0.dev0,>=1.19.0->google-api-python-client) (0.2.8)\n",
      "Requirement already satisfied: rsa<5,>=3.1.4 in c:\\users\\danii\\anaconda3\\lib\\site-packages (from google-auth<3.0.0.dev0,>=1.19.0->google-api-python-client) (4.7.2)\n",
      "Requirement already satisfied: pyparsing!=3.0.0,!=3.0.1,!=3.0.2,!=3.0.3,<4,>=2.4.2 in c:\\users\\danii\\anaconda3\\lib\\site-packages (from httplib2<1.dev0,>=0.15.0->google-api-python-client) (3.0.4)\n",
      "Requirement already satisfied: pyasn1<0.5.0,>=0.4.6 in c:\\users\\danii\\anaconda3\\lib\\site-packages (from pyasn1-modules>=0.2.1->google-auth<3.0.0.dev0,>=1.19.0->google-api-python-client) (0.4.8)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\danii\\anaconda3\\lib\\site-packages (from requests<3.0.0.dev0,>=2.18.0->google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0.dev0,>=1.31.5->google-api-python-client) (3.3)\n",
      "Requirement already satisfied: charset-normalizer~=2.0.0 in c:\\users\\danii\\anaconda3\\lib\\site-packages (from requests<3.0.0.dev0,>=2.18.0->google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0.dev0,>=1.31.5->google-api-python-client) (2.0.4)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\danii\\anaconda3\\lib\\site-packages (from requests<3.0.0.dev0,>=2.18.0->google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0.dev0,>=1.31.5->google-api-python-client) (2021.10.8)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\\users\\danii\\anaconda3\\lib\\site-packages (from requests<3.0.0.dev0,>=2.18.0->google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0.dev0,>=1.31.5->google-api-python-client) (1.26.9)\n"
     ]
    }
   ],
   "source": [
    "pip install google-api-python-client"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9bc8340d-7aa2-4123-bf0d-e30c5366f291",
   "metadata": {
    "collapsed": true,
    "jupyter": {
     "outputs_hidden": true
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: isodate in c:\\users\\danii\\anaconda3\\lib\\site-packages (0.6.1)\n",
      "Requirement already satisfied: six in c:\\users\\danii\\appdata\\roaming\\python\\python39\\site-packages (from isodate) (1.16.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install isodate"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "8e52b54e-af23-429c-83ef-ef53b2ed64d7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Scraping andato a buon fine, il Dataset è stato creato e salvato nel file 'youtube_data.csv'.\n"
     ]
    }
   ],
   "source": [
    "# Importo la libreria csv per salvare il Dataset in formato csv una volta scaricati i dati\n",
    "import csv \n",
    "\n",
    "# Importo la libreria per interfacciarsi con le API di Google\n",
    "from googleapiclient.discovery import build \n",
    "\n",
    "# Importo la libreria per rendere la durata del video in un formato più leggibile\n",
    "from isodate import parse_duration \n",
    "\n",
    "# Definisco una funzione per ottenere dati da un canale Youtube \n",
    "def get_youtube_data(api_key, channel_id, max_results=400): \n",
    "    # Importo l'oggetto youtube con la chiave api fornita\n",
    "    youtube = build(\"youtube\", \"v3\", developerKey=api_key) \n",
    "\n",
    "    # Ottengo l'ID della playlist degli upload del canale\n",
    "    channel_response = youtube.channels().list(\n",
    "        part=\"contentDetails\",\n",
    "        id=channel_id\n",
    "    ).execute()\n",
    "\n",
    "    # Estraggo l'ID della playlist degli upload\n",
    "    uploads_playlist_id = channel_response[\"items\"][0][\"contentDetails\"][\"relatedPlaylists\"][\"uploads\"]\n",
    "\n",
    "    # Ottengo gli ultimi 400 video della playlist degli upload\n",
    "    data = []\n",
    "\n",
    "    next_page_token = None\n",
    "\n",
    "    while len(data) < max_results:\n",
    "        # Ottengo i dettagli dei video nella playlist\n",
    "        request = youtube.playlistItems().list(\n",
    "            part=\"snippet\",\n",
    "            playlistId=uploads_playlist_id,\n",
    "            maxResults=min(50, max_results - len(data)),\n",
    "            pageToken=next_page_token\n",
    "        )\n",
    "\n",
    "        # Eseguo la richiesta\n",
    "        response = request.execute()\n",
    "\n",
    "        # Ciclo for che ottiene dettagli aggiuntivi per ciascun video\n",
    "        for item in response[\"items\"]: \n",
    "            video_id = item[\"snippet\"][\"resourceId\"][\"videoId\"]\n",
    "            \n",
    "            # Ottengo ulteriori dettagli per ciascun video\n",
    "            video_details = youtube.videos().list(\n",
    "                part=\"snippet,contentDetails,statistics\",\n",
    "                id=video_id\n",
    "            ).execute()\n",
    "\n",
    "            # Estraggo le informazioni desiderate per ciascun video\n",
    "            video_title = video_details[\"items\"][0][\"snippet\"][\"title\"]\n",
    "            video_date = video_details[\"items\"][0][\"snippet\"][\"publishedAt\"]\n",
    "            video_likes = video_details[\"items\"][0][\"statistics\"].get(\"likeCount\", 0)\n",
    "            video_comments = video_details[\"items\"][0][\"statistics\"].get(\"commentCount\", 0)\n",
    "            video_views = video_details[\"items\"][0][\"statistics\"].get(\"viewCount\", 0)\n",
    "            video_duration = parse_duration(video_details[\"items\"][0][\"contentDetails\"][\"duration\"]).total_seconds()\n",
    "\n",
    "            # Aggiungo i dati del video alla lista\n",
    "            data.append({\n",
    "                \"VideoTitle\": video_title,\n",
    "                \"VideoDate\": video_date,\n",
    "                \"nLikes\": video_likes,\n",
    "                \"nComments\": video_comments,\n",
    "                \"nViews\": video_views,\n",
    "                \"Duration(seconds)\": video_duration\n",
    "            })\n",
    "\n",
    "        next_page_token = response.get(\"nextPageToken\")\n",
    "\n",
    "        if not next_page_token:\n",
    "            break\n",
    "\n",
    "    return data\n",
    "\n",
    "# Definisco una funzione per salvare i dati in un file csv\n",
    "def save_to_csv(data, filename=\"youtube_data.csv\"):\n",
    "    # Salvo i dati nel file csv specificato\n",
    "    with open(filename, mode='w', newline='', encoding='utf-8') as file: \n",
    "        fieldnames = [\"VideoTitle\", \"VideoDate\", \"nLikes\", \"nComments\", \"nViews\", \"Duration(seconds)\"]\n",
    "        \n",
    "        # Inizializzo il writer per il file CSV\n",
    "        writer = csv.DictWriter(file, fieldnames=fieldnames)\n",
    "\n",
    "        # Scrivo l'header\n",
    "        writer.writeheader()\n",
    "\n",
    "        # Scrivo i dati nel file CSV\n",
    "        writer.writerows(data)\n",
    "\n",
    "# Verifico se lo script è eseguito direttamente\n",
    "if __name__ == \"__main__\":\n",
    "   \n",
    "    # L'API key è personale, si puà visualizzare cercando su Google for Developers \"Youtube Data API\"\n",
    "    api_key = \"YourAPIkey\" \n",
    "    channel_id = \"DesiredChannelID\" # L'ID del canale desiderato si ottiene direttamente da Youtube\n",
    "   \n",
    "    # Ottengo i dati dal canale YouTube\n",
    "    youtube_data = get_youtube_data(api_key, channel_id)\n",
    "    \n",
    "    # Salvo i dati nel file CSV\n",
    "    save_to_csv(youtube_data)\n",
    "\n",
    "    # Stampo un messaggio indicando che lo scraping è andato a buon fine\n",
    "    print(\"Lo scraping è andato a buon fine, il Dataset è stato creato e salvato nel file 'youtube_data.csv'.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "b46eece2-af7f-4c8a-8301-5abefa82b2c9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Importo la libreria per gestire e modificare il Dataset\n",
    "import pandas as pd \n",
    "\n",
    "# Importo le librerie necessarie per gestire il tempo\n",
    "from datetime import datetime, timezone, timedelta \n",
    "\n",
    "# Carico il DataFrame da un file CSV\n",
    "df = pd.read_csv('youtube_data.csv')\n",
    "\n",
    "# Creo una funzione per calcolare l'età del video a partire dalla data di pubblicazione\n",
    "def calculate_video_age(published_at):\n",
    "    # Converto la data di pubblicazione in un oggetto datetime\n",
    "    published_date = datetime.strptime(published_at, \"%Y-%m-%dT%H:%M:%SZ\")\n",
    "\n",
    "    # Imposto il fuso orario su UTC per rendere l'oggetto datetime \"offset-aware\"\n",
    "    published_date = published_date.replace(tzinfo=timezone.utc)\n",
    "\n",
    "    # Ottengo la data e l'ora corrente \n",
    "    current_date = datetime.now(timezone.utc)\n",
    "\n",
    "    # Calcolo la differenza tra la data di pubblicazione e la data corrente\n",
    "    age = current_date - published_date\n",
    "\n",
    "    # Restituisce l'età del video in giorni\n",
    "    return age.days\n",
    "\n",
    "# Stampo il DataFrame risultante\n",
    "print(df)\n",
    "\n",
    "# Salvo il DataFrame aggiornato nel file CSV originale\n",
    "df.to_csv('youtube_data.csv', index=False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dea46fb8-57d8-45cc-aaab-b615a6d89f2a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
