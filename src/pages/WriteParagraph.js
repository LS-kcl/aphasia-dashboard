import React from "react";
import axios from "axios";
import { Remarkable } from "remarkable";

import { Container, Row, Col } from "react-bootstrap";

export default class SetAdd extends React.Component {
    constructor(props){
        super(props);
        this.markdown = new Remarkable();
        this.handleChange = this.handleChange.bind(this);
        this.state = { text: '' };
    }

    getRawMarkup() {
        return { __html: this.markdown.render(this.state.text) }
    }

    handleChange = event => {
        this.setState({ text: event.target.value })
    }

    handleSubmit = event => {
        event.preventDefault()

        const text = this.state.text

        axios.post('/Some/url/here', {text})
        .then(res => {
            console.log(res)
            console.log(res.data)
        })
    }

    render() {
        return (
            <Container>
                <Row>
                    <Col>
                        <h3> Enter your text here: </h3>
                        <textarea 
                            id="userInput"
                            onChange={this.handleChange}
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
            </Container>
        )
    }

}