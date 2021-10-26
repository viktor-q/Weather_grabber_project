from flask import Flask, request
#from modules.grabber import grabber_gecko
from modules.databases import city_links_base
from modules.grabber.grabber_gecko import grabber_ge
from flask import render_template, flash, redirect


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
        region = request.form.get('selectcity')
        parcer = grabber_ge()
        if region == '78':
            fff = city_links_base.yandex_78
        if region == '40':
            fff = city_links_base.yandex_40


        otchet = parcer.yandex_weather(fff)
    return str([otchet, region])


if __name__ == "__main__":
    app.run(debug=True)  # add debug mode
