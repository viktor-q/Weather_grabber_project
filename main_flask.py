from flask import Flask, request
#from modules.grabber import grabber_gecko
from modules.databases import city_links_base
from modules.grabber.grabber_gecko import grabber_ge
from modules.grabber.counter import counter
from flask import render_template, flash, redirect
from modules.databases import weather_base


app = Flask(__name__, template_folder="modules/webtemplates")
app.config.from_object('config')

# be run ok if in db file we have "check_same_thread=False", else - conflict threads

@app.route('/', methods=['GET', 'POST'])
def pusher():

    return render_template('firstpage.html',
                           title='Sign In',
                           )


#the module who must print results from database
@app.route('/result', methods=['GET', 'POST'])
def count():

    if request.method == 'POST':
        region_selected = int(request.form.get('selectcity'))
        parcer = counter()

        parced_result = parcer.count(city_links_base.regions[region_selected]['yandex'],
                   city_links_base.regions[region_selected]['gismeteo'],
                   city_links_base.regions[region_selected]['gidromet'])

        prod_db = weather_base.databaser_cl()
        prod_db.post_to_table(str(parced_result), region_selected)

    given = prod_db.read_from_table()

    return str(given)

#print(str(fiction.read_from_table()))



if __name__ == "__main__":
    app.run(debug=True)  # add debug mode
