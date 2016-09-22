import React, { Component, PropTypes } from 'react'

export default class ChatMessage extends Component {
    render() {
        return (
            <li>
                {this.props.text}
            </li>
        )
    }
}