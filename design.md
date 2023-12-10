# Design Understanding

## `scuba/`

### `admin.py`

File that configures the admin page for the site.

### `apps.py`

File to register the app in the django program.

### `forms.py`

This file contains the forms that are are needed by the app. The three forms that are written in the file correspond to the three models. The forms contain all the user input that I would like to store in the database besides user credentials.

### `models.py`

Models has all the models that are stored in the database. 
- The User is the default that we have been using throughout the term. 
- Dive collects all the need info for each dive. Each dive is linked to one user. 
- Destination collects all the need info for each destination. Each destination is linked to one user.
- DiverProfile is a one to one field as each user will only have one profile with SAC states.

_Design notes: I would like to link both dives and destinations so that each time you put a dive in it would prompt you for a destination to be attached to that dive. You could also get to the detailed destination page form the detailed dive page. I was also using the DiverProfile for a dive planning tool that I couldn't get to work and in the end had to scrap. I would like to implement it in the future, but for right now it is just a place to track that info for the user._

### `tests.py`

No testing is implemented. This was something that I wrote down on my personal, but I was not able to write any.

### `urls.py`

All the URLs for the app. 

_Notes: Here again, I would like to implement more pages for the app including a separate dive tools page if I could get more dive planning logic to work._

### `views.py`

All the views needed for the app.

- index has the information for the main page of the app. This displays all of the dives that the user has entered by filtering all dives by request user. It also has a POST action for adding new dives to the database. 

- login_view lets the user log in to the app. _Note: I did not write the login. I took this from the Network project that we worked on earlier in the term. The CS33a staff wrote this code._

- logout_view lets the user logout of the app. _Note: I did not write the logout. I took this from the Network project that we worked on earlier in the term. The CS33a staff wrote this code._

- register lets the someone register as a user for the app. _Note: I did not write the register. I took this from the Network project that we worked on earlier in the term. The CS33a staff wrote this code._

- dive_detail pulls an individual dive that the user can see in dive_detail.html.

- destination_list displays all of the destinations that the user has entered by filtering all destinations by request user. It also has a POST action for adding new destinations to the database.

- destination_detail pulls an individual destination that the user can see in destination_detail.html.

- diver_profile displays all the SAC information that the user has inputted for themselves. It also has a form that will update their SAC information. 

- dive_planner just returns the dive_planner.html. The page only has js functionally so nothing is being called or pushed to the DB. _Note: In the future this is where I would put some gas planning information by using the backgas and deco gas that the user inputs. I could not figure out how to target input that the user put in a dynamic table that the js created._

### `static/`

#### `scuba/`

##### `dive.js`

`dive.js` has a lot going on. In the file there seems to be a some redundant use of a DOMContentLoaded event listener. This is because I would put them all under the same one, but it would disable some of the code for one part of the js. For example the first two functions I have. When they are both under the same DOMContentLoaded event, only the first one would work. I found this over and over when I was writing this file. In the end to make sure things are working properly, I separated them out when they did not work together. 

- The first chunk is too toggle the new dive form when the button is clicked.

- The next one is the same function, but for the new destination form.

- Then we have a form that takes user input and updates the diver profile and displays the new information entered when save profile is clicked.

- The rest of the `dive.js` page is devoted to the dive planner page for the app. I wanted to make the page as easy to read as possible and I thought that it would help if you only have the information that you need on the screen at one time. This is why the deco gas/gasses are not displayed unless you are going to use them. All of this information could also be used for more in-depth gas planning in the future with this app. A lot of the math was difficult to understand how the numbers were being handled and how to make the app use them properly. I don't know how many times I ran into NaN when trying to implement all of this.

##### `styles.css`

`styles.css` has all the style for this app. I made is so the app should be visible on any container and have some padding.

### `templates/`

#### `scuba/`

##### `destination_detail.html`

Displays the detailed page for the selected destination.

##### `destination_list.html`

Displays the list of all the destinations the user has entered. The list is created from the most recent entry to the oldest entry. Each destination is clickable to go to it's detail page. This page also has the form the user could fill out to add a new destination. 

##### `dive_detail.html`

Displays the detailed page for the selected dive.

##### `dive_planner.html`

This page has all the dive planning tools the app offers. 

##### `diver_profile.html`

Displays the user's SAC data the user has entered. This page also has the form the user could use to change their SAC data.

##### `index.html`

Displays the list of all the dives the user has entered. The list is created from the most recent entry to the oldest entry. Each dive is clickable to go to it's detail page. This page also has the form the user could fill out to add a new dive. 

##### `layout.html`

This page is the base that all the other pages use. It has the HTML head data that is being used by the other HTML pages.
_Note: I did not write most of `layout.html`. I took this from the Network project that we worked on earlier in the term. The CS33a staff wrote the majority of the code. I did change some of the links and wording to work with my app._

##### `login.html`

`login.html` lets the user log in to the app. _Note: I did not write this page. I took this from the Network project that we worked on earlier in the term. The CS33a staff wrote this code._

##### `register.html`

`register.html` lets the someone register as a user for the app. _Note: I did not write this page. I took this from the Network project that we worked on earlier in the term. The CS33a staff wrote this code._
