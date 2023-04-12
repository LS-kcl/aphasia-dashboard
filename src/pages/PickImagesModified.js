import React from "react";
import axios from "axios";
import ImageSelectionHelper from "../helpers/ImageSelectionHelper";
import { Link } from "react-router-dom";
import { useParams } from "react-router-dom";
axios.defaults.withCredentials = true;

class PickImagesModified extends React.Component {
    state = {
        pageid: 0,
        sentences: []
    }

    componentDidMount() {
        // Get id value from URL to make request
        let { pageid } = this.props.params;

        // Make request for page based on pageid
        axios.get('/api/view_set_and_images/' + pageid)
            .then(res =>{
                const responsejson = res.data;
                this.setState({
                    pageid: responsejson.id, 
                    sentences: responsejson.child_sentences 
                })
            })

        // Request images to be generated for each 
    }

    ToggleImageSelected(generated_image_id){
        let requesturl = '/api/toggle_image_selected/' + generated_image_id
        axios.put(requesturl, {'withCredentials': true })
            // .then(res => {
            //     // Update page with new data
            //     const responsejson = res.data;
            //     this.setState({
            //         pageid: responsejson.id, 
            //         sentences: responsejson.child_sentences 
            //     })
            // })

        axios.get('/api/view_set_and_images/' + this.state.pageid)
            .then(res =>{
                const responsejson = res.data;
                this.setState({
                    pageid: responsejson.id, 
                    sentences: responsejson.child_sentences 
                })
            })
    }

    render() {
        return (
            <div>
                {
                    this.state.sentences
                        .map(sentence =>
                            <div className="set col-sm-12 col-md-6 offset-md-3">
                                {
                                    // Check image selection is not null before generating selection:
                                    sentence.child_image_selections ? <p>{sentence.child_image_selections.prompt}</p> : <p>The image selection has not been generated</p>
                                }
                                <div className="row">
                                {
                                    // Only render image if exists
                                    sentence.child_image_selections ? sentence.child_image_selections.child_images?.map(data =>
                                        data.selected ? 
                                        <div className="col selected-border"><img src={data.url} onClick={e => this.ToggleImageSelected(data.id)}/></div> :
                                        <div className="col"><img src={data.url} onClick={e => this.ToggleImageSelected(data.id)}/></div>
                                    ) : null
                                }
                                </div>
                                <button className="btn btn-light">Generate new images</button>
                                <button className="btn btn-light">Switch to stock images</button>
                            </div>
                        )
                }
                    <Link to={"/view_page/" + this.state.pageid} className="btn btn-light" activeStyle>
                        Create page
                    </Link>
                    <Link to="/" className="btn btn-light" activeStyle>
                        Back to home
                    </Link>
            </div>
        )
    }
}

// See: https://stackoverflow.com/questions/58548767/react-router-dom-useparams-inside-class-component
function withParams(Component) {
    return props => <Component {...props} params={useParams()} />;
}


// Helper function required to pass params
export default withParams(PickImagesModified)