
import Api from '@/services/Api'
const state = {
  bookmarks: [],
  pageNumber: 1
}

const mutations = {
  SET_BOOKMARKS (state, payload) {
    state.bookmarks = payload
  },
INCREASE_PAGE(state) {
    state.pageNumber++
  },
  DECREASE_PAGE(state) {
    state.pageNumber--
  }
}

const actions = {
  async createBookmark({ commit }, { payload, cb }) {
    return await Api()
        .post('/bookmarks', payload)
        .then((response) => {
            if (cb) {
                cb(response.data)
            }
            return response.data
        })
        .catch((error) => {
            return Promise.reject(error)
        })
},
  async getAllBookmarks({ commit, state }, { setResult=true, cb }) {
    return await Api()
        .get(`/bookmarks?page=${state.pageNumber}`)
        .then((response) => {
            if (setResult) {
                commit('SET_BOOKMARKS', response.data.results)
            }
            if (cb) {
                cb(response.data)
            }
            return response.data
        })
        .catch((error) => {
            return Promise.reject(error)
        })
},
async updateBookmark({ commit }, { uuid, payload, cb }) {
  return await Api()
      .put(`bookmarks/${uuid}/`, payload)
      .then((response) => {
          if (cb) {
              cb(response.data)
          }
          return response.data
      })
      .catch((error) => {
          return Promise.reject(error)
      })
},
async deleteBookmark({ commit }, { uuid, cb }) {
  return await Api()
      .delete(`bookmarks/${uuid}/`)
      .then((response) => {
          if (cb) {
              cb(response.data)
          }
          return response.data
      })
      .catch((error) => {
          return Promise.reject(error)
      })
}

}
const getters = {
  getStoredBookmarks: (state) => {
    return state.bookmarks
},
}

const bookmarkModule = {
    state,
    mutations,
    actions,
    getters
  }
export default bookmarkModule
