import axios from 'axios'

export default (content_type = 'application/json') => {
    const token = JSON.parse(localStorage.getItem("bookmarks"))
    
    const Api = axios.create({
        baseURL: process.env.VUE_APP_BASE_URL,
        withCredentials: false,
        headers: {
            Accept: 'application/json',
            'Content-Type': content_type,
            Authorization: `Bearer ${token.access}`
        },
    })
    return Api
}
