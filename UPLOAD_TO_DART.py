from flask import Flask, request
import requests
import webbrowser
import os
import sys
import threading
import shutil
import time
import json

app = Flask(__name__)

# Charger les informations de configuration à partir du fichier JSON
def load_config():
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
    return config

# Fonction pour obtenir le token d'accès
def get_access_token(client_id, client_secret, code, redirect_uri):
    url = "https://www.deviantart.com/oauth2/token"
    payload = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": redirect_uri
    }
    response = requests.post(url, data=payload)
    if response.ok:
        return response.json().get("access_token")
    else:
        return None

# Fonction pour soumettre une image à Sta.sh
def submit_to_stash(access_token, image_path, title, tags):
    url = "https://www.deviantart.com/api/v1/oauth2/stash/submit"
    headers = {"Authorization": f"Bearer {access_token}"}
    files = {'image': open(image_path, 'rb')}
    data = {
        "title": title,
        "tags[0]": tags[0],
        "tags[1]": tags[1],
        "tags[2]": tags[2]
    }
    response = requests.post(url, headers=headers, files=files, data=data)
    if response.ok:
        return response.json().get("itemid")
    else:
        return None

# Fonction pour publier une image de Sta.sh sur DeviantArt
def publish_from_stash(access_token, itemid, gallery_id):
    url = "https://www.deviantart.com/api/v1/oauth2/stash/publish"
    headers = {"Authorization": f"Bearer {access_token}"}
    data = {
        "validate_token": access_token,
        "itemid": itemid,
        "galleryids[0]": gallery_id[0],
        "galleryids[1]": gallery_id[1],
        "is_mature": "true",
        "mature_level": "moderate",
        "mature_classification": "sexual",
        "agree_submission": "true",
        "agree_tos": "true",
        "feature": "true",
        "allow_comments": "true",
        "display_resolution": "0",
        "sharing": "allow",
        "allow_free_download": "true",
        "add_watermark": "false",
        "mature_content": "true"
    }

    response = requests.post(url, headers=headers, data=data)
    return response.json()

def run_flask_app():
    app.run(port=5088)

@app.route('/stop')
def stop_flask_app():
    # Utiliser 'os._exit(0)' pour arrêter l'application
    os._exit(0)

@app.route('/')
def receive_code():
    code = request.args.get('code')
    if code:
        print(f"Received Authorization Code: {code}")
        
        # Charger la configuration
        config = load_config()
        client_id = config['client_id']
        client_secret = config['client_secret']
        redirect_uri = config['redirect_uri']
        
        # Échanger le code contre un token
        access_token = get_access_token(client_id, client_secret, code, redirect_uri)

        # Info Images # <-- A RENSEIGNER ICI
        ####################################
        title_info = sys.argv[1]  # Premier argument après le nom du script
        tags_temp = title_info.split(" ")
        tags_info = [tag[1:] for tag in tags_temp]
        ####################################

        # Featured gallery
        gallery_id = ["1551DEF0-436F-4D02-FA1A-9018FB8737C9"]
        gallery_id.append(sys.argv[2])

        # Si obtention du token, alors continuer
        if access_token:
            print("Token d'accès obtenu :", access_token)

            # on parcours la liste des fichiers pour les uploader un à un
            directory_file_to_upload = r"C:\AI_TEMP_UPLOAD\_AI_UPLOAD_DART"
            done_directory = os.path.join(directory_file_to_upload, "done")

            for filename_to_upload in os.listdir(directory_file_to_upload):
                if filename_to_upload.endswith(".png"):
                    file_path = os.path.join(directory_file_to_upload, filename_to_upload)
                    print(f"Uploading {file_path}...")

                    # DEVIANT_ART STASH
                    itemid = submit_to_stash(access_token, file_path, title_info, tags_info)
                    if itemid:
                        print("Image soumise à Sta.sh, Item ID :", itemid)
                        # DEVIANT SUBMISSION !
                        publish_result = publish_from_stash(access_token, itemid, gallery_id)
                        print(f"Résultat de la publication : ", publish_result)

                        # Déplacer le fichier dans le dossier "done"
                        shutil.move(file_path, os.path.join(done_directory, filename_to_upload))
                    else:
                        return "Échec de la soumission à Sta.sh"
        else:
            return "Échec de l'obtention du token d'accès"

    # Après avoir fini le traitement
    time.sleep(8) # pause de 8 secondes
    stop_flask_app()
    return "Vous pouvez fermer cette page."

if __name__ == '__main__':
    # Charger la configuration
    config = load_config()
    client_id = config['client_id']
    redirect_uri = config['redirect_uri']
    
    auth_url = f"https://www.deviantart.com/oauth2/authorize?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}"
    firefox_path = 'C:/Program Files/Mozilla Firefox/firefox.exe %s'
    webbrowser.get(firefox_path).open(auth_url)

    # Lancer Flask dans un thread séparé
    flask_thread = threading.Thread(target=run_flask_app)
    flask_thread.start()
