# Item-Catalog

## Description

Create a restaurant ordering app where users can add, edit and delete orders. 

## Running the Program 

  1. Install Vagrant and VirtualBox
  2. Unzip and place the Item Catalog folder in your Vagrant directory
  3. Change directory to vagrant 
  4. Launch Vagrant using the command vagrant ssh
  5. Initialize the database using python database_setup.py
  6. Extract some data by executing python CatalogItems.py
  7. Launch application python Shoppingmain.py
  8. Open the browser and go to http://localhost:8000/
  
## JSON Endpoints
    
   ## JSON Endpoint of all shops
   
    @app.route('/shops/JSON/')
    
   ## JSON Endpoint of Shopping Items
   
    @app.route('/shops/<int:shopping_id>/ShoppingItem/JSON')

   ## JSON Endpoint of specific shopping items
    @app.route('/shops/<int:shopping_id>/ShoppingItem/<int:ShoppingItem_id>/JSON')
