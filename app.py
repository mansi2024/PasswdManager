from loginapp import app, db

@app.before_first_request
def create_tables():
    db.create_all()
if __name__ == '__main__':
    db.create_all() # first we need to create table other wise HUGE ERROR. Wasted-24hr :(
    app.run(debug=True, port=5000)
