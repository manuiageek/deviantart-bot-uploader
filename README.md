# DeviantArt Bot Uploader

This bot automates the process of uploading images to DeviantArt using the DeviantArt API. It submits images to DeviantArt's Sta.sh as a temporary holding area and then publishes them to your featured gallery and/or a custom gallery of your choice.

## What the Program Does

- **Creates a Flask server**: The script sets up a Flask server that listens on a specific URL, which is used to connect the bot with your DeviantArt application. This allows for secure OAuth2 authorization.
- **Handles OAuth2 Authentication**: Once the connection is established through the redirect URL, the bot can interact with your DeviantArt account.
- **Uploads to Sta.sh**: The bot uploads images to Sta.sh, a temporary storage location on DeviantArt.
- **Final Commit to Galleries**: After uploading to Sta.sh, the bot publishes the image to the "Featured" gallery and, optionally, to a custom gallery created by the user.

## Prerequisites

pip install flask requests

### Create an "Application" on DeviantArt

1. Go to [DeviantArt Developers](https://www.deviantart.com/developers).
2. Click on "Create Application" and upload an image to represent your application (any image is fine).
3. Fill in the required fields:
    - **Title**: Use "Upload" or any name you like.
    - **Description**: This can be anything, e.g., "Automated uploader for my gallery".
    - **OAuth2 Grant Type**: Choose "Authorization code".
    - **OAuth2 Redirect URI whitelist**: Enter a URL where your local machine can be accessed from the outside. This can be a dynamic DNS pointing to your machine. Example: `http://hey.mydomainname.com`.
4. **Important**: Disable comments on the image post for the application on DeviantArt (to avoid unnecessary comments on the app's image).
5. Save the application and note down the `client_id` and `client_secret`.

### Add the `client_id` and `client_secret` to the Configuration

1. Copy `config.dist.json` to `config.json`.
2. Enter your `client_id` and `client_secret` from the DeviantArt application into `config.json`.

### Find the `gallery_id`

1. Use the [DeviantArt Developers Console](https://www.deviantart.com/developers).
2. Go to `Gallery /folders` to retrieve the folder ID for the gallery where you want to upload your images.

## Configuration

1. Rename `config.dist.json` to `config.json`.
2. Edit `config.json` and fill in the following details:
    - `"client_id"`: Your DeviantArt application client ID.
    - `"client_secret"`: Your DeviantArt application client secret.
    - `"redirect_uri"`: The URL you used for the OAuth2 Redirect URI whitelist.

## How the Script Works

1. Opens a browser window to authenticate with DeviantArt.
2. Sets up a local Flask server to listen for the OAuth2 redirect URI, facilitating the connection between your application and DeviantArt.
3. Submits images to DeviantArt's Sta.sh.
4. Commits the images from Sta.sh to your "Featured" gallery and optionally to a custom user-created gallery.

## Additional Notes

- Ensure your local machine is accessible from the outside (if required) to work with the OAuth2 Redirect URI.
- This bot uses the DeviantArt API to upload images.
- You will need firefox for my program to execute properly

---

*This README.md was redacted with ChatGPT.*


# PENTAHO (v9) transformation (kitchen ETL software)
The PENTAHO folder contains pentaho files to automate upload on devian art
It loads an xlsx file (CHARACTER_SELECTOR.xlsx) to get all the information for uploads.
WARNING : don't just execute the program as it might delete from files on your harddrive ! 
Use it as a way to learn how I manage my files in order to make your own version