import React, { Component, PropTypes } from 'react'
import ChatMessage from './ChatMessage'

export default class ChatMessageList extends Component {
    render() {
        return (
            <ul>
                {this.props.chats.map((chat, index) =>
                    <ChatMessage {...chat}
                        key={index}
                    />
                )}
            </ul>
        )
    }
}