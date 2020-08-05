# hangman-mvp

[ Visit application](https://condescending-boyd-766f38.netlify.app/) 
## Description
The **Hangman-mvp** is an application that allows the user to play the hangman game and also add categories with words.
The Frontend built with **VueJs - Javascript** and the Backend built on **Flask - Python**.


The FrontEnd is a VueJs application located in the client folder 
The Flask project is in the api folder

The flask app contains endpoints to
- Get categories
- Add categories with associated words
- Get words by category

* Here is the [ LIVE FRONTEND URL](https://condescending-boyd-766f38.netlify.app/) of the application


## Technology Stack

- Vue
- Flask
- Postgres


###  Setting Up For Local Development

-   Check that python 3 is installed:
	
	-   Clone the hangman-mvp repo and cd into it:

    ```
    git clone https://github.com/tonyguesswho/hangman-mvp.git
    ```

    ```
    python --version
    >> Python 3.7.0
    ```

-   Create and activate virtual enviroment:

    ```
    python3 --m venv env

    ```

-   Install dependencies from requirements.txt file:

    ```
    pip install -r requirements.txt
    ```

-   Make a copy of the .env.sample file in the api folder and rename it to .env and update the variables accordingly:


-   Apply migrations:

    ```
    in the api folder run python manage.py db migrate
    ```

*   Start the application with the command

    ```
    flask run
    ```

*   Deactivate the virtual environment once you're done:
    ```
    exit
    ```





#### (Setting up the front end locally)
- Check that Node (recommended v11.12+) and npm are installed on your machine.

- Install dependencies
```
cd into the client folder and run npm install
```

- Add this to the .env file
```
VUE_APP_API_URL=http://127.0.0.1:8000
```
- Run app
```
npm run serve
```
- Open Application in browser
```
http://127.0.0.1:8080
```
- Production build
```
npm run build
```




I will appreciate any feedback on this project :)
