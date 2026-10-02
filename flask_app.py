from flask import Flask, Response, request
import requests

app = Flask(__name__)

USERNAME = 'MAGNL39E26'
PASSWORD = 'hvhS6xsuZP'
# ഇവിടെ raztv.online-ന് ശേഷം രണ്ട് സ്ലാഷ് (//) നൽകിയിരിക്കുന്നു
SERVER_URL = 'http://raztv.online//'

@app.route('/')
def proxy():
    stream_id = request.args.get('stream_id')
    
    # URL ജോയിൻ ചെയ്യുമ്പോൾ ഡബിൾ സ്ലാഷ് വരുന്നത് ഒഴിവാക്കാൻ strip ഉപയോഗിക്കുന്നു
    base = SERVER_URL.rstrip('/')
    
    if stream_id:
        target_url = f"{base}/live/{USERNAME}/{PASSWORD}/{stream_id}.m3u8"
    else:
        target_url = f"{base}/get.php?username={USERNAME}&password={PASSWORD}&type=m3u_plus"
        
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36',
        'Accept': '*/*'
    }
    
    try:
        resp = requests.get(target_url, headers=headers, stream=True)
        return Response(resp.raw.read(), status=resp.status_code, headers=dict(resp.headers))
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == '__main__':
    app.run()
