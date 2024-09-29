DeviantArt Bot Uploader
This bot automates the process of uploading images to DeviantArt using the DeviantArt API. It submits images to DeviantArt's Sta.sh as a temporary holding area and then publishes them to your featured gallery and/or a custom gallery of your choice.

What the Program Does
Creates a Flask server: The script sets up a Flask server that listens on a specific URL, which is used to connect the bot with your DeviantArt application. This allows for secure OAuth2 authorization.
Handles OAuth2 Authentication: Once the connection is established through the redirect URL, the bot can interact with your DeviantArt account.
Uploads to Sta.sh: The bot uploads images to Sta.sh, a temporary storage location on DeviantArt.
Final Commit to Galleries: After uploading to Sta.sh, the bot publishes the image to the "Featured" gallery and, optionally, to a custom gallery created by the user.

Prerequisites
Create an "Application" on DeviantArt:

Go to DeviantArt Developers.
Click on "Create Application" and upload an image to represent your application (any image is fine).
Fill in the required fields:
Title: Use "Upload" or any name you like.
Description: This can be anything, e.g., "Automated uploader for my gallery".
OAuth2 Grant Type: Choose authorization code.
OAuth2 Redirect URI whitelist: Enter a URL where your local machine can be accessed from the outside. This can be a dynamic DNS pointing to your machine. Example: http://hey.mydomainname.com.
Important: Disable comments on the image post for the application on DeviantArt (to avoid unnecessary comments on the app's image).
Save the application and note down the client_id and client_secret.
Add the client_id and client_secret to the configuration:

Copy the config.dist.json to config.json.
Enter your client_id and client_secret from the DeviantArt application into the config.json.
Find the gallery_id:

Use the DeviantArt Developers Console.
Go to Gallery /folders to retrieve the folder id for the gallery where you want to upload your images.
Configuration
Rename config.dist.json to config.json.
Edit config.json and fill in the following details:
"client_id": Your DeviantArt application client ID.
"client_secret": Your DeviantArt application client secret.
"redirect_uri": The URL you used for the OAuth2 Redirect URI whitelist.

The script will:
Open a browser window to authenticate with DeviantArt.
Set up a local Flask server to listen for the OAuth2 redirect URI, facilitating the connection between your application and DeviantArt.
Submit images to DeviantArt's Sta.sh.
Commit the images from Sta.sh to your "Featured" gallery and optionally to a custom user-created gallery.

Additional Notes
Ensure your local machine is accessible from the outside (if required) to work with the OAuth2 Redirect URI.
This bot uses the DeviantArt API to upload images

This README.md was redacted with chatgpt