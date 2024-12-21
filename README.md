# Machos Takeaway

![Am_I_Responsive](/screenshots/responsive.png)

Machos Takeaway is a modern restaurant platform that offers a comprehensive experience for customers looking to enjoy delicious meals in a welcoming environment. 
Our website allows users to easily book tables, leave comments, create accounts, check our diverse menu, and find information about our location and opening hours.
Additionally, the site features an admin interface built with Django, which enables administrators to manage reservations, oversee customer feedback, and approve or reject comments. The admin panel also allows for easy updates to the restaurant’s menu and operational settings, ensuring that everything is current and well-organized.

### [Features](#features-1)
### [Technologies](#technologies-1)
### [Programs_&_Libraries_Used_in_project](#programs--libraries-used-in-project)
### [Testing](#testing-1)
* [Validation_reports](#validation-reports)
* [Manual_Testing](#manual-testing)
### [Deployment](#deployment-1)
### [Bugs Detected](#bugs-detected-1)
### [Credits](#credits-1)
 * [Other](#other)
---

# Features:

## Main Page:
![Main page](/screenshots/mainpage.png) 

### Main Page Offer Section:
![Main page](/screenshots/mainpagedeals.png) 
  * Displays current promotions
    
### Main Page Location Section:
![Update menu](/screenshots/location2.png)
  * Using Google maps to display locations:

### Main Page Customers Comments Section:
  ![Report Menu](/screenshots/mainpagcomments.png)
   * Customer comments.
     * only displays the 10 most recent comments.

## Navbar :
  ![Report Menu](/screenshots/navbarlogin.png)
   * Depending on the user's status, different sharing options

## About Page :
  ![Report Menu](/screenshots/aboutpage.png)
   * Info about restaurant

## Menu Page :
  ![Report Menu](/screenshots/menu.png)
   * Displays the entire restaurant menu. 


## Technologies:

 * Django: The main framework, providing a robust MVC architecture, ORM, and built-in admin interface.
 * HTML/CSS: For developing the front-end layout and styling.
 * Bootstrap: Create responsive design for website.
 * PostgreSQL to cretate databes.
 * Django Allauth: For user authentication, registration, and account management.
 * Django Crispy Forms: To manage and render forms more easily and with a better user experience.
 * Gunicorn For serving Django application in production environments.
 ---
## Programs Used in project:

 * [Gitpod](https://www.gitpod.io/)
    * To write the code.
 * [Github](https://github.com/)
    * Storing the files online.
 * [Heroku](https://heroku.com)
    * To deploy project.
 * [Am I Responsive](https://ui.dev/amiresponsive)
    * Screenshots for README.md file.
---
## Testing:

### Validation reports:
  #### Main page html validation report:
  * ![mainpage](/screenshots/htmlmainpage.png)
  #### About page html validation report:
  * ![aboutnpage](/screenshots/htmlabout.png)
  #### Resrevation page html validation report:
  * ![reservationnpage](/screenshots/htmlreservation.png)

  * No errors found in html.
  
### Manual Testing:

<table>
  <tr>
    <th>User Choice</th>
    <th>Expected Action</th>
    <th>Result Correct Input</th>
    <th>Result In Correct Input</th>
  </tr>
  <tr>
    <td>Register new user navbar link</td>
    <td>Display</td>
    <td>Number 1 and Enter section UpdateStock Open</td>
    <td>Letter 'A', Number 5 warning and question for correct input.</td>
  </tr>
  <tr>
    <td>Main Menu Choice 2</td>
    <td>Pass to section "Update Product List".</td>
    <td>Number 2 pick, correct section open.</td>
    <td>Rendom String inputed, warning and question for correct input .</td>
  </tr>
  <tr>
    <td>Main Menu Choice 3</td>
    <td>Pass to section "Stock Report"</td>
    <td>Number 3 pick, correct section open.</td>
    <td>Number 10 choose , wrong number warning appear.</td>
  </tr>
  <tr>
    <td>Main Menu Choice 4</td>
    <td>Close program.</td>
    <td>Affter choose '4' program finish.</td>
    <td>Letter q , wrong input warning, "please chose number from 1-4" appear.</td>
  </tr>
  <tr>
    <td>Update Stock Menu</td>
    <td>Choose 1/2 open correct section.</td>
    <td>After pick nuber 1 or 2 correct secton open.</td>
    <td>Wrong input, like string or number biger then 3, warning apears all working ok.</td>
  </tr>
  <tr>
    <td>Report Menu</td>
    <td>Choose 1/2/ print to the terminal correct report.</td>
    <td>With correct inputs all reports were printed correctly, and number 4 returned to main menu.</td>
    <td>Wrong input, like string or number biger then 3, warning apears all working ok.</td>
  </tr>

</table>

* Testing correct inputs and worksheet update for Product List:
  * Product Name, max 20 characters and using only letters and space, working correctly.
  * Product Name Size chose only from the list working correct, wrong input warning apears.
  * Product barcode: 13 characters and only numbers after wrong input warning to use correct values.
  * After all inputs are correct Product List worksheets are updated correctly, and new products are added to the list.
* Testing correct inputs and worksheet update for Goods In and Goods Out.
  * App displaying all products one by one and asking for numbers only, warning if incorrect input.
  * After all quantitys are collected, worksheets correctly updated.

## Deployment:

### This app was deployed using Code Institute's mock terminal for Heroku

   #### Simple steps:

   * Fork or clone this repository
   * Create a new Heroku app
   * Set the build packs to Python and NodeJs in that order
   * Link the heroku app to the repository
   * Click on Deploy
   * Live "Natures Oils Stock System" app you can find by clicking this link:
     [heroku](https://naturesoilsstock-9ab4d188a6d6.herokuapp.com/)


## Bugs Detected:
  * When testing the function  "update_stock(choice, product_list)" and function "update worksheet()",
    there was a problem with the correct data being retrieved from the "Tuple" that the first function returned.
    The worksheet was not updated and a message about incorrect data appeared.
  * The problem was solved by changing the 'Tuple' to a 'List' and converting the numeric input to integer.
  
## Unfixed Bugs:
  * All detected bugs have been fixed.

## Credits:
  *  To check the correct operation of most functions, the following was used:
     [Python Tutor](https://pythontutor.com/visualize.html#mode=edit)
  *  Google sheets to store data.
### Other:
   * Much of the information about python was obtained from https://www.w3schools.com/python/.