"""Runs after `npx cap add android`: installs launcher icons and the camera permission."""
import os, re, shutil
res = 'android/app/src/main/res'
for d in os.listdir('android-res'):
    shutil.copytree(os.path.join('android-res', d), os.path.join(res, d), dirs_exist_ok=True)
os.makedirs(os.path.join(res, 'values'), exist_ok=True)
with open(os.path.join(res, 'values', 'ic_launcher_background.xml'), 'w') as f:
    f.write('<?xml version="1.0" encoding="utf-8"?>\n<resources>\n    <color name="ic_launcher_background">#0F1B3D</color>\n</resources>\n')
m = 'android/app/src/main/AndroidManifest.xml'
t = open(m).read()
if 'android.permission.CAMERA' not in t:
    t, n = re.subn(r'(<uses-permission android:name="android.permission.INTERNET"\s*/>)',
                   r'\1\n    <uses-permission android:name="android.permission.CAMERA" />\n    <uses-feature android:name="android.hardware.camera" android:required="false" />', t, count=1)
    if n != 1:
        raise SystemExit('INTERNET permission line not found in AndroidManifest.xml')
    open(m, 'w').write(t)
print('icons and permissions applied')
