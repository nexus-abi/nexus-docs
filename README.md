# Nexus Docs v3 - Android APK (cloud build)

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

What's new in v3
- Header no longer hides under the status bar / camera cut-out (Android 15 edge-to-edge fix, done in MainActivity via scripts/prep_android.py).
- Phone back button: closes popup > viewer > vehicle detail > goes to Home. Press back twice on Home to exit.
- Documents have a Front and a Back slot. Front + Back is ONE document ("Front + Back"), not "2 files".
- Pull down to refresh, copy document number, share all pages, dark navy header, phone expiry notifications (Profile > Phone notifications).
- New plugins: @capacitor/app, @capacitor/local-notifications (installed automatically by the GitHub build).
