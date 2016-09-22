import React, { Component, PropTypes } from 'react'
import Chat from './Chat'

export default class ChatList extends Component {
    render() {
        return (
            <ul>
                {this.props.chats.map((chat, index) =>
                    <Chat {...chat}
                        key={index}
                    />
                )}
            </ul>
        )
    }
}