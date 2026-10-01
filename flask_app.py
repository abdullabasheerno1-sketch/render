from flask import Flask, Response, request
import urllib.request

app = Flask(__name__)

USERNAME = 'MAGNL39E26'
PASSWORD = 'hvhS6xsuZP'
SERVER_URL = 'http://raztv.online:80/'

@app.route('/')
def proxy():
    stream_id = request.args.get('stream_id')
    
    if stream_id:
        target_url = f"{SERVER_URL}/live/{USERNAME}/{PASSWORD}/{stream_id}.m3u8"
    else:
        target_url = f"{SERVER_URL}/get.php?username={USERNAME}&password={PASSWORD}&type=m3u_plus"
        
    try:
        req = urllib.request.Request(
            target_url, 
            headers={'User-Agent': 'VLC/3.0.18 LibVLC/3.0.18'}
        )
        with urllib.request.urlopen(req) as resp:
            content = resp.read()
            headers = dict(resp.headers.items())
            return Response(content, status=resp.status, headers=headers)
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == '__main__':
    app.run()
