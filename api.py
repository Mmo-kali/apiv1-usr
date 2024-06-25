from flask import Flask, request, jsonify, send_file
import csv
import os

#needs to run on a differnt port than the main app

app = Flask(__name__)

@app.route('/apiV1-usr', methods=['GET', 'POST'])
def read_csv():
    directory_path = r'API-Challenge\apiDirectory'  # Update this path

    if request.method == 'GET':
        debug_pin = request.args.get('debugPin')
        file_name = request.args.get('fileName')

        if not debug_pin:
            if not file_name:
                return jsonify({"error": " 'debugPin' or 'fileName' parameter missing"}), 400
            else:
                files = os.listdir(directory_path)
                if file_name in files:
                    file_path = os.path.join(directory_path, file_name)
                    return send_file(file_path, as_attachment=True)
                else:
                    return jsonify({"error": "File not found"}), 404
                
        elif debug_pin == '123-456-789' or debug_pin == 123-456-789:
            files = os.listdir(directory_path)
            file_name = request.args.get('fileName')        
            
    
            if file_name == '*':
                return jsonify(files)
            elif file_name and file_name in files:
                file_path = os.path.join(directory_path, file_name)
                return send_file(file_path, as_attachment=True)
            else:
                return jsonify({"error": "File not found or fileName parameter missing"}), 404
            
        elif debug_pin != '123-456-789' or debug_pin != 123-456-789:
            return jsonify({"error": "Invalid request"}), 403

        else:
            return jsonify({"error": "Invalid request look at  GITHUB FOR DOCUMENTATION "}), 403
        

        
        
    elif request.method == 'POST':
        data = request.json
        region_id = data.get('RegionID')
        file_name = 'userRegion.csv'  # Specify your CSV file name
        file_path = os.path.join(directory_path, file_name)
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] == region_id:
                    # Assuming the entire row is needed. Adjust as necessary.
                    return jsonify(row)
        return jsonify({"error": "Region ID not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=8000) # specify the port number here
