from flask import Flask, flash, redirect, render_template, request
from modules.databases import city_links_base, weather_base
from modules.grabber.counter import counter


app = Flask(__name__, template_folder="modules/webtemplates")
app.config.from_object("config")

# be run ok if in db file we have "check_same_thread=False", else - conflict threads


@app.route("/", methods=["GET", "POST"])
def pusher():

    return render_template(
        "firstpage.html",
        title="Sign In",
    )


# the module who must print results from database
@app.route("/result", methods=["GET", "POST"])
def count():

    prod_db = weather_base.databaser_cl()
    if request.method == "POST":
        region_selected = int(request.form.get("selectcity"))
        parcer = counter()

        parced_result = parcer.count(
            city_links_base.regions[region_selected]["yandex"],
            city_links_base.regions[region_selected]["gismeteo"],
            city_links_base.regions[region_selected]["gidromet"],
        )


        prod_db.post_to_table(str(parced_result), region_selected)

    given = prod_db.read_from_table()

    return str(given)


if __name__ == "__main__":
    app.run(debug=True)  # add debug mode
