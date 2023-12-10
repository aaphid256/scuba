# SCUBA Log
> This SCUBA Log project for cs33a is a Django website that allows users to keep track of SCUBA related activity and use some tools for dive planning. Users are able to log into the website and log individual dives as well as their travel experience. With the dive tools, users can calculate MOD, Best Mix, and tank gas levels in cubic feet. This final project was an opportunity to develop my own software using the skills I learned in cs33a.
[Video Introduction](https://youtu.be/w1aJbZv79zE)


## Requirements  (Prerequisites)
Tools and packages required to successfully install this project.
* Visual Studio Code (VSCode): [Install] (https://code.visualstudio.com/download)
* Python 3.3 and up [Install](https://www.python.org/downloads/) - Make sure to check the option to add Python to your system's PATH during installation.

## VSCode Extensions:
* [Python Extension for VSCode] - Install the "Python" extension by Microsoft from the VSCode Extensions marketplace. This extension provides Python language support and debugging capabilities.
* [HTML/CSS Support] - If you're working with HTML, you may want to install an extension like "HTML CSS Support" for better HTML and CSS language support.


## Installation
Next download the final_project.zip file from the [Gradescope page](https://www.gradescope.com/courses/564771) and add it to your codespace in VSCode.

Then execute

`unzip final_project.zip`

to create a folder called `final_project`. You no longer need the ZIP file, so you can execute

`rm final_project.zip`

and respond with "y" followed by Enter at the prompt to remove the ZIP file you downloaded.

Now type

`cd final_project`

followed by Enter to move yourself into (i.e., open) that directory. Your prompt should now resemble the below.

`final_project/ $`

If you run into any trouble, follow these same steps again and see if you can determine where you went wrong!

## Running

Start Django's built-in web server (within `final_project/`):

`$ python3 manage.py runserver`

Visit the URL outputted by `django` to see the distribution code in action and use the website!

## Screenshots
Screenshots of the website that show the dive log, dive detail, destination log, destination detail, and dive planner.

![Dive Log](https://drive.google.com/file/d/1CPTVby-xo-RaEuaeb6DQ48zDredT6K3b/view?usp=sharing)


![Dive Detail](https://drive.google.com/file/d/1rQdc3v5DcJ8aQLCngNV4uqn_dEgRwLoC/view?usp=sharing)


![Destination Log](https://drive.google.com/file/d/1qmpO8UaHg_V8p-LG6qPlynecoYApIA5z/view?usp=sharing)


![Destinations Detail](https://drive.google.com/file/d/1DaOAUgVF4dxMKbeMbPzpso7nIQUTox7Y/view?usp=sharing)


![Dive Planner](https://drive.google.com/file/d/1PNTXZdU-zyrsQ8WwV6kVgOyXbvaNWbkS/view?usp=sharing)

## Usage example
### Dive Log
#### Log a New Dive

1. Navigate to the "My Dives" section.
2. Click on "Add New Dive".
3. Fill in the dive details.
4. Click "Add Dive" to submit the entry.

#### View Dives Details

1. Visit the "My Dives" page to see a table of your dive logs.
2. Explore various dive details by clicking on the location of each dive.

### Destination Log

#### Record Destinations

1. Visit the "My Destinations" section.
2. Click "Add New Destination".
3. Enter the destination details.
4. Click "Add Destination" to include the travel entry.

#### Explore Travel History

1. Go to the "My Destinations" page to see a record of your travel destinations.
2. Click on a location to see the details page for that destination.

### Dive Planner

1. Click on "Dive Planner" to explore tools.

#### Gas Volume

1. To find the gas volume of your backgas, fill out the inputs under backgas
2. to find the gas volume for your deco gasses, choose how many you have
3. Enter info for your deco gas(ses).

#### Calculate MOD

1. Enter the O2% of your tanks.
2. This will output the Max Operating Depth for the gas.

#### Calculate Best Mix

1. Enter the depth in feet of your planned dive.
2. This will output the best EAN to use for your dive.

## Tech Stack / Built With
(See `design.md` for an exhaustive explanation over each file)

1. [Python 3](https://www.python.org/download/releases/3.0/) - One of the programming languages used.

2. [HTML](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics) - The markup language used to display info in the web browser.

3. [Visual Studio Code](https://code.visualstudio.com/) - The source-code editor that was used.

4. [Django](https://www.djangoproject.com/) - A high-level Python web framework that encourages rapid development and clean, pragmatic design.

5. [JavaScript](https://www.javascript.com/) - A programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS.


## Authors
Tony Warfield - tony.warfield86@gmail.com

I'm a student at Harvard Extension School concentrating in Computer Science. I'm planning on graduating Summer of 2025.

You can find me here:
[Github](https://github.com/aaphid256) and
[LinkedIn](https://www.linkedin.com/in/tonywarfieldta/)

## Credits
The [Final Project](https://cs50.harvard.edu/extension/web/2023/fall/projects/final/) from CS33a class is what this project was created for. This link has all the expectations for the project.

Here's a list of other related projects, sites, and tutorials which helped me in creating this project:

- [Make a README](https://medium.com/@sagarganiga468/how-to-create-a-stunning-readme-md-edf1c74b6a46) - How to make a great README file.
- [Python](https://www.python.org) - For all my Python needs.
- [W3Schools](https://www.w3schools.com/) - For almost everything! I tend to google things every 2 minutes and they seem to answer the majority of my questions.
- [Stack Overflow](https://stackoverflow.com/) - For everything I can't find on W3Schools.
- [CS33a Network](https://cs50.harvard.edu/extension/web/2023/fall/projects/4/network/) - I used the skeleton of the Network app that we built earlier in the term to build my final project. Please notice that the login/out and register are all taken directly from this source and was not written by me.
