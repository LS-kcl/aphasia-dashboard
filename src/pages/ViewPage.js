import React from "react";
import axios from "axios";
import SentenceHelper from "../helpers/SentenceHelper";
import { Link } from "react-router-dom";
import { useParams } from "react-router-dom";

class ViewPage extends React.Component {
    state = {
        parentid: 0,
        sentences: []
    }

    componentDidMount() {
        // Get id value from URL to make request
        let { pageid } = this.props.params;

        // Make request for page based on pageid
        axios.get('/api/view_set/' + pageid)
            .then(res =>{
                const responsejson = res.data;
                this.setState({parentid: 0, sentences: responsejson.child_sentences })
            })
    }

    render() {
        return (
            <div>
                {
                    this.state.sentences
                        .map(sentence =>
                            <SentenceHelper 
                                parent_set={this.state.parentid}
                                text={sentence.text}
                                image_url={"text"}
                            />
                        )
                }

                <Link to="/" activeStyle>
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
export default withParams(ViewPage)