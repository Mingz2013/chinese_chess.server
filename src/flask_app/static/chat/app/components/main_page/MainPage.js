/**
 * Created by zhaojm on 23/09/2016.
 */
import React, { Component, PropTypes } from 'react'

import Chat from './chat/Chat'
import BottomTabs from './BottomTabs'

export default class MainPage extends Component {
    render() {
        //const { dispatch, chats } = this.props;

        return (
            <div>
                <Chat/>
                <BottomTabs />
            </div>
        )
    }
}