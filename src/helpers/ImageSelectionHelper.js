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
                // Only render image if exists
                image_selection ? image_selection.child_images?.map(data =>
                    <img src={data.url} onClick={e => ToggleImageSelected(data.id)}/>
                ) : null
            }
        </>
    )
}

function ToggleImageSelected(generated_image_id){
    let requesturl = '/api/toggle_image_selected/' + generated_image_id
    axios.put(requesturl, {'withCredentials': true })
        .then(res => {
            // Do nothing, selected should already be bound
        })
}
// TODO: 
// Take in sentence as a parameter too
// Add onClick request to update the sentence image
// Display sentence details above, and imageSelection details below
