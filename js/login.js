// LOGIN.js
function click() {
    inputname = $("name").val();
    inputpassword =$("pass").val();

    for (i in data.username )      //to match username with provided array
    { 
        name = data.username[i];

        for ( i in data.password){
            pass = data.password[i];

            if (inputname == name & inputpassword == pass ){
                //The user has successfully authenticated. We need to store this information
                //for the next page.
                sessionStorage.setItem("AuthenticationState", "Authenticated");
                
                //This authentication key will expire in 1 hour.
                sessionStorage.setItem("AuthenticationExpires", Date.now.addHours(1));
                
                //Push the user over to the next page.
                window.open('/main.html','_self');
            }               
        }
    }

    if (inputname != name & inputpassword != pass ){
        alert("Wrong Password");
    }
}

//addHours to a date.
//Credit to: Kennebec
//https://stackoverflow.com/questions/1050720/adding-hours-to-javascript-date-object
Date.prototype.addHours = function(h) {    
   this.setTime(this.getTime() + (h*60*60*1000)); 
   return this;   
}
//Is the user authenticated?
if (sessionStorage.getItem('AuthenticationState') === null) {
   window.open("1..html", "_self");
}
//Is their authentication token still valid?
else if (Date.now > new Date(sessionStorage.getItem('AuthenticationExpires'))) {
      window.open("1.html", "_self");
}
else {
  //The user is authenticated and the authentication has not expired.
}