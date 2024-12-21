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
![Deals](/screenshots/mainpagedeals.png) 
  * Displays current promotions
    
### Main Page Location Section:
![MainPageLocation](/screenshots/location2.png)
  * Using Google maps to display locations:

### Main Page Customers Comments Section:
  ![MainPComments](/screenshots/mainpagcomments.png)
   * Customer comments.
     * only displays the 10 most recent comments.

## Navbar :
  ![Navbar](/screenshots/navbarlogin.png)
   * Depending on the user's status, different sharing options

## About Page :
  ![About](/screenshots/aboutpage.png)
   * Info about restaurant

## Menu Page :
  ![Menu](/screenshots/menu.png)
   * Displays the entire restaurant menu. 

## Account for users :

  ### Registration form:

  ![Registration](/screenshots/registerform.png)
   * New user is able to create account.
   * Acount is needed to add comment and make table reservation.

  ### Login form for registered user:

  ![signin](/screenshots/sininform.png)
   * Registered user can login.

  ### Logout form:

  ![Signout](/screenshots/signout.png)
   * For user to logout from his account.

## Options for logged in users:
  
   ### Make reservation (book table):

  ![Makereservation](/screenshots/makereservation.png)
   * User can easy make reservation by using reservation form.

  ### Manage reservation see reservation status:

  ![Reservation](/screenshots/reservation.png)
   * User can easy check reservation status can also cancel reservation.

  ### Leave a comment:

  ![Comments](/screenshots/comments.png)
   * In this section user can add/delete or edit comments.
   * Only comments done by loged in user are displayed in this section.
   * User can only change his comments.


## Footer section:
   
   ![Footer](/screenshots/footer.png)
   * Includes contact number, location, email adrres.
   * Address
   * Opening hours



## Technologies:

 * Django: The main framework, providing a robust MVC architecture, ORM, and built-in admin interface.
 * HTML/CSS: For developing the front-end layout and styling.
 * Bootstrap: Create responsive design for website.
 * PostgreSQL to cretate databes.
 * Django Allauth: For user authentication, registration, and account management.
 * Django Crispy Forms: To manage and render forms more easily and with a better user experience.
 * Gunicorn For serving Django application in production environments.
 * Jest used for testing front-end functionalities in the application.
 * Babel JavaScript compiler to use the latest JavaScript features, ensuring compatibility across different browsers.
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
 #### Register new user

<table>
  <tr>
    <th>User Choice</th>
    <th>Expected Action</th>
    <th>Result Correct Input</th>
    <th>Result Incorrect Input</th>
  </tr>
  <tr>
    <td>Register new user navbar link</td>
    <td>Display the registration form</td>
    <td>Form displays</td>
    <td>No wrong input required is only link.</td>
  </tr>
  <tr>
    <td> Fill out registration form</td>
    <td>Complete the form and submit .</td>
    <td>A success message confirming registration appears</td>
    <td>Error message indicating what fields need correction.</td>
  </tr>
  <tr>
    <td>Correctly filled email address </td>
    <td>Check email field for valid email format</td>
    <td>Acknowledgment of successful email entry</td>
    <td>Error about invalid email format appears </td>
  </tr>
  <tr>
    <td>Password confirmation</td>
    <td>Confirm passwords match</td>
    <td>Registration is successful; user is created</td>
    <td>Error indicating passwords do not match appears</td>
  </tr>

</table>

#### Logged-in User Adds Comment

<table>
  <tr>
    <th>User Choice</th>
    <th>Expected Action</th>
    <th>Result Correct Input</th>
    <th>Result Incorrect Input</th>
  </tr>
  <tr>
    <td>Navigate to comments section</td>
    <td>Access the comments feature</td>
    <td>Displays the current comments and an input form to add new comments</td>
    <td></td>
  </tr>
  <tr>
    <td> Fill out registration form</td>
    <td>Complete the form and submit .</td>
    <td>A success message confirming registration appears</td>
    <td>Error message indicating what fields need correction.</td>
  </tr>
  <tr>
    <td>Correctly filled email address </td>
    <td>Check email field for valid email format</td>
    <td>Acknowledgment of successful email entry</td>
    <td>Error about invalid email format appears </td>
  </tr>
  <tr>
    <td>Password confirmation</td>
    <td>Confirm passwords match</td>
    <td>Registration is successful; user is created</td>
    <td>Error indicating passwords do not match appears</td>
  </tr>

</table>

## Automated Testing

The Machos Takeaway project utilizes Django's built-in testing framework to ensure that all key functionalities work as expected. Below are the details of the tests implemented for various components of the application.

### Tests Overview

- **Reservation Tests**:
  - **`test_make_reservation`**: Verifies that a logged-in user can successfully create a reservation and receives a success message.
  - **`test_reservation_with_short_notice`**: Checks that a user cannot make a reservation less than 24 hours in advance, displaying an appropriate warning message.
  - **`test_cancel_reservation`**: Confirms that users can cancel their own reservations and receive a success message.
  - **`test_cancel_nonexistent_reservation`**: Tests that attempting to cancel a non-existent reservation results in the appropriate error handling.

- **Menu Tests**:
  - **`test_menu_view_status_code`**: Ensures that the menu view loads successfully with a status code of 200.
  - **`test_menu_view_template`**: Checks that the correct template is used to display the menu.
  - **`test_menu_view_context`**: Verifies that the context contains the expected menu items.

- **Main Page Tests**:
  - **`test_main_page_loads`**: Tests that the main page loads successfully with a status code of 200.
  - **`test_main_page_template_used`**: Ensures that the correct template is used when rendering the main page.
  - **`test_main_page_context`**: Checks that the context of the main page contains the expected number of approved comments.

- **JavaScript Tests**:
  - **Alert Functionality**: 
    - The JavaScript tests verify that auto-closing alert messages disappear after a specified time and can be smoothly faded out.
    - Tests utilize **Jest** and **@testing-library/jest-dom** to ensure DOM manipulation occurs as expected.

  ![Allerttestjs](/screenshots/allerttestjs.png)

### Running the Tests

   To run all tests in the Django project, use the following command:

    python manage.py test

## Deployment:

### This app was deployed on Heroku

   #### Simple steps:

   * Fork or clone this repository
   * Create a new Heroku app
   * Link the heroku app to the repository
   * Click on Deploy
   * Live "Machos Takeway" app you can find by clicking this link:
     [heroku](https://machostakaeaway-202ce3a8c774.herokuapp.com/)


## Bugs Detected:
  * ---
  * --
  
## Unfixed Bugs:
  * All detected bugs have been fixed.

## Credits:
  *  To check the correct operation of most functions, the following was used:
     [Python Tutor](https://pythontutor.com/visualize.html#mode=edit)
  *  Template use for a project was downloaded from https://themewagon.com/themes/

### Other:
  
   * Much of the information about python was obtained from https://www.w3schools.com/python/.