# Machos Takeaway

![Am_I_Responsive](/screenshots/responsive.png)

Machos Takeaway is a modern restaurant platform that offers a comprehensive experience for customers looking to enjoy delicious meals in a welcoming environment. 
Our website allows users to easily book tables, leave comments, create accounts, check our diverse menu, and find information about our location and opening hours.
Additionally, the site features an admin interface built with Django, which enables administrators to manage reservations, oversee customer feedback, and approve or reject comments. The admin panel also allows for easy updates to the restaurant’s menu and operational settings, ensuring that everything is current and well-organized.

## [Features](#features-1)
* ### [MainPage](#main-page)
  * #### [MainPageDelas](#main-page-offer-section)
  * #### [MainPageLocation](#main-page-location-section)
  * #### [MainPageCustomerComments](#main-page-customers-comments-section)
* ### [Navbar](#navbar-1)
* ### [About](#about-page)
* ### [Menu Page](#menu-page-1)
* ### [Account for Users](#account-for-users-1)
* ### [Footer Section](#footer-section-1)
### [Technologies](#technologies-1)
### [Programs_Used_in_project](#programs-used-in-project)
### [Testing](#testing-1)
* [Validation_reports](#validation-reports)
* [Manual_Testing](#manual-testing)
* [Making_a_Reservation](#making-a-reservation)
* [Deleting_a_Reservation](#deleting-a-reservation)
### [Automated Testing](#automated-testing)
### [Deployment](#deployment)
### [Bugs Detected](#bugs-detected)
### [Credits](#credits)
* [Other](#other)
---

# Features:

## Main Page:
![Main page](/screenshots/mainpage.png) 

### Main Page Offer Section:
#### [Menu](#features)
![Deals](/screenshots/mainpagedeals.png) 
  * Displays current promotions
    
### Main Page Location Section:
#### [Menu](#features)
![MainPageLocation](/screenshots/location2.png)
  * Using Google maps to display locations:

### Main Page Customers Comments Section:
#### [Menu](#features)
  ![MainPComments](/screenshots/mainpagcomments.png)
   * Customer comments.
     * only displays the 10 most recent comments.

## Navbar :
#### [Menu](#features)
  ![Navbar](/screenshots/navbarlogin.png)
   * Depending on the user's status, different sharing options

## About Page :
#### [Menu](#features)
  ![About](/screenshots/aboutpage.png)
   * Info about restaurant

## Menu Page :
#### [Menu](#features)
  ![Menu](/screenshots/menu.png)
   * Displays the entire restaurant menu. 

## Account for users :
#### [Menu](#features)
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
#### [Menu](#features)
  
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
#### [Menu](#features)
   
   ![Footer](/screenshots/footer.png)
   * Includes contact number, location, email adrres.
   * Address
   * Opening hours

## User Experience (UX) Design
#### [Menu](#features)

The Machos Takeaway project emphasizes an intuitive, responsive, and engaging experience across all devices. The UX decisions were guided by best practices for accessibility, visual clarity, and user-centered design principles.

###  **Key UX Features:**

| Feature | Description |
|--------------------------------------|-------------------------------------------------------------------|
| Responsive Layout  | Fully responsive across mobile, tablet, and desktop using Bootstrap 5 and custom CSS media queries |
| Navigation | Clear, consistent navigation with active link highlights and smooth redirects. |
| Comment System | Authenticated users can submit, edit, or delete comments. Superusers auto-approve, while others require moderation. |
| Reservations UX | Logged-in users can reserve tables using a simplified form with real-time validation. Past dates are disabled, and reservations under 24 hours are blocked. |
| Form Validation | Custom client- and server-side validation for all forms including phone number, booking time, and special requests. |
| Feedback & Alerts | Interactive flash messages (success, error, info) with dismiss buttons and auto-hide functionality for streamlined feedback. |
| Google Maps Integration | Embedded interactive map for location discovery via Google Maps API. |
| Accessibility | All form elements are properly labeled. Color contrasts and focus states follow accessibility best practices. |


UX Goals Achieved:

 * Reduce friction in critical user flows (e.g. table reservation, leaving a review).
 * Promote trust and transparency (approval status, success messages).
 * Align visual branding with Machos Takeaway's friendly and bold identity.

#### Wireframes :

All wireframes were initially created using Balsamiq before development began.

* Home Page:

  ![HomePageW](/READMEmedia/wireframe_main_page.png)

* Product Listing:

  ![ProductListW](/READMEmedia/wireframe_product_list.png)


* Product Detail:

  ![ProductDetailW](/READMEmedia/wireframe_product_details.png)

---

### 🎨 Color Scheme
     
  * The Machos Takeaway brand identity is reflected through a warm and appetizing color palette that enhances the user          experience across the site.



    |      Colour Name           |       Swatch     |            Hex Code                                   |   Usage                                 |
    |---------------------------------|-----------------------------|-----------------------------------------|---------------------------------------------------|
    |        **Main Yellow**       |  <span style="background-color:#ffbe33; padding:5px 20px; display:inline-block; border:1px solid #ccc;"></span> |        #ffbe33        |  Primary buttons, highlights  |
    | **Hover Yellow**           | <span style="background-color:#e69c00; padding:5px 20px; display:inline-block; border:1px solid #ccc;"></span>    | #e69c00 | Button hovers, interactive elements | 
    | **Dark Grey**               | <span style="background-color:#222831; padding:5px 20px; display:inline-block; border:1px solid #ccc;"></span>  | #222831 | Background sections (footer, cards)  |
    | **White**                  | 	<span style="background-color:#ffffff; padding:5px 20px; display:inline-block; border:1px solid #ccc;"></span>   | #ffffff | Text, backgrounds, contrast areas  |
    | **Light Grey**               | <span style="background-color:#f1f2f3; padding:5px 20px; display:inline-block; border:1px solid #ccc;"></span> | #f1f2f3 |  Menu card backgrounds    |
    | **Accent Red**              | <span style="background-color:#dc3545; padding:5px 20px; display:inline-block; border:1px solid #ccc;"></span>   | 	#dc3545  |  Error alerts, delete buttons    |
    | **Custom Green**             | <span style="background-color:#a8c65f; padding:5px 20px; display:inline-block; border:1px solid #ccc;"></span>  | #a8c65f | Confirmation, success (e.g., approve) |


    The design aims for an elegant yet fun experience, with strong contrast and visual clarity for accessibility.

    ---

---

## Technologies:
#### [Menu](#features)

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
#### [Menu](#features)

 * [Gitpod](https://www.gitpod.io/)
    * To write the code.
 * [Github](https://github.com/)
    * Storing the files online.
 * [Heroku](https://heroku.com)
    * To deploy project.
 * [Am I Responsive](https://ui.dev/amiresponsive)
    * Screenshots for README.md file.

 ---

 ## Project Management:

  #### Agile Methodology:

  This project uses Agile methodology for managing tasks and tracking progress efficiently. We leverage GitHub Issues, Milestones, and a Kanban-style project board for clear organization and transparency.

  #### MoSCoW Prioritization:

  I have ategorize tasks and user stories using the MoSCoW method, clearly indicating their importance to the project's success:

  - Must : These are the highest-priority requirements that absolutely must be included in the final product.(Highest Priority)
  - Should : These requirements should be delivered if at all possible. Their absence might reduce user satisfact.(High Priority)
  - Could : These requirements provide beneficial enhancements or improvements but are not critical to basic functionality.(Medium Priority)
  - Won't : Not critical or required; might revisit in the future.(Lowest Priority)

  #### Includes some helpfulll labels like:

  - bug : Something isn't working
  - documentation : Improvements or additions to documentation
  - help wanted : Extra attention is needed
  - question : Further information is requested

  ![Labels](/screenshots/milestones/Labels.png)
      
  #### Milestones & Sprints

  - Each Milestone corresponds to a Sprint or Epic, grouping related issues together.

  ![Milestones](/screenshots/milestones/Milestone_Finalize%20Deployment&Secutity.png)
  
  - Milestones clearly outline deadlines and project phases.
  - User stories (GitHub Issues) are linked to Milestones for tracking.

  #### Project Board

  - Use a Kanban board structured into clear columns (To Do, In Progress, and Done) to reflect real-time progress.

  ![Kanban](/screenshots/milestones/Kanban.png)

  - Issues on the board are labeled with MoSCoW tags for quick prioritization.
     
  ![Kanban](/screenshots/milestones/open_issue.png)

---

## Data Models & Relationships:

* CustomerComment Model


    | FIeld Name              | Type                                    |   Description                                  |
    |-------------------------|-----------------------------------------|---------------------------------------------------|
    | **user**                |   ForeignKey  |  Linked to User who posted the comment.|
    | **comment** | TextField | The body of the comment. |
    | **comment_date**       | DateTimeField |  When the comment was posted.  |
    | **updated_on**          |   DateTimeField    |   Auto-update on comment edit.  |
    | **is_approved**       |  	BooleanField |    Whether the comment is approved for display.   |

    ---

    ```
    
    User ──────┐
           │
        CustomerComment
             │
     [Text, Approved, Timestamp]

    ```
    - Each CustomerComment is linked to a User.
    - Comments include approval logic and timestamps.

* Reservation Model


    | FIeld Name              | Type                                    |   Description                                  |
    |-------------------------|-----------------------------------------|---------------------------------------------------|
    | **user**                |   ForeignKey  | Linked to the user making the reservation.|
    | **reservation_date** | DateTimeField | Timestamp when reservation was created. |
    | **number_of_guests**       | IntegerField | Number of guests (limited to 6 max via form). |
    | **contact_number**          |   CharField   |   Customer's contact number.  |
    | **booking_date**       |  	DateField |    Date of the reservation.   |
    | **booking_time**       |  	TimeField |    Time of the reservation.   |
    | **is_approved** | BooleanField | For internal approval management. |
    | **special_requests** | CharField | Optional field for special requests. |

     ```
    
   User ───────────────┐
                    │
               Reservation ───→ RestaurantSettings
                    │
      [Guests, Phone, Date, Time, Approved, Notes]

    ```
    - Reservations are made by users.
    - Booking slots are validated against RestaurantSettings.


* RestaurantSettings Model
 
    | FIeld Name              | Type                                    |   Description                                  |
    |-------------------------|-----------------------------------------|---------------------------------------------------|
    | **opening_time** |   TimeField  | Restaurant opening hour. |
    | **closing_time** |   TimeField  | Restaurant closing hour. |


     ```
    
     RestaurantSettings
              │
     [Opening Time, Closing Time]

    ```
    - Used by the reservation form to validate time choices.

 * About Model
 
    | FIeld Name              | Type                                    |   Description                                  |
    |-------------------------|-----------------------------------------|---------------------------------------------------|
    | **heading** |   CharField  | 	Title or heading of the about section.|
    | **content** |   TextField | Descriptive content about the restaurant. |
    | **image**  | CloudinaryField | Image uploaded using Cloudinary. |
    | **created_on** | DateTimeField | Auto-generated on creation. |
    | **updated_on** | DateTimeField | Auto-updated on modification. | 

     ```
    
     About
       │
       ├─ Heading
       ├─ Content
       ├─ Image (Cloudinary)
       ├─ Created_on
       └─ Updated_o

    ```
    - Used to dynamically display business information on the About page.

 * MenuItem Model
 
    | FIeld Name              | Type                                    |   Description                                  |
    |-------------------------|-----------------------------------------|---------------------------------------------------|
    | **title** |   CharField  | 	Name of the menu item.|
    | **description** |   TextField | Description of the item. |
    | **price**  | DecimalField | Price of the item. |
    | **category** | CharField | Menu category: burger, pizza, etc.|
    | **image** | CloudinaryField | Image hosted via Cloudinary |
    | **slug** | SlugField | Auto-generated from description. | 


     ```
    
     MenuItem
      │
      ├─ Title
      ├─ Description
      ├─ Price
      ├─ Category  ← (burger, pizza, etc.)
      ├─ Image (Cloudinary)
      └─ Slug (Auto)

    ```
    - Displays available dishes.
    - Categorized and visually enriched via images.

    ---


## Testing:
#### [Menu](#features)

### Validation reports:
  #### Main page html validation report:
  * ![mainpage](/screenshots/htmlmainpage.png)
  #### About page html validation report:
  * ![aboutnpage](/screenshots/htmlabout.png)
  #### Resrevation page html validation report:
  * ![reservationnpage](/screenshots/htmlreservation.png)

  * No errors found in html.
  
## Manual Testing:
#### [Menu](#features)

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
    <td>No comments found message</td>
  </tr>
  <tr>
    <td>Fill out comment form </td>
    <td>Complete the form and submit.</td>
    <td>A success message confirming registration appears</td>
    <td> Error message indicating that the comment is empty or invalid</td>
  </tr>
  <tr>
    <td>View added comment</td>
    <td>Refresh or navigate back to comments section </td>
    <td>The new comment appears in the list of comments </td>
    <td> No change in comments displayed</td>
  </tr>
</table>

#### Logged-in User Making a Reservation

<table>
  <tr>
    <th>User Choice</th>
    <th>Expected Action</th>
    <th>Result Correct Input</th>
    <th>Result Incorrect Input</th>
  </tr>
  <tr>
    <td>Navigate to reservation section</td>
    <td>Access the make reservation page</td>
    <td>Displays the booking form with fields to fill</td>
    <td>No wrong input</td>
  </tr>
  <tr>
    <td>Fill out reservation form</td>
    <td>Complete the form with valid details</td>
    <td>A success message confirming the reservation appears</td>
    <td>Warning message indicating that the fields cannot be empty</td>
  </tr>
  <tr>
    <td>Select booking date</td>
    <td>Choose a valid booking date from the calendar</td>
    <td>Shows the selected date in the form</td>
    <td></td>
  </tr>
  <tr>
    <td> Select booking time</td>
    <td>Choose a booking time from the available options</td>
    <td>Shows the selected time in the form</td>
    <td></td>
  </tr>
  <tr>
    <td>Attempt to make reservation less than 24 hours</td>
    <td>Fill form for pass date</td>
    <td>Warning appears indicating booking must be at least 24 hours in advance</td>
    <td> No reservation is made, and the user remains on the form</td>
  </tr>
</table>

#### Deleting a Reservation

<table>
  <tr>
    <th>User Choice</th>
    <th>Expected Action</th>
    <th>Result Correct Input</th>
    <th>Result Incorrect Input</th>
  </tr>
  <tr>
    <td>Navigate to reservations section</td>
    <td>Access the comments feature</td>
    <td>Displays the current comments and an input form to add new comments</td>
    <td>No comments found message</td>
  </tr>
  <tr>
    <td> Click on 'Cancel' for a reservation</td>
    <td>Confirm cancellation prompt</td>
    <td>Displays the current reservations associated with the user</td>
    <td> If no reservation section is blank</td>
  </tr>
  <tr>
    <td>View added comment</td>
    <td>Refresh or navigate back to comments section </td>
    <td>A success message confirming that the reservation has been cancelled appears</td>
    <td>Error message appears if the reservation does not exist</td>
  </tr>
</table>

## Automated Testing
#### [Menu](#features)

The Machos Takeaway project utilizes Django's built-in testing framework to ensure that all key functionalities work as expected. Below are the details of the tests implemented for various components of the application.

### Tests Overview
#### [Menu](#features)

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


---

## Installation & Setup

1️⃣ Clone the Repository

```
bash

git clone https://github.com/krzysztofkadela/MachosTakeaway.git  
cd MachosTakeaway

```
2️⃣ Set Up a Virtual Environment

```
bash

python -m venv env  
source env/bin/activate  # On Windows: env\Scripts\activate

```

3️⃣ Install Dependencies

```
bash

pip install -r requirements.txt

```

4️⃣ Create a .env File

Add your local environment variables inside .env or env.py:

```
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
GOOGLE_MAPS_API_KEY=your-google-maps-api-key
CLOUDINARY_URL = your-cloudinary-url

```

5️⃣ Apply Migrations & Run the Server

```
python manage.py migrate  
python manage.py runserver

```


## Deployment (Heroku)
#### [Menu](#features)

###  Before You Begin:
 - Make sure DEBUG = False in production
 - Confirm ALLOWED_HOSTS includes your Heroku domain

### Deploy Using the Heroku Dashboard

  - #### Create a Heroku App
     * Go to Heroku Dashboard
     * Click "New" → "Create New App"
     * Enter a unique app name
     * Choose a region and click "Create app"
  
  * #### Connect to GitHub
    - Go to the Deploy tab
    - Choose GitHub as deployment method
    - Connect your GitHub account
    - Search and connect your MachosTakeaway repo

  * #### Set Up Environment Variables (Config Vars)
    -  In the Settings tab → Click "Reveal Config Vars":

   ```
     SECRET_KEY = your-secret-key
     DEBUG = False
     DATABASE_URL = your-postgres-db-url
     GOOGLE_MAPS_API_KEY = your-maps-api-key
     CLOUDINARY_URL = your-cloudinary-url

  ```
  * #### Trigger Deployment
     - In the Deploy tab → Manual Deploy section
     - Click "Deploy Branch"
     - Heroku will install dependencies and run build

  * #### Post-Deployment Setup
     - From the More → Run Console:

     ```
     bash

      python manage.py migrate
      python manage.py collectstatic --noinput
      python manage.py createsuperuser
     ```

  * #### Done! Your app is now live. Visit it via the "Open App" button in Heroku dashboard

   * Live "Machos Takeway" app you can find by clicking this link:
     [heroku](https://machostakaeaway-202ce3a8c774.herokuapp.com/)


## Bugs Detected:
#### [Menu](#features)

 ### **Issue with Reservation Date Input**: 
  * During the initial testing phase of the reservation functionality, it was discovered that the system allowed users to make reservations for past dates. This posed a significant concern as it would lead to confusion and inaccuracies in reservation management.

  *  **Resolution**: 
    The validation logic in the `ReservationForm` was updated to ensure that users cannot select a past date when trying to make a reservation. Now, only future dates are permitted for booking, enhancing the user experience and maintaining the integrity of reservations.

  ### **Edit Comment Issue 1**

  * Description:

      When a user attempted to edit a comment, instead of updating the existing comment, the system created a new comment entry, leaving the old one unchanged. This led to duplicated comments and confusion.

  * Expected Behavior:

     The existing comment should be updated in place, not duplicated.

  * Root Cause:

     The edit_comment view was not using the instance parameter in the form, so Django treated the form submission as a new comment instead of an update.

  * Resolution:

     The edit_comment view was updated to pass the existing comment instance into the form:

     ```
     python
     
     form = CustomerCommentForm(request.POST, instance=comment)
     
     ```
   
  ### **Edit Comment Issue 2**

  * Description:

    When a user edits an existing comment, the comment is automatically re-approved even if it was previously pending. This bypasses the intended moderation process for non-admin users.

  * Expected Behavior:

    Edited comments by regular users should be marked as is_approved = False and re-submitted for approval after modification.

  * Root Cause:

    The edit_comment view was missing logic to reset the is_approved field for non-superusers.

  * Resolution: 

    The following fix was applied in views.py under the edit_comment function:

    ```
    python

    if not request.user.is_superuser:
    updated_comment.is_approved = False
    
    ```
  
  
## Unfixed Bugs:
  * All detected bugs have been fixed.

## Credits:
  *  To check the correct operation of most functions, the following was used:
     [Python Tutor](https://pythontutor.com/visualize.html#mode=edit)
  *  Template use for a project was downloaded from https://themewagon.com/themes/

### Other:
  
   * Much of the information about python was obtained from https://www.w3schools.com/python/.

#### [Menu](#features)