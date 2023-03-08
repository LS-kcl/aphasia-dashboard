import React from "react";
import axios from "axios";
import SentenceHelper from "../helpers/SentenceHelper";
import { Link } from "react-router-dom";

export default class ViewPage extends React.Component {
    state = {
        parentid: 0,
        sentences: []
    }

    componentDidMount() {
        axios.get('api/view_set/100')
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