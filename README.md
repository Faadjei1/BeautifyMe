What is this Website about?

Beautify_me is a website for a clothing shop.


How was it built?
Beautify_me runs on “flask”. In order to run this website, a user must log into the final-project folder and run “flask-run” on the generated link. As a new user, create an account and enjoy it!!!

Rubrics

The main folder called the final-project folder has 3 main folders: The flask_session folder, static folder, and templates folder. It also contains the files: app.py, DESIGN.md, final.db and helpers.py.

Flask_session: The flask_session folder contains two files that hold the extensions for flask and supports the server-side session to my application.

Static: The static folder contains a css file named final.css, and an image folder.
    Final.css: This contains all the css designs of the website.
   Images folder: the images folder contains all the images and icons used to create
       and     design this website.

 Templates folder: the templates folder contains all the html files(index.html, login, register, logout, about,, contact, items,)

    Login: the login page is the first page of the website. The login page has a register, email, password and a login button.
    The register button redirects a new user to a registration page. Using both GET, and POST, a new user can successfully create their logins and it will be stored in the final.db database file.
    
   The email, password and login button enables a returning user to login into their account.
  Index: the index html page simply displays the name of the shop with an aesthetically creative background.
      The index page has a navigation bar that displays a navigation column when clicked. The navigation menu symbol menu automatically becomes a close button which can be used for closing the navigation bar. The nav bar has the following buttons: About Us, Contact Us, Items, instagram, google maps, log out.

About Us: when clicked, About-us directs a user to the about page which is run with the about.html. The page displays information about the shop including the trading services available.

Contact us contains the contact information of the shop(the email, phone number, and location)

Items bar which runs in the items html displays the available items in stock in the shop. Customers can view the prices of the items available.

The “instagram” links a  user to the instagram page of the website.

The google maps, when clicked, displays the location of the shop on google maps.

Logout: The logout button logs the user of of the website, and redirects them to the login page.

The files in the final-project folder: The app.py folder is the backend document of the website. It contains the POST, GET, and return functions that take the data of a user, store it
in the database, and make logging in. and all the navigation possible.

DESIGN.md: This file is a word document file and contains the rubrics of the desig of the website.

Final.db is the database of the website. Customer login information is stored here.

Helpers.py contains the helper functions that were built by the website developer.
