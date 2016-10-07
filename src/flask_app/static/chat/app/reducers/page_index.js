import { CHANGE_PAGE } from '../constants/ActionTypes'
import { PAGE_LOGIN } from '../constants/PageIndex'

export function page_index(state = PAGE_CHAT, action) {
    switch (action.type) {
        case CHANGE_PAGE:
            return action.page_index;
        default:
            return state
    }
}
