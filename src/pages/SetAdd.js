import React from "react";
import axios from "axios";
import { Remarkable } from "remarkable";
import { Link } from "react-router-dom";
import { Col, Row } from "react-bootstrap";
axios.defaults.withCredentials = true;

export default class SetAdd extends React.Component {
    constructor(props){
        super(props);
        this.markdown = new Remarkable();
        this.handleChangeText = this.handleChangeText.bind(this);
        this.state = { 
            title: '',
            text: ''
        };
    }

    getRawMarkup() {
        return { __html: this.markdown.render(this.state.text) }
    }

    handleChangeTitle = event => {
        this.setState({ title: event.target.value })
    }

    handleChangeText = event => {
        this.setState({ text: event.target.value })
    }

    handleSubmit = event => {
        event.preventDefault();

        // Creating a json to send using axios
        const title = this.state.title
        const text = this.state.text

        axios.post(`/api/create_set`, { title, text })
            .then(res => {
                console.log(res);
                console.log(res.data);
                // Redirect to homepage
                window.location.href = '/pick_images/' + res.data.id
            })
    }

    render() {
        return (
            <div>
                <form onSubmit={this.handleSubmit}>
                    <label>
                        Set Title:
                        <input type="text" name="title" onChange={this.handleChangeTitle}/>
                    </label>
                    <Row>
                        <Col>
                            <h3> Enter your text here: </h3>
                            <textarea 
                                id="userInput"
                                name="text"
                                onChange={this.handleChangeText}
                                defaultValue={this.state.value}
                            />
                        </Col>
                        <Col>
                            <h3> Text preview: </h3>
                            <div
                                className="output"
                                dangerouslySetInnerHTML={this.getRawMarkup()}
                            />
                        </Col>
                    </Row>
                    <button type="submit">Create Set</button>
                </form>

                <Link to="/" activeStyle>
                    Back to home
                </Link>
            </div>
        )
    }

}