import React from "react";
import { Row, Col } from "react-bootstrap";

export default function SentenceHelper({ parent_set, text, image_url}) {
    return(
        <div>
            <p>{text}</p>
            <img src={image_url}/>
        </div>
    )
}