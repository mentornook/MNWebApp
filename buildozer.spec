[app]
title = MN WebApp
package.name = mnwebapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Icon (replace icon.png with your logo)
icon.filename = %(source.dir)s/icon.png

# Requirements
requirements = python3,kivy,kivy_garden.webview
orientation = portrait

# Permissions for WebView
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# Target Android API (Google Play requires at least 33 now)
android.api = 34
android.minapi = 21

# Build release format
android.release_artifact = aab

[buildozer]
log_level = 2
warn_on_root = 1
