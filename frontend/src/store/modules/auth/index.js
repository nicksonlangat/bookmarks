
import AuthApi from '@/services/Auth'
import Api from '@/services/Api'
const state = {
  user: null
}

const mutations = {
  SET_USER(state, payload){
    state.user = payload
  }
}

const actions = {
    async createUser({ commit }, { payload, cb }) {
        return await AuthApi()
            .post('/accounts/register/', payload)
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
    async loginUser({ commit }, { payload, cb }) {
        return await AuthApi()
            .post('accounts/login/', payload)
            .then((response) => {
                localStorage.setItem("bookmarks", JSON.stringify(response.data))
                localStorage.setItem("hasPermission", true)
                if (cb) {
                    cb(response.data)
                }
                return response.data
            })
            .catch((error) => {
                return Promise.reject(error)
            })
      },
      
      async resetPasswordRequest({ commit }, { payload, cb }) {
      return await AuthApi()
        .post('/accounts/password/reset/', payload)
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

      async verifyResetToken({ commit }, { uidb4, token,  cb }) {
        return await AuthApi()
            .get(`/accounts/password-reset/${uidb4}/${token}/`)
            .then((response) => {
                if (cb) {
                    cb(response.data)
                }
                return response.data
            })
            .catch((error) => {
                console.log(error)
            })
        },
        async resetPassword({ commit }, { payload, cb }) {
            return await AuthApi()
              .post('/accounts/new/password/', payload)
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
      async getUsersMe({ commit }, { setResult=true, cb }) {
        return await Api()
            .get('/accounts/users/me')
            .then((response) => {
                if (setResult) {
                    commit('SET_USER', response.data)
                }
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
    getStoredUser: (state) => {
        return state.user
    }
}
const authModule = {
    state,
    mutations,
    actions,
    getters
  }
export default authModule
