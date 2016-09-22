import { combineReducers } from 'redux'
import { chats } from './chats'
import {page_type} from './page_type'

const rootReducer = combineReducers({
    page_type,
    chats
});

export default rootReducer