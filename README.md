# Item-Catalog

## Description

Create a restaurant ordering app where users can add, edit and delete orders. 

## Running the Program 

  1. Install Vagrant and VirtualBox
  2. Unzip and place the Item Catalog folder in your Vagrant directory
  3. Change directory to vagrant 
  4. Launch Vagrant using the command vagrant ssh
  5. Initialize the database using python database_setup.py
  6. Extract some data by executing python menus.py
  7. Launch application python project.py
  8. Open the browser and go to http://localhost:8000/
  
## JSON Endpoints
    
   ## JSON Endpoint of all restaurants
   
   /restaurants/JSON
    
   ## JSON Endpoint of orders
   
   /restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON

   ## JSON Endpoint of specific order
    /restaurants/<int:restaurant_id>/menu/JSON
