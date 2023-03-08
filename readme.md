# Doing
- Learn how to create react cards to be displayed for each set
- Learn how to create pages and redirect in react
- Implement image selection to add images to sentences
- Implement GTTS on frontend

# To-do (before next set of office hours):
- Try to implement AI image generation into image selection
- Host site on heroku
- Write up quick draft of report for feedback

# Stretch goals:
- Begin some work on the report
- Start implementing login functionality
- Add navbar to move between pages

# Done
- Add edit functionality, allowing the user to edit sentences as opposed to just creating them
- Reformat pages to look nicer
- Complete browse page to show all created sets
- Implement tests for models
- Migrate from view functions to API calls
- Create views for external API calls 

# Notes for frontend:
## Requirements:
- node v18.14.2
- npm 9.5.1

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

Note: this is a one-way operation. Once you `eject`, you can't go back!

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build depend    ency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have     full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this     point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use th    is feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

# Resources used:
[Django text to speech](https://pytutorial.com/django-text-to-speech/)
[Installing axios for react](https://www.digitalocean.com/community/tutorials/react-axios-react)
[Developing react components](https://www.digitalocean.com/community/tutorial_series/how-to-code-in-react-js)
[Installing bootstrap for React](https://create-react-app.dev/docs/adding-bootstrap/)
[Using react-bootstrap for responsive web design](https://react-bootstrap.github.io/layout/grid/)
[Setting innerHTML values in React](https://blog.logrocket.com/using-dangerouslysetinnerhtml-in-a-react-application/)
[Rendering markdown in the page](https://www.npmjs.com/package/remarkable-react)
[Storing secret keys securely for deployment](https://stackoverflow.com/questions/15209978/where-to-store-secret-keys-django)

# External APIs used:

# Costs:

Heroku Web Hosting Services: £24 (6 months £4/mo eco dyno hosting)
Heroku Postgres Database: £24 (6 months £4/mo mini plan)
Google Cloud Text-to-Speech: £0 (WaveNet free character allowance)
Unsplash Image API: £0 (50 requests/hr free allowance)
OpenAI Image Generation: £12 (Estimated 1500 images at £0.02/image, minus £18 free credits)

Total: £60