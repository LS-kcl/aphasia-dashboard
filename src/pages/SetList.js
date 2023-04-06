import React from "react";
import axios from "axios";
import { Link } from "react-router-dom";

axios.defaults.withCredentials = true;

export default class PageList extends React.Component {
    state = {
        pages: []
    }

    componentDidMount() {
        axios.get('/api/list_sets', {'withCredentials': true })
            .then(res =>{
                const pages = res.data;
                this.setState({ pages })
            })
    }

    render() {
        return (
            <div className="col-sm-12 col-md-6 offset-md-3">
                <ol>
                    {
                        this.state.pages
                            .map(page =>
                                <div class="card">
                                    <div class="card-body">
                                        <h5 class="card-title">{page.title}</h5>
                                        <p class="card-text">{page.text}</p>
                                        <Link to={"/view_page/" + page.id} className="btn btn-light" activeStyle>
                                            View Page
                                        </Link>
                                    </div>
                                </div>
                            )
                    }
                </ol>

                <Link to="/" className="btn btn-light" activeStyle>
                    Back to home
                </Link>
            </div>
        )
    }
}