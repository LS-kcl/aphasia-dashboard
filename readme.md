# Installation Instructions

## Set up a virtual environment:

`virtualenv venv`
`source venv/bin/activate`

## Install packages required for backend:

`pip install -r requirements.txt`


## Installing the Frontend:

`npm install`


## Apply migrations to the database

`python manage.py migrate`

## Create secret .env file with API Keys

Create developer accouns with OpenAI and Unisplash, and add their secret keys to a new file named `.env` in the root directory

## Run backend and frontend

`python3 manage.py runserver`
`npm run start`

# Resources used:
[Django text to speech](https://pytutorial.com/django-text-to-speech/)
[Installing axios for react](https://www.digitalocean.com/community/tutorials/react-axios-react)
[Developing react components](https://www.digitalocean.com/community/tutorial_series/how-to-code-in-react-js)
[Installing bootstrap for React](https://create-react-app.dev/docs/adding-bootstrap/)
[Using react-bootstrap for responsive web design](https://react-bootstrap.github.io/layout/grid/)
[Setting innerHTML values in React](https://blog.logrocket.com/using-dangerouslysetinnerhtml-in-a-react-application/)
[Rendering markdown in the page](https://www.npmjs.com/package/remarkable-react)
[Storing secret keys securely for deployment](https://stackoverflow.com/questions/15209978/where-to-store-secret-keys-django)
[Developing multi-page react apps 1](https://www.geeksforgeeks.org/how-to-create-a-multi-page-website-using-react-js/)
[Developing multi-page react apps 2](https://stackoverflow.com/questions/41956465/how-to-create-multiple-page-app-using-react)
[Remarkable documentation](https://github.com/jonschlinkert/remarkable)
[Possible solution for stripping markdown](https://www.npmjs.com/package/remove-markdown)
[Getting values from URL inside component](https://stackoverflow.com/questions/58548767/react-router-dom-useparams-inside-class-component)
[Setting up login and authentication cookies for React](https://priyanshuguptaofficial.medium.com/django-and-react-integration-b712321a5232)
[Setting up login and authentication cookies for React 2](https://medium.com/@ronakchitlangya1997/jwt-authentication-with-react-js-and-django-c034aae1e60d)
[JWT tokens simplified](https://www.permify.co/post/jwt-authentication-in-react)
