import React, { Component, PropTypes } from 'react'
import { connect } from 'react-redux'
import { addChat } from '../actions'
import AddChat from '../components/AddChat'
import ChatList from '../components/ChatList'

class App extends Component {
    render() {
        const { dispatch, chats } = this.props;
        return (
            <div>
                <ChatList chats={chats}/>
                <AddChat onAddClick={text => dispatch(addChat(text))}/>
            </div>
        )
    }
}

let mapStateToProps = (state) => ({
    chats: state.chats
});

export default connect(mapStateToProps)(App)