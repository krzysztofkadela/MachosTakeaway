# Machose Takeaway

![Am_I_Responsive](/screenshots/responsive.png)

A small company producing sauces needs a simple, uncomplicated system to control the amount of products in the warehouse.
Basic tasks:

Adding manufactured products to the stock.

Recording the quantity and type of products shipped from the warehouse.

Adding new products to the main list.

Checking stock levels.

Checking total sales: product - quantity sold.

Checking the total number of manufactured products: product - quantity produced.


## Table of Contents

### [Stock System Structure](#stock-structure-1)
### [Features_coming_soon](#features-coming-soon)
### [Technologies_used_in_the_project](#technologies-used-in-the-project)
### [Programs_&_Libraries_Used_in_project](#programs--libraries-used-in-project)
### [Testing](#testing-1)
* [Validation_reports](#validation-reports)
* [Manual_Testing](#manual-testing)
### [Deployment](#deployment-1)
### [Bugs Detected](#bugs-detected-1)
### [Credits](#credits-1)
 * [Other](#other)
---

## Stock Structure:

### Main Menu:
![Main menu](/assets/images/main_menu.png) 
  * Main Menu Contains 4 options:
    * 1 - Update Stock.
    * 2 - Update Product List.
    * 3 - Stock Report.
    * 4 - Finish.

### Update Stock Menu:
![Update menu](/assets/images/update_stock_menu.png)
  * Update Stock Menu Contains 3 option:
   * 1 - Goods In
   * 2 - Goods Out
   * 3 - Return to Main Menu

### Report Menu:
  ![Report Menu](/assets/images/report_menu.png)
   * Report Contains 4 Options
      * 1 - Full Stock By Product.
      * 2 - Total Production.
      * 3 - Total Sale.
      * 4 - Return


## Features coming soon:

* Two levels of access:
  *  Administrator(manager)
  *  General User

* New stock reports:
  * To control raw materials usage.
---

## How to use :

 * Main menu :
    * From the main menu you can select 4 basic options after pressing the appropriate number on the keyboard and  
      pressing 'ENTER', the application will go to the next section or will exit the program(4).
      * After selecting option no. 1, the program will open a menu that will give you the option of updating stock levels.
        * Update Stock Menu:
          * '1' -  The program will display all products one by one with a question asking how many pieces to add to the warehouse.
          * '2' - Displays all products individually with a question asking how many pieces were sent out.   
          * '3' - Selecting the third option will return you to the previous menu.
      * By selecting the option number 2  you can add another product to the list of products produced in Natures Oils, to do 
         this you need to follow some rules which will be displayed in the terminal:
        * Type and number of characters you can use when entering a new product name.
        * The right size, choose from the size list.
        * Appropriate barcode length.
      * Option 3  report options:
        * '1' - After selecting this option, the current stock status for each product will be displayed.
        * '2' - Total number of products produced for each of the list.
        * '3' - Total number of products sold.
        * '4' - Return to previous menu

### Data storage :
   * The app uses 'Google Sheets to store all data:
      * "Product list" worksheet store all products name, size and barcode, can be update by user: 
        ![Product List](/assets/images/product_list_worksheet.png)
      * "Product Size" list worksheet, can't be update from app by user:
        ![Product Size](/assets/images/product_size_list.png)
      * "Quantity In" worksheet, store inputs from user about production for each product.
        ![Quantity In](/assets/images/goods_in_worksheet.png)
      * "Quantity Out" worksheet to store all inputs for products send out from warehouse.
        ![Quantity Out](/assets/images/qty_out_worksheet.png)

---
## Technologies used in the project:

 * [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
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
  * ![Valid](/assets/images/validator.png)

  * No errors.
  
### Manual Testing:

<table>
  <tr>
    <th>User Choice</th>
    <th>Expected Action</th>
    <th>Result Correct Input</th>
    <th>Result In Correct Input</th>
  </tr>
  <tr>
    <td>Main Menu Choice 1</td>
    <td>Pass to section Update Stock</td>
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