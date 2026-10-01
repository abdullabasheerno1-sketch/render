from flask import Flask, redirect, request

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
        
    return redirect(target_url, code=302)

if __name__ == '__main__':
    app.run()
