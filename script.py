

import requests
import json
from flask import Flask,render_template,request

app= Flask(__name__)

def scrapperfunc(namesearch):
    response = requests.get("https://api.github.com/users/"+namesearch)
    c=response.json()

    #htmlurl
    htmlurl = c['html_url']
    #avatarurl
    avatarurl=c['avatar_url']
    #numberofrepos
    reponumber=c['public_repos']
    #repolist
    response1= requests.get(c['repos_url'])
    c1 = response1.json()
    repolist=list()
    stars= list()
    description=list()
    for c11 in c1:
        for key,val in c11.items():
            if(key=='name'):
                repolist.append(val)
            if(key=='stargazers_count'):
                stars.append(val)
            if(key=='description'):
                description.append(val)
    #followers
    num_followers = c['followers']
    #following
    num_following = c['following']
    #location
    location = c['location']
    #bio
    bio = c['bio']
    #email
    email = c['email']
    #username
    username = c['name']
    return {
            'htmlurl':htmlurl,
            'avatarurl':avatarurl,
            'reponumber':reponumber,
            'repolist':repolist,
            'stars':stars,
            'description':description,
            'num_followers':num_followers,
            'num_following':num_following,
            'location':location,
            'bio':bio,
            'email':email,
            'username':username
    }

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/results', methods=['POST','GET'])
def results():
    mssg ="HELLO SUCCESS!"
    namesearch = request.form['namesearch']
    namesearch1 = request.form['namesearch1']
    data = scrapperfunc(namesearch)
    data1 = scrapperfunc(namesearch1)
    return render_template("results.html",mssg=mssg,htmlurl=data['htmlurl'],avatarurl=data['avatarurl'],reponumber=data['reponumber'] , \
    repolist= data['repolist'], stars= data['stars'], follower = data['num_followers'],following=data['num_following'], location = data['location'], bio = data['bio'], email=data['email'],\
    description=data['description'],htmlurl1=data1['htmlurl'],avatarurl1=data1['avatarurl'],reponumber1=data1['reponumber'] , \
    repolist1= data1['repolist'], stars1= data1['stars'], follower1 = data1['num_followers'],following1=data1['num_following'], location1 = data1['location'], bio1 = data1['bio'], email1=data1['email'],\
    description1=data1['description'],username=data['username'],username1=data1['username'],zipped=zip(data['repolist'],data['stars'],data['description']),zipped1=zip(data1['repolist'],data1['stars'],data1['description']))


if __name__=="__main__":
    app.run(debug=True)
