from flask import Flask, render_template 

app = Flask(__name__) 

@app.route('/') 
def welcome(): 
  return render_template('index2.html')

@app.route('/nextPage2/') 
def nextPage1(): 
  return render_template('index3.html') 


if(__name__ == "__main__"): 
  app.run(debug=True)
