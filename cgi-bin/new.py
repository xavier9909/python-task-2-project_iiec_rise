#!/usr/bin/python3

print("content-type: text/html")


print()

import cgi
import subprocess as sp
import webbrowser as wb
#a = ["ter"]
b = ["opt"]

form = cgi.FieldStorage()
c = form.getvalue('ter')


if("Terminal" in  c):
	
	print("""
	<!DOCTYPE html>
<html >
    <meta charset="UTF-8">
    <title>BeBlack</title>
    
    
    <link rel="icon" type="/image/png" sizes="32x32" href="/img/favicon.png">
    <link rel="stylesheet" type="text/css" href="/css/normalize.min.css" media="all" />
    <link href="https://fonts.googleapis.com/css?family=Raleway&display=swap" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="/css/flexboxgrid.css" media="all" />
    <link rel="stylesheet" type="text/css" href="/css/theme.css" media="all" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
</head>
<body>
    <header class="fade-in">
        
        <div class="hero flex middle-xs" style="background-image: linear-gradient(rgba(0, 0, 0, 0.9), rgba(0, 0, 0, 0.7)), url('/img/hero-image.jpg');
    }">
    <div class="hero-text ">
        <h1>Why So Serious? </h1>
        <p>WHEN YOU HAVE WHOLE TERMINAL</p>   
        <h1>~#I'm all Yours</h1>
        <iframe style="border:3px black;" src="https://192.168.10.201:4200" height="300" width="800" ></iframe>
    </div>
</div>
</header>

 <script src="https://cdn.polyfill.io/v2/polyfill.min.js?callback=polyfillsAreLoaded" defer></script>
 <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
 <script src="/js/script.js" defer></script>
</body>
</html>""")
elif(c in b):
    print("hello")
		
