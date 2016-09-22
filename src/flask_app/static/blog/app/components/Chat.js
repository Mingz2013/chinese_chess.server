import React, { Component, PropTypes } from 'react'

export default class Chat extends Component {
    render() {
        return (
            <li>
                {this.props.text}
            </li>
        )
    }
}