import React from "react";
import axios from "axios";
axios.defaults.withCredentials = true;

export default function ImageSelectionHelper({ prompt, images, sentenceid }) {
    return (
        <>
            <p>
                {prompt}
            </p>
            {
                images?.map(data =>
                    <img src={data.url} onClick={e => SetImageRequest(data.url, sentenceid)}/>
                )
            }
        </>
    )
}

function SetImageRequest(url, sentenceid){
    console.log("Set image function called")
    const data = { image_url: url }
    let requesturl = '/api/set_sentence_image/' + sentenceid
    axios.put(requesturl, { data })
}
// TODO: 
// Take in sentence as a parameter too
// Add onClick request to update the sentence image
// Display sentence details above, and imageSelection details below
