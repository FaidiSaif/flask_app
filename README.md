# flask_app
This is an example of a flask application for a store  


# to setup with heroku : 
1_ add the     
        -procfile   
        -requirements.txt   
        -runtime.txt    
        -uwsgi.ini files    
        
2_ in the settings set the buildpack to python 

note that any command in __name__  == "__main__" will not be executed 
since uwsgi doesn't run the script directly but it loads the app module and run it itself

#Heroku debugging: 
install heroku locally : sudo snap install --classic heroku

login to heroku        : heroku login

see logs with          : heroku logs --app=stores-rest-api-saif

#limitations of free tier : 
-limited numbers of hours heroku can run to 1000hours 

-each time the dyno go to sleep (after 30min without any request) we loose the data.db 

-the solution is to use more available storage system with heroku which is postgreSQL

#setup postgreSQL :
1-install it from heroku adds-on 

2-setup the environment variable DATABASE_URL in your heroku project as the pstgreSQl path in the 
virtual machine of the dyno

2-make the path to the database useful locally and on heroku:
app.config["SQLALCHEMY_DATABASE_URI"]   = os.environ.get('DATABASE_URL', 'sqlite:///data.db')

---> if the DATABASE_URL environment variable is set retrieve it's value else use the sqlite:///data.db as a default path

3-add the library psycopg2 in the requirements.txt file in order to handle the postgreSQL database





























