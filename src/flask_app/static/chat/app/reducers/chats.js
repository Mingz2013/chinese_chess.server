import { ADD_CHAT } from '../constants/ActionTypes'

export function chats(state = [], action) {
    switch (action.type) {
        case ADD_CHAT:
            return [
                ...state,
                {
                    text: action.text
                }
            ];
        default:
            return state
    }
}