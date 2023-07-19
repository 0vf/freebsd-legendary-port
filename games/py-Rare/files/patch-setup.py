--- setup.py.orig   2022-07-18 8:23:41 UTC
+++ setup.py
@@ -19,6 +19,7 @@ requirements = [
 optional_reqs = dict(
     webview=[
         'pywebview[gtk]; platform_system == "Linux"',
+        'pywebview[gtk]; platform_system == "FreeBSD"',
         'pywebview[cef]; platform_system == "Windows"',
     ],
     pypresence=["pypresence"]
     
