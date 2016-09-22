import { combineReducers } from 'redux'
import { chats } from './chats'
import {change_page} from './change_page'

const chatApp = combineReducers({
    change_page,
    chats
});

export default chatApp