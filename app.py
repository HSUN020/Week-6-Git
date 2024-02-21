#!/usr/bin/env python
# coding: utf-8

# In[3]:


from textblob import TextBlob


# In[4]:


from flask import Flask


# In[5]:


app = Flask(__name__)


# In[6]:


from flask import render_template,request


# In[7]:


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text")
        print(text)
        r1 = TextBlob(text).sentiment
        return(render_template("index.html", result1=r1))
    else:
        return(render_template("index.html", result1="2"))


# In[ ]:


if __name__=="__main__":
    app.run()
