#!/usr/bin/python3

print("content-type: text/html")


print()

import cgi
a = ["1111"]
b = ["1111"]
c=["ter"]

form = cgi.FieldStorage()
user = form.getvalue('username')
passwd = form.getvalue('password')
pac = form.getvalue('ter')
if(user in a):
	if(passwd in b):
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
     <div class="hero-text"  >
    <div>
    <form  method="post" action="http://192.168.10.201/cgi-bin/new.py">

          <h1 class=" text-center text-capitalize pt-5" style="float: left; width: 50%; padding: 10px; margin:text-align:center; width: 620px;
   padding: 40px;  margin-bottom:65px;color:black ">  <input name="ter" type='submit' value='Terminal' class="submit" align="center"> </h1> 
     </form>
     </div>

     
     <div>
     <form  method="post" action="http://192.168.10.201/be.html"> 
    <h1 class=" text-center text-capitalize pt-5" style=" float: left; width: 50%; padding: 10px;float: left;text-align:center; width: 620px;
   padding: 40px;  margin-bottom:65px;color:black "> <input  type='submit' value="User Interface"  class="submit" align="center"> </h1>
       </form>
      </div>  
       
    </div>
      
</header>

 <script src="https://cdn.polyfill.io/v2/polyfill.min.js?callback=polyfillsAreLoaded" defer></script>
 <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
 <script src="/js/script.js" defer></script>
</body>
</html>""")
		
	else:

		print("""<style>
                h1{text-align: center;}
                p{text-align: center;}</style>
                <body>
                <h1>!!!!!GO BACK SIMON GO BACK!!!!!</h1> <br/> <p>PASSWD ERROR</p>
                </body""")
else:

    print("""<style>
                h1{text-align: center;}
                p{text-align: center;}</style>
                <body>
                <h1>!!!!!GO BACK SIMON GO BACK!!!!!</h1> <br/> <p>USERNAME ERROR</p>
                </body""")
