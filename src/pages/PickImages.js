import React from "react";
import axios from "axios";
import ImageSelectionHelper from "../helpers/ImageSelectionHelper";
import IDBasedImageSelectionHelper from "../helpers/IDBasedImageSelectionHelper"
import { Link } from "react-router-dom";
import { useParams } from "react-router-dom";
axios.defaults.withCredentials = true;

class PickImages extends React.Component {
    state = {
        pageid: 0,
        sentences: [],
        isLoading: true
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

    render() {
        if (this.state.isLoading) {
            <div/>
        }
        return (
            <div>
                {
                    this.state.sentences
                        .map(sentence =>
                            <div className="set col-sm-12 col-md-6 offset-md-3">
                            <IDBasedImageSelectionHelper 
                                sentence_id={sentence.id}
                            />
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
export default withParams(PickImages)