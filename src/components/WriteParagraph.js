import React from "react";
import axios from "axios";

import { Container, Row, Col } from "react-bootstrap";

export default class SetAdd extends React.Component {
    state = {
        text: ''
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
                        <textarea 
                            id="userInput"
                            onChange={this.handleChange}
                            defaultValue={this.state.value}
                        />
                    </Col>
                    <Col>
                        <p>{this.state.text}</p>
                    </Col>
                </Row>
            </Container>
        )
    }

}