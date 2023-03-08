import React from "react";
import axios from "axios";
import { Link } from "react-router-dom";

export default class PageList extends React.Component {
    state = {
        pages: []
    }

    componentDidMount() {
        axios.get('/api/list_sets')
            .then(res =>{
                const pages = res.data;
                this.setState({ pages })
            })
    }

    render() {
        return (
            <>
                <ol>
                    {
                        this.state.pages
                            .map(page =>
                                <li>
                                    <Link to={"/view_page/" + page.id} activeStyle>
                                        {page.title}
                                    </Link>
                                </li>
                            )
                    }
                </ol>

                <Link to="/" activeStyle>
                    Back to home
                </Link>
            </>
        )
    }
}