import React from "react";
import axios from "axios";
import SentenceHelper from "../helpers/SentenceHelper";
import { Link } from "react-router-dom";
import { useParams } from "react-router-dom";
axios.defaults.withCredentials = true;
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'x-csrftoken'

class ViewPage extends React.Component {
    state = {
        setid: 0,
        sentences: [],
        title: "",
        public: false
    }

    componentDidMount() {
        // Get id value from URL to make request
        let { pageid } = this.props.params;

        // Make request for page based on pageid
        axios.get('/api/view_set/' + pageid, {'withCredentials': true })
            .then(res =>{
                const responsejson = res.data;
                this.setState({
                    setid: responsejson.id, 
                    sentences: responsejson.child_sentences,
                    title: responsejson.title,
                    public: responsejson.public 
                })
            })
    }

    togglePublic = event => {
        let { pageid } = this.props.params;

        // Make request to toggle visibility API
        axios.put('/api/toggle_set_visibility/' + pageid, {'withCredentials': true })
            .then(res =>{
                const responsejson = res.data;
                this.setState({
                    public: responsejson.public 
                })
            })
    
    }

    render() {
        return (
            <>
                <div>
                    <h1>{this.state.title}</h1>
                    {
                        this.state.public ? 
                        <button onClick={this.togglePublic}>Make Private</button> :
                        <button onClick={this.togglePublic}>Make Public</button>
                    }
                </div>

                <div>
                    {
                        this.state.sentences
                            .map(sentence =>
                                    <SentenceHelper 
                                        parent_set={this.state.parentid}
                                        text={sentence.text}
                                        image_url={sentence.image_url}
                                        sound_clip={sentence.sound_clip}
                                    />
                            )
                    }

                    <Link to="/" activeStyle>
                        Back to home
                    </Link>
                </div>
            </>
        )
    }
}

// See: https://stackoverflow.com/questions/58548767/react-router-dom-useparams-inside-class-component
function withParams(Component) {
    return props => <Component {...props} params={useParams()} />;
}

// Helper function required to pass params
export default withParams(ViewPage)