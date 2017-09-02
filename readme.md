<h1>ClarityUI - Python Flask Example</h1>

This is a simple example of creating a Python Flask WebApp using Clarity UI 

There are a couple features in this page
* Simple login functionality using the Clarity login control 
* API connectivity to a rest API endpoint that lists out virtual machines 
* API Connectivity to a vRO endpoint that lists out all vRO workflows with their Item HREF
* Jinja templating used extensively
* Session details carried between pages 

Angular functionality is missing from the ClarityUI so it's purely the CSS/JS components. 

<h2>Flask Overview</h2>
Flask is essentially a web platform for hosting page leveraging Python. It follows a traditional web application model for how it functions. Jinja templating is used to embed pages wtihin pages. You can see this example in how we include the header.html file in all other pages using the {% includes 'header.html' %} syntax. 

<h2>Component Examples</h2>

<h3>header.html</h3>
Includes jinja templating references to carry this page int oothers 

<h3>index.html</h3>
Simple login form using Clarity UI. Uses the flask sessions module to tag sessions as "logged_in" = True to allow you to restrict certain pages if you wish

<h3>vms.html</h3>
We feed in a variable thats defined in our app.py and the iterate over it, using the table compononent from clarity to render the page. It's good and good for you. We do a simple for i in vms to iterate over it, and then drop a row component for each. 

<h3>workflows.html</h3>
We do a similar thing to what we did in vms.html but we iterate deeper into the array in this example 

Enjoy! 