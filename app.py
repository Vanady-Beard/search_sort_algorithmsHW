from flask import Flask, request, jsonify
from binary import bubble_sort, binary_search, video_titles




app = Flask(__name__)

# http://127.0.0.1:5000/search?video_title=Digital Photography Essentials

bubble_sort(video_titles)

@app.route('/search', methods=['GET'])

def search ():
    query = request.args.get('video_title')
    if not query:
        return jsonify({"error": "Missing 'video_title'"}), 400
   
    index = binary_search(video_titles, query)

    if index is not None:
        return jsonify({"title": video_titles[index]}), 200
    else:
        return jsonify({"error": "Title not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)


