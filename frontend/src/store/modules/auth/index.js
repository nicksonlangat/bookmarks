
import AuthApi from '@/services/Auth'
import Api from '@/services/Api'
const state = {
  user: null
}

const mutations = {
  SAVE_TOKEN (payload) {
    localStorage.setItem("navis", JSON.stringify(payload))
  },
  SET_USER(state, payload){
    state.user = payload
  }
}

const actions = {
    async loginUser({ commit }, { payload, cb }) {
        return await AuthApi()
            .post('accounts/login/', payload)
            .then((response) => {
                // commit('SAVE_TOKEN', response.data)
                localStorage.setItem("navis", JSON.stringify(response.data))
                if (cb) {
                    cb(response.data)
                }
                return response.data
            })
            .catch((error) => {
                return Promise.reject(error)
            })
      },
      
      async changePassword({ commit }, { payload, cb }) {
      return await Api()
        .patch('/accounts/users/password/change', payload)
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
        },
      
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
