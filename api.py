from flask import Flask, request, jsonify, send_file
import csv
import os

#needs to run on a differnt port than the main app

app = Flask(__name__)
            /*  REST CODE HIDDEN FOR SECURITY !!! */

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
