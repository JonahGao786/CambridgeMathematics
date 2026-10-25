#!/usr/bin/env python3
"""Drive access with a service-account key (stdlib + openssl only).

  drive_sa.py KEY.json list FOLDER_ID            # recursive: id, modifiedTime, size, path
  drive_sa.py KEY.json get FILE_ID OUT_PATH      # download binary content

The key file is a credential: keep it outside the repository, never print or commit it.
The Drive folder must be shared with the key's client_email (Viewer is enough).
"""
import base64, json, subprocess, sys, time, urllib.parse, urllib.request

API = "https://www.googleapis.com/drive/v3/files"
SCOPE = "https://www.googleapis.com/auth/drive.readonly"

def b64(b): return base64.urlsafe_b64encode(b).rstrip(b"=")

def token(key):
    now = int(time.time())
    head = b64(json.dumps({"alg": "RS256", "typ": "JWT"}).encode())
    claim = b64(json.dumps({"iss": key["client_email"], "scope": SCOPE, "aud": key["token_uri"],
                            "iat": now, "exp": now + 3000}).encode())
    msg = head + b"." + claim
    fd = _keyfd(key["private_key"])
    p = subprocess.run(["openssl", "dgst", "-sha256", "-sign", f"/dev/fd/{fd}"], input=msg, capture_output=True,
                       check=True, pass_fds=(fd,))
    jwt = (msg + b"." + b64(p.stdout)).decode()
    data = urllib.parse.urlencode({"grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer", "assertion": jwt}).encode()
    return json.load(urllib.request.urlopen(urllib.request.Request(key["token_uri"], data)))["access_token"]

def _keyfd(pem):
    # feed the PEM to openssl through a pipe, never through a file or argv
    import os
    r, w = os.pipe()
    os.write(w, pem.encode()); os.close(w)
    os.set_inheritable(r, True)
    return r

def call(url, tok):
    return urllib.request.urlopen(urllib.request.Request(url, headers={"Authorization": "Bearer " + tok}))

def walk(tok, folder, prefix=""):
    page = None
    while True:
        q = urllib.parse.urlencode({"q": f"'{folder}' in parents and trashed=false", "pageSize": 200,
              "fields": "nextPageToken,files(id,name,mimeType,modifiedTime,size)", **({"pageToken": page} if page else {})})
        d = json.load(call(f"{API}?{q}", tok))
        for f in d.get("files", []):
            path = prefix + f["name"]
            if f["mimeType"] == "application/vnd.google-apps.folder":
                yield from walk(tok, f["id"], path + "/")
            else:
                yield f["id"], f["modifiedTime"], f.get("size", "-"), path
        page = d.get("nextPageToken")
        if not page: break

if __name__ == "__main__":
    key = json.load(open(sys.argv[1])); tok = token(key); cmd = sys.argv[2]
    if cmd == "list":
        for row in walk(tok, sys.argv[3]): print(*row, sep="\t")
    elif cmd == "get":
        with call(f"{API}/{sys.argv[3]}?alt=media", tok) as r, open(sys.argv[4], "wb") as o:
            while chunk := r.read(1 << 20): o.write(chunk)
