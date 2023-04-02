import React from "react";
import axios from "axios";
axios.defaults.withCredentials = true;

// This takes a child_image_selections object that can be null
// Otherwise contains prompt, images, and sentenceid
export default function ImageSelectionHelper({ image_selection }) {
    return (
        <>
            {
                // Check image selection is not null before generating selection:
                image_selection ? <p>{image_selection.prompt}</p> : <p>The image selection has not been generated</p>
            }
            {
                image_selection ? image_selection.images?.map(data =>
                    <img src={data.url} onClick={e => SetImageRequest(data.url, image_selection.sentenceid)}/>
                ) : <p>No image could be generated</p>
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
