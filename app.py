from flask import Flask, render_template, url_for

articles = {
	"title": "post",
	"author": "x",
	"date": "xx/xx/xxxx",
	"content": "x"
}

presentations = {
	"Daniel":   """
					Highly-motivated & ambitious SWUFE MIB senior year
				    student with considerable 2 years track record &
				    experience in business development & marketing incl. 
				    successful creation & execution of creative digital 
				    media project for the Government of Queensland, 
				    effective coordination & implementation of e-commerce 
				    marketing strategy - paired with strong organizational 
				    & functional skills. Recognized appointed TA of SWUFE 
				    prof. Xu Yongan & laureate of Chinese Government 
				    Scholarship for SWUFE MIB Programme & HNU Chinese 
				    Language and Culture Programme, SWUFE International 
				    Students Performance Scholarship. Enterprising, 
				    knowledgeable & ingenious Visionary, bring change and 
				    innovation via creative performance & solutions.
			    """,
	"Bastien":  """  From Lyon, France, Bastien landed in Chendgu in 
				    2014. Student, entrepreneur, civil servant, he's
				    now heading to work in the tech world after he
				    dove into programming.
				"""
}

pages = ["Homepage", "About"]
names = ["Daniel Biskupski", "Bastien Ratat"]

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", articles=articles, pages=pages)

@app.route('/about')
def about():
    return render_template("about.html", pages=pages, names=names, presentations=presentations)

if __name__ == '__main__':
	app.run(debug=True)
    
