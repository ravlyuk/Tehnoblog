import fetch from '../common/fetch';

export const getArticles = (backendUrl, id, pageNumber) => {
    if (id) {
        return fetch(
            `${backendUrl}/rubric/${id}/?page=${pageNumber}`
        )
    } else {
        return fetch(
            `${backendUrl}/article/?page=${pageNumber}`
        )
    }

}

export const getSingleArticle = (backendUrl, id) => {
    return fetch(
        `${backendUrl}/article/${id}/`
    )
}

export const getRubrics = (backendUrl) => {
    return fetch(
        `${backendUrl}/rubric/?limit=20`
    )
}

// export const getArticlesByRubric = (backendUrl, rubricId, pageNumber) => {
//     return fetch(
//         `${backendUrl}/rubric/${rubricId}/?page=${pageNumber}`
//     )
// }
