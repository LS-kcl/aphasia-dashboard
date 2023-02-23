import React from "react";
import axios from "axios";

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
            <ul>
                {
                    this.state.pages
                        .map(page =>
                            <li key={page.id}>{page.title}</li>
                        )
                }
            </ul>
        )
    }
}