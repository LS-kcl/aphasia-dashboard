import React from "react";
import SentenceHelper from "../helpers/SentenceHelper";
import { Link } from "react-router-dom";

export default class NotFound extends React.Component {
    render() {
        return (
            <>
                <div className="cover-container d-flex h-100 p-3 mx-auto flex-column">
                <main role="main" className="inner cover">
                            <h1 className="error-heading text-white">404 Not Found</h1>
                            <p className="lead text-white">The page you were looking for could not be found, are you sure you have typed the URL in correctly?</p>
                            <Link to="/" className="btn btn-light" activeStyle>
                                Return to home
                            </Link>
                </main>
                </div>
            </>
        )
    }
}