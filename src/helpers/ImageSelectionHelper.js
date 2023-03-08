import React from "react";
import { Row, Col } from "react-bootstrap";

export default function ImageSelectionHelper({ prompt, images }) {
    return (
        <Row>
            <Col>
                <div className="text">
                    <p>
                        {prompt}
                    </p>
                </div>
                <div className="images">
                    {
                        images
                            .map(storedUrl =>
                                <img src={storedUrl}/>
                            )
                    }
                </div>
            </Col>
        </Row>
    )
}

// TODO: 
// Take in sentence as a parameter too
// Add onClick request to update the sentence image
// Display sentence details above, and imageSelection details below
