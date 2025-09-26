[app]

# ⚡ Change this to your app name
title = Mentor Nook

# ⚡ Package name (used in APK name)
package.name = mnwebapp

# ⚡ Reverse-domain style package (must be unique if uploading to Google Play)
package.domain = org.mnwebapp

# Your app version (change this when updating)
version = 0.1

# Android versioning
android.version_code = 1
android.version_name = 0.1

# Use system-installed SDK/NDK# Force SDK and NDK paths
android.sdk_path = /home/runner/android-sdk
android.ndk_path = /home/runner/android-sdk/ndk


# The main script (dummy launcher, since we use webview)
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,html,css,js

# Requirements
requirements = python3,kivy,kivy_garden.xcamera,plyer

# Orientation (landscape, portrait or all)
orientation = portrait

# App icon (⚡ replace with your icon file)
icon.filename = %(source.dir)s/data/icon.png

# Starting screen (splash)
presplash.filename = %(source.dir)s/data/splash.png

# Package format
android.release_artifact = apk

# Permissions
android.permissions = INTERNET

# (Optional) allow WebView debug
android.debug = True


[buildozer]
log_level = 2
warn_on_root = 1
