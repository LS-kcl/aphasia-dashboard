import React from "react";
import axios from "axios";

export default class SetAdd extends React.Component {
    state = {
        title: ''
    }

    handleChange = event => {
        this.setState({ title: event.target.value })
    }

    handleSubmit = event => {
        event.preventDefault();

        // Creating a json to send using axios
        const title = this.state.title

        axios.post(`/api/create_set`, { title })
            .then(res => {
                console.log(res);
                console.log(res.data);
            })
    }

    render() {
        return (
            <div>
                <form onSubmit={this.handleSubmit}>
                    <label>
                        Set Title:
                        <input type="text" name="title" onChange={this.handleChange}/>
                    </label>
                    <button type="submit">Create Set</button>
                </form>
            </div>
        )
    }

}