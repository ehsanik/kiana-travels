from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/climb_stats.html')
def climb_stats():
    return render_template('climb_stats.html')

@app.route('/trips.html')
def trips():
    return render_template('trips.html')

@app.route('/20200609-montana_trip.html')
def montana_trip():
    return render_template('20200609_montana_trip.html')

@app.route('/20210725_mount_rainier_via_dc.html')
def mount_rainier_via_dc():
    return render_template('20210725_mount_rainier_via_dc.html')

@app.route('/20210501_mount_angeles_ski_touring.html')
def mount_angeles_ski_touring():
    return render_template('20210501_mount_angeles_ski_touring.html')

@app.route('/20210514_hojjat_and_friends_in_town.html')
def hojjat_and_friends_in_town():
    return render_template('20210514_hojjat_and_friends_in_town.html')

@app.route('/20210522_vahalla_peak_and_5050_pass.html')
def vahalla_peak_and_5050_pass():
    return render_template('20210522_vahalla_peak_and_5050_pass.html')

@app.route('/20210527_memorial_weekend_with_marzi.html')
def memorial_weekend_with_marzi():
    return render_template('20210527_memorial_weekend_with_marzi.html')

@app.route('/20210731_eldorado_peak.html')
def eldorado_peak():
    return render_template('20210731_eldorado_peak.html')

@app.route('/20211201_peru.html')
def peru():
    return render_template('20211201_peru.html')

@app.route('/central_asia.html')
def central_asia():
    return render_template('central_asia.html')

@app.route('/europe_the_alps_and_mont_blanc.html')
def europe_the_alps_and_mont_blanc():
    return render_template('europe_the_alps_and_mont_blanc.html')

@app.route('/mexico_city.html')
def mexico_city():
    return render_template('mexico_city.html')

@app.route('/japan_may_2024.html')
def japan_may_2024():
    return render_template('japan_may_2024.html')

if __name__ == '__main__':
    app.run(debug=True)
