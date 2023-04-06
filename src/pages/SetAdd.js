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
                <div class="col-md-5 p-lg-5 mx-auto my-5">
                    <h1 className="text-white">Create some content</h1>
                    <p class="lead font-weight-normal">Title your page, enter some text to be made accessible, then watch it pop up as a preview!</p>
                    <input type="text" name="title" placeholder="Enter title here" onChange={this.handleChangeTitle}/>
                    <label className="text-white">
                    </label>
                </div>
                    <Row>
                        <Col>
                            <h3 className="text-white"> Enter your text here: </h3>
                            <textarea 
                                id="userInput"
                                name="text"
                                placeholder="Enter a paragraph or two to be made accessible here"
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