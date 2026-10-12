# Nexus Docs - Android APK (cloud build)

No Android Studio or PC setup needed. GitHub builds the APK for you.

1. Create a free account at github.com and make a new repository (private is fine).
2. Upload everything in this folder (keep the folder layout, including the hidden `.github` folder) and commit to the `main` branch.
3. Open the repo > Actions tab > "Build Android APK". It runs by itself after the upload (about 5 to 8 minutes). You can also press "Run workflow".
4. When it turns green, open the repo > Releases > "Nexus Docs APK" > download NexusDocs.apk on your phone.
5. Open the APK. If Android asks, allow "Install unknown apps" for your browser or Files app.

Notes
- This is a debug-signed APK: fine for your own phone and sharing with family, not for Play Store.
- To update the app later, replace the files in `www/` and commit again. A new APK is built each time.
- Backend (Apps Script) is unchanged from the v2 package: the app talks to the same Google Sheet.
