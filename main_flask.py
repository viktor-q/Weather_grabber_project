from flask import Flask, request
from modules.grabber import grabber_gecko
#from modules import forms
from modules.webtemplates import first_forms
from flask import render_template, flash, redirect
#from modules import base
from modules.databases import weather_base


#from weather_base import Databaser_cl
#import datetime

app = Flask(__name__, template_folder="modules/webtemplates")
app.config.from_object('config')

fiction = weather_base.Databaser_cl()

# be run ok if in db file we have "check_same_thread=False", else - conflict threads

@app.route('/', methods=['GET', 'POST'])
def pusher():
    form = first_forms.Dataform()

    if form.validate_on_submit():
        first_typed_field = int(form.numberone.data)
        second_typed_field = int(form.numbertwo.data)


        print(maker.maker_foo(first_typed_field, second_typed_field))

#        fiction = Databaser_cl() maked upper
        res = fiction.post_to_table(first_typed_field, second_typed_field)
        print(res)

#place for add data to table?


    return render_template('firstpage.html',
                           title='Sign In',
                           form = form)



#the module who must print results from database
@app.route('/result', methods=['GET', 'POST'])
def count():
#    fiction = Databaser_cl() maked upper
##    resultate = fiction.read_from_table()
##    return str(resultate)
    if request.method == 'POST':
        region = request.form.get('selectcity')
        otchet = grabber_gecko.rounds
    return str([otchet, region])


    #return Databaser_cl.read_from_table()



if __name__ == "__main__":
    app.run(debug=True)  # add debug mode
