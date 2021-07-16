
#Author          : Deric San ANdres
#Course and Year : 2-BSIT
#Filename        : base.html
#Description     : This is the parent template for child templates home, about and connect
#Honor Code      : I have not given nor received any unathorized help in
#                  completing this exercise. I am also well aware of the 
#                 policies stipulated in the AdNU student handbook


from flask import Flask, render_template
from flask_restful import request, abort, Api, Resource

app = Flask(__name__)
api = Api (app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/manage')
def manage():
    return render_template('manage.html')


@app.route('/api/<int:get_id>', methods=['GET'])
def get_menu(get_id):
    for key in MUSIC:
        if key == get_id:
            response = MUSIC[key]
            return response
        abort (404)

#@app.route('/manage')
#def manage():
#   return render_template('manage.html')

MUSIC = {
    1 : {"id": 1, "title" : "Butter",  "released" : 2021, "genre" : "Pop" },  
    2 : {"id": 2, "title" : "Good 4 U",  "released" : 2021, "genre" : "Pop" },
    3 : {"id": 3, "title" : "Levitating", "released" : 2021, "genre" : "Pop" },
    4 : {"id": 4, "title" : "Kiss Me More",  "released" : 2021, "genre" : "Pop" },
}
class MusicList(Resource):
    def get (self):
        song_list = [ song_data for id, song_data in MUSIC.items()]
        response_data = { "data" : song_list }
        return response_data

    def post (self):
        request_data = request.get_json(force = True)

        new_song_id = int(max(MUSIC.keys())) + 1;
        new_song = {
            "id" : new_song_id,
            "title" : request_data["title"],
            "released" : request_data["released"],
            "genre" : request_data["genre"],
        }
        MUSIC[new_music_id] = new_song
        return new_song, 201

api.add_resource(MusicList, "/api/music")

if __name__ == '__main__':
    app.run(debug=True)
