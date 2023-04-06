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
                <h1 className="text-white">Enter a name and some text content for the page</h1>
                <form onSubmit={this.handleSubmit}>
                    <label className="text-white">
                        Set Title:
                        <input type="text" name="title" onChange={this.handleChangeTitle}/>
                    </label>
                    <Row>
                        <Col>
                            <h3 className="text-white"> Enter your text here: </h3>
                            <textarea 
                                id="userInput"
                                name="text"
                                onChange={this.handleChangeText}
                                defaultValue={this.state.value}
                            />
                        </Col>
                        <Col>
                            <h3 className="text-white"> Text preview: </h3>
                            <div
                                className="output"
                                dangerouslySetInnerHTML={this.getRawMarkup()}
                            />
                        </Col>
                    </Row>
                    <Link to="/" className="btn btn-light" activeStyle>
                        Back to home
                    </Link>
                    <button type="submit" className="btn btn-light">Create Set</button>
                </form>

            </div>
        )
    }

}