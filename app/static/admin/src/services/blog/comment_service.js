/**
 * Created by zhaojm on 16/11/2016.
 */

import ajax_promise from '../../api/ajax_promise'


class CommentService {
    constructor() {
    }

    add_comment(comment) {
        return ajax_promise({
            type: "POST",
            data: comment,
            url: "/api/blog/comment/add"
        })
    }

    get_comment_list() {
        return ajax_promise({
            type: "GET",
            url: "/api/blog/comment/list"
        })
    }


}

let comment_service = new CommentService();

export default comment_service;