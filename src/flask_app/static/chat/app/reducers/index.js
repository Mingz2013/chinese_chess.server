import { combineReducers } from 'redux'
import { chat_messages } from './chat_messages'
import {page_index} from './page_index'

const rootReducer = combineReducers({
    chat_messages,
    page_index
});

export default rootReducer