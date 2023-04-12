import React from "react";
import axios from "axios";
axios.defaults.withCredentials = true;

// This takes a child_image_selections object that can be null
// Otherwise contains prompt, images, and sentenceid
class IDBasedImageSelectionHelper extends React.Component {
    state = {
        sentenceid: 0,
        prompt: "",
        child_images: null
    }

    componentDidMount() {
        let { sentence_id } = this.props.sentence_id;

        // Make request for page based on sentence_id passed in
        axios.get('/api/view_sentence/' + sentence_id)
            .then(res =>{
                const responsejson = res.data;
                this.setState({
                    sentence_id: sentence_id,
                    prompt: responsejson.prompt, 
                    child_images: responsejson.child_images
                })
            })
    }

    render() {
        return (
        <>
            {
                // Check image selection is not null before generating selection:
                this.state.prompt ? <p>{this.state.prompt}</p> : <p>The image selection has not been generated</p>
            }
            <div className="row">
            {
                // Only render image if exists
                this.state ? this.state.child_images?.map(data =>
                    data.selected ? 
                    <div className="col selected-border"><img src={data.url} onClick={e => ToggleImageSelected(data.id)}/></div> :
                    <div className="col"><img src={data.url} onClick={e => ToggleImageSelected(data.id)}/></div>
                ) : null
            }
            </div>
            <button className="btn btn-light">Generate new images</button>
            <button className="btn btn-light">Switch to stock images</button>
        </>
    )}
}

function ToggleImageSelected(generated_image_id){
    let requesturl = '/api/toggle_image_selected/' + generated_image_id
    axios.put(requesturl, {'withCredentials': true })
        .then(res => {
            // Do nothing, selected should already be bound
        })
}

export default IDBasedImageSelectionHelper;