[app]
title = Eco Scanner
package.name = ecoscanner
package.domain = org.vincent
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0
android.permissions = CAMERA
android.api = 33
android.minapi = 21
android.ndk = 25b

[buildozer]
log_level = 2
warn_on_root = 0