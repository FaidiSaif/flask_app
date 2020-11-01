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