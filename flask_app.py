from flask import Flask, Response, request
import requests

app = Flask(__name__)

USERNAME = 'MAGNL39E26'
PASSWORD = 'hvhS6xsuZP'
SERVER_URL = 'http://raztv.online'

@app.route('/')
def proxy():
    stream_id = request.args.get('stream_id')
    
    if stream_id:
        target_url = f"{SERVER_URL}/live/{USERNAME}/{PASSWORD}/{stream_id}.m3u8"
    else:
        target_url = f"{SERVER_URL}/get.php?username={USERNAME}&password={PASSWORD}&type=m3u_plus"
        
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    
    try:
        resp = requests.get(target_url, headers=headers, stream=True)
        return Response(resp.raw.read(), status=resp.status_code, headers=dict(resp.headers))
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == '__main__':
    app.run()
