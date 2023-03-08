import React from "react";
import SentenceHelper from "../helpers/SentenceHelper";
import { Nav } from "react-bootstrap";
import { Link } from "react-router-dom";

export default class Home extends React.Component {
    render() {
        return (
            <>


                <Link to="/browse" activeStyle>
                    Browse pages
                </Link>
                <p>   </p>
                <Link to="/add_set" activeStyle>
                    Create a page
                </Link>

            </>
        )
    }
}