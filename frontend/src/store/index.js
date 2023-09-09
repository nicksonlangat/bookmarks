import { createStore } from 'vuex'
import bookmarkModule from './modules/bookmarks'
import authModule from './modules/auth'

export default createStore({
  modules: {
    bookmarkModule,
    authModule
  }
})
