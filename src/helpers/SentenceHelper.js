import React from "react";
import { Row, Col } from "react-bootstrap";

export default function SentenceHelper({ parent_set, text, image_url, sound_clip }) {
    return(
        <div className="message">
            <p>{text}</p>
            <img src={image_url}/>
            <div>
                <audio controls>
                    <source src={sound_clip} type="audio/mp3"/>
                </audio>
            </div>
        </div>
    )
}