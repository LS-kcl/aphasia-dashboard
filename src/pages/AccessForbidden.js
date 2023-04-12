import React from "react";
import SentenceHelper from "../helpers/SentenceHelper";
import { Link } from "react-router-dom";

export default class AccessForbidden extends React.Component {
    render() {
        return (
            <>
                <div className="cover-container d-flex h-100 p-3 mx-auto flex-column">
                <main role="main" className="inner cover">
                            <h1 className="error-heading text-white">403 Forbidden</h1>
                            <p className="lead text-white">You are not permitted to access this page</p>
                            <p className="lead text-white">If you are the owner of this page please <Link to="/login" activeStyle>log in here</Link>, otherwise contact the sharer of the page.</p>
                            <Link to="/" className="btn btn-light" activeStyle>
                                Return to home
                            </Link>
                </main>
                </div>
            </>
        )
    }
}