# tch_app
The Computer Hospital - Web App (CIS 3343 Project)

Templates are located within the singlepage folder

If you just want to run a single web page (with no javascript or connection to the db).
1. Download the template - _template.html_
2. Open _https://getbootstrap.com/docs/5.0/getting-started/introduction/_
3. Look for items you want on your page (search button, input box etc.)
4. Copy and paste the code you want
5. Within the style tag is where you will code your CSS
  * I like using https://www.w3schools.com/css/ as a reference, but google has a lot of answers.
  * div tags are also very useful in designing. If there is a group of components that should be together, such as a picture and a button, or a textbox     and a checkbox, wrap them around in a div
  * You can also write your javascript login within the script tag. However, in my opinion VUE makes it much easier to write javascript, but you need to install the whole web application.
  * You can also just design the page, and I'll link it up with the rest of the web application.
  * Any questions let me know
 6. After you are done, you can upload your page within the single page folder, I'll add it to the web application.

If you want to run the whole web app on your computer, follow these steps
How to Install (Windows)
1. Download Python https://www.python.org/downloads/ if not installed
 * Make sure you check 'Add python to path' when installing, if not you'll have to manually add it. Here's a tutorial on how to manually add it to path
 * https://datatofish.com/add-python-to-windows-path/
3. Download Node https://nodejs.org/en/download/ if not installed
5. Download this repository as ZIP (should be a green button that says Code
6. Extract it
7. Using the command prompt, navigate to the location of the folder you just extracted with _cd_. ie. cd C:\Downloads\tch_app\
  * You can find the location when you open up the file exporer, and click on the search bar on the top. Then, copy that location and paste it into the command prompt. Don't forget the cd before it.
8. Navigate into the backend by doing cd backend\
9. Run _pip install -r requirements.txt_
  * If an error occurs, try pip3 intall -r requirements.txt
  * If an error still occurs, let me know
10. Now go back to the main folder by doing _cd .._
11. Navigate to the frontend by doing cd frontend\
12. Run _npm install_
  * If an error occurs, let me know
13. If no error, you should be ready to start both servers
14. Start the frontend server by doing _npm run dev_

If you want, you can stop here and start navigating around, and working with the _template.vue_ file. However, database calls will not work as the backend service is not up.

 * You can use the template.vue, or use my code from one of my pages located within the frontend/src/views or frontend/src/component as reference
 * You can also upload them to the singlepages folder, or add them within the frontend/src/views folder. If you want your link to work, make sure you have added it to the frontend/router/index.js file as a router. Just copy the code for the /new_customer page. {path: '/new_customer', name: /new_customer}
 * Or just let me know and Ill add it 
 * Any questions let me know

If you have a database setup, or are connected to the remote database (not set up yet as of April 4, 2022), then you can also start the backend service.

13. Navigate to the backend folder by first doing _cd .._ then _cd backend\_
14. Make sure that within the database.py, the correct database is set up.
15. Run _python main.py_
  *If an error occurs, try python3 main.py
  *If an error still occurs, let me know
 16. From here, you can start adding some APIs, such as creating a new employee, or getting data from a customer
  
