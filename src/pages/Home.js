import React from "react";
import SentenceHelper from "../helpers/SentenceHelper";
import { Link } from "react-router-dom";

export default class Home extends React.Component {
    render() {
        return (
            <>
                <div className="cover-container d-flex h-100 p-3 mx-auto flex-column">
                <main role="main" className="inner cover">
                            <h1 className="cover-heading text-white">SpeakEasy</h1>
                            <p className="lead text-white">SpeakEasy is a tool for creating web content for those with aphasia quickly and easily. Simply enter some text to be made accessible, style with markdown if desired, and select some images for the final hosted page.</p>
                            <Link to="/browse" className="btn btn-light" activeStyle>
                                Browse pages
                            </Link>
                            <Link to="/add_set" className="btn btn-light" activeStyle>
                                Create a page
                            </Link>
                </main>
                </div>

                <footer className="mastfoot mt-auto">
                    <div className="inner">
                        <p className="text-white">If not logged in already, please login <Link to="/login" activeStyle>here</Link>.</p>
                    </div>
                </footer>
            </>
        )
    }
}