/**
 * Created by zhaojm on 23/09/2016.
 */
import React, { Component, PropTypes } from 'react'

import ChatMessageList from './ChatMessageList'
import AddChatMessage from './AddChatMessage'

export default class Chat extends Component {
    render() {
        return (
            <div>
                <ChatMessageList chats={chats}/>
                <AddChatMessage onAddClick={text => dispatch(addChat(text))}/>
            </div>
        )
    }
}