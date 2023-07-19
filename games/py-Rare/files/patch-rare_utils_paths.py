--- rare/utils/paths.py.orig    2022-07-18 6:43:23 UTC
+++ rare/utils/paths.py
@@ -80,6 +80,10 @@ __link_suffix = {
         "link": "lnk",
         "icon": "ico",
     },
+    "FreeBSD": {
+        "link": "desktop",
+        "icon": "png",
+    },
     "Linux": {
         "link": "desktop",
         "icon": "png",
@@ -128,7 +132,7 @@ def get_rare_executable() -> List[str]:
     # lk: detect if nuitka
     if "__compiled__" in globals():
         executable = [sys.executable]
-    elif platform.system() == "Linux" or platform.system() == "Darwin":
+    elif platform.system() == "Linux" or platform.system() == "Darwin" or platform.system() == "FreeBSD":
         if p := os.environ.get("APPIMAGE"):
             executable = [p]
         else:
@@ -199,7 +203,7 @@ def create_desktop_link(app_name: str, app_title: str = "", link_name: str = "",
     else:
         logger.info(f"Creating shortcut for {app_title} at {shortcut_path}")
 
-    if platform.system() == "Linux":
+    if platform.system() == "Linux" or platform.system() == "FreeBSD":
         executable = get_rare_executable()
         executable = shlex.join(executable)
         if not for_rare:
