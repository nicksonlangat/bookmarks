<template>
<div class="container mx-auto">

    <div class="flex justify-between items-center mt-5 text-stone-300">
        <div class="flex flex-col gap-2">
            <h3 class="text-2xl">Good morning</h3>
            <p class="text-stone-400">Friday, Sept 08</p>
        </div>
        <span class="bg-[#111111] px-2 py-2 rounded-lg">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M6.75 12a.75.75 0 11-1.5 0 .75.75 0 011.5 0zM12.75 12a.75.75 0 11-1.5 0 .75.75 0 011.5 0zM18.75 12a.75.75 0 11-1.5 0 .75.75 0 011.5 0z" />
            </svg>
        </span>
    </div>
    <Notification />

    <div class="flex mt-10 justify-between items-center text-stone-300">
        <div class="w-1/2 relative">
            <input @keyup.enter="submitNewBookmark" v-model="link" type="text" class="bg-[#111111] w-full rounded-lg py-2 pl-5  focus:outline-none focus:ring-0 placeholder:text-stone-400" placeholder="https://">
            <svg xmlns="http://www.w3.org/2000/svg" class="absolute top-2.5 right-5" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                <path d="M18 6v6a3 3 0 0 1 -3 3h-10l4 -4m0 8l-4 -4"></path>
            </svg>
        </div>
        <div class="w-1/4 relative">
            <input v-model="text" type="text" class="bg-[#111111] w-full rounded-lg py-2 pl-10  focus:outline-none focus:ring-0 placeholder:text-stone-400" placeholder="Search">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 absolute top-2.5 text-stone-400 left-2 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z" />
            </svg>
        </div>

    </div>

    <div v-if="bookmarks.length" class="grid grid-cols-4 mt-10 gap-5 gap-y-4">
        <div v-for="bookmark in bookmarks" class="bg-[#111111] flex flex-col gap-12 overflow-hidden text-stone-200 h-32 rounded-lg">
            <div class="flex justify-between items-center ml-5 mr-5 mt-2">
                <div class="flex gap-2 mt-2 items-center">
                    <img v-if="bookmark.thumbnail" class="w-6 h-6 object-cover rounded-full" :src="bookmark.thumbnail" alt="">
                    <svg v-else xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M12 21a9.004 9.004 0 008.716-6.747M12 21a9.004 9.004 0 01-8.716-6.747M12 21c2.485 0 4.5-4.03 4.5-9S14.485 3 12 3m0 18c-2.485 0-4.5-4.03-4.5-9S9.515 3 12 3m0 0a8.997 8.997 0 017.843 4.582M12 3a8.997 8.997 0 00-7.843 4.582m15.686 0A11.953 11.953 0 0112 10.5c-2.998 0-5.74-1.1-7.843-2.918m15.686 0A8.959 8.959 0 0121 12c0 .778-.099 1.533-.284 2.253m0 0A17.919 17.919 0 0112 16.5c-3.162 0-6.133-.815-8.716-2.247m0 0A9.015 9.015 0 013 12c0-1.605.42-3.113 1.157-4.418" />
                    </svg>

                    <h3>{{ bookmark.site_name }}</h3>
                </div>

                <div class="fixed top-52 ml-12 mt-1 w-56 text-right">
                    <Menu as="div" class="relative inline-block text-left">
                        <div>
                            <MenuButton class="inline-flex w-full justify-center text-sm font-medium">
                                <span class="bg-[#191919] px-1.5 py-1.5 rounded-lg">
                                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M6.75 12a.75.75 0 11-1.5 0 .75.75 0 011.5 0zM12.75 12a.75.75 0 11-1.5 0 .75.75 0 011.5 0zM18.75 12a.75.75 0 11-1.5 0 .75.75 0 011.5 0z" />
                                    </svg>
                                </span>
                            </MenuButton>
                        </div>

                        <transition enter-active-class="transition duration-100 ease-out" enter-from-class="transform scale-95 opacity-0" enter-to-class="transform scale-100 opacity-100" leave-active-class="transition duration-75 ease-in" leave-from-class="transform scale-100 opacity-100" leave-to-class="transform scale-95 opacity-0">
                            <MenuItems class="absolute right-0 mt-2 w-40 origin-top-right divide-y divide-gray-100 rounded-md bg-white  shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none">
                                <div class="px-1 py-1">
                                    <MenuItem v-slot="{ active }">
                                    <button @click="editBookmark(bookmark)" :class="[
                  active ? 'bg-violet-500 text-white' : 'text-black',
                  'group flex gap-2 w-full items-center rounded-md px-2 py-2 text-sm',
                ]">
                                        <svg :active="active" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-4 h-4">
                                            <path stroke-linecap="round" stroke-linejoin="round" d="M16.862 4.487l1.687-1.688a1.875 1.875 0 112.652 2.652L6.832 19.82a4.5 4.5 0 01-1.897 1.13l-2.685.8.8-2.685a4.5 4.5 0 011.13-1.897L16.863 4.487zm0 0L19.5 7.125" />
                                        </svg>

                                        Edit
                                    </button>
                                    </MenuItem>
                                    <MenuItem v-slot="{ active }">
                                    <button @click="copyBookmark(bookmark.url)" :class="[
                  active ? 'bg-violet-500 text-white' : 'text-gray-900',
                  'group flex gap-2 w-full items-center rounded-md px-2 py-2 text-sm',
                ]">
                                        <svg :active="active" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-4 h-4">
                                            <path stroke-linecap="round" stroke-linejoin="round" d="M13.19 8.688a4.5 4.5 0 011.242 7.244l-4.5 4.5a4.5 4.5 0 01-6.364-6.364l1.757-1.757m13.35-.622l1.757-1.757a4.5 4.5 0 00-6.364-6.364l-4.5 4.5a4.5 4.5 0 001.242 7.244" />
                                        </svg>

                                        Copy URL
                                    </button>
                                    </MenuItem>
                                </div>
                                <div class="px-1 py-1">

                                    <MenuItem v-slot="{ active }">
                                    <button @click="duplicateBookmark(bookmark.url)" :class="[
                  active ? 'bg-violet-500 text-white' : 'text-gray-900',
                  'group flex w-full gap-2 items-center rounded-md px-2 py-2 text-sm',
                ]">
                                        <svg :active="active" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-4 h-4">
                                            <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 17.25v3.375c0 .621-.504 1.125-1.125 1.125h-9.75a1.125 1.125 0 01-1.125-1.125V7.875c0-.621.504-1.125 1.125-1.125H6.75a9.06 9.06 0 011.5.124m7.5 10.376h3.375c.621 0 1.125-.504 1.125-1.125V11.25c0-4.46-3.243-8.161-7.5-8.876a9.06 9.06 0 00-1.5-.124H9.375c-.621 0-1.125.504-1.125 1.125v3.5m7.5 10.375H9.375a1.125 1.125 0 01-1.125-1.125v-9.25m12 6.625v-1.875a3.375 3.375 0 00-3.375-3.375h-1.5a1.125 1.125 0 01-1.125-1.125v-1.5a3.375 3.375 0 00-3.375-3.375H9.75" />
                                        </svg>

                                        Duplicate
                                    </button>
                                    </MenuItem>

                                </div>

                                <div class="px-1 py-1">
                                    <MenuItem v-slot="{ active }">
                                    <button @click="removeBookmark(bookmark.id)" :class="[
                  active ? 'bg-violet-500 text-white' : 'text-gray-900',
                  'group flex w-full gap-2 items-center rounded-md px-2 py-2 text-sm',
                ]">
                                        <svg :active="active" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-4 h-4">
                                            <path stroke-linecap="round" stroke-linejoin="round" d="M14.74 9l-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 01-2.244 2.077H8.084a2.25 2.25 0 01-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 00-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 013.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 00-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 00-7.5 0" />
                                        </svg>

                                        Delete
                                    </button>
                                    </MenuItem>
                                </div>
                            </MenuItems>
                        </transition>
                    </Menu>
                </div>
            </div>
            <div class="ml-5 text-stone-400">
                <h3>{{ bookmark.url }}</h3>
            </div>
        </div>
    </div>
    <div v-else class=" mt-20 text-3xl text-stone-300 flex items-center justify-center">
        <h3>You have not saved any bookmarks yet.</h3>
    </div>
</div>
</template>

<script>
import {
    mapActions,
    mapGetters,
    mapMutations
} from 'vuex';
import Notification from '@/components/Notification.vue';
import {
    Menu,
    MenuButton,
    MenuItems,
    MenuItem
} from '@headlessui/vue'
export default {
    name: 'Bookmarks',
    components: {
        Notification,
        Menu,
        MenuButton,
        MenuItems,
        MenuItem
    },
    data() {
        return {
            text: "",
            totalPages: 0,
            previousPage: "",
            nextPage: "",
            currentPage: "",
            link: "",
            linkCopied: false,
            currentBookmark: null,
        }
    },
    computed: {
        ...mapGetters({
            storedBookmarks: 'getStoredBookmarks'
        }),
        bookmarks() {
            return this.storedBookmarks.filter((bookmark) => {
                return bookmark.title.toLowerCase().includes(this.text.toLowerCase())
            })
        }
    },
    methods: {
        ...mapActions({
            getAllBookmarks: 'getAllBookmarks',
            deleteBookmark: 'deleteBookmark',
            createBookmark: 'createBookmark',
            updateBookmark: 'updateBookmark'
        }),
        ...mapMutations({
            INCREASE_PAGE: 'INCREASE_PAGE',
            DECREASE_PAGE: 'DECREASE_PAGE',
        }),
        goToNextPage() {
            if (this.nextPage != null) {
                this.INCREASE_PAGE()
                this.init()
            }
        },
        goToLastPage() {
            if (this.previousPage != null) {
                this.DECREASE_PAGE()
                this.init()
            }
        },
        editBookmark(bookmark){
          this.link = bookmark.url
          this.currentBookmark = bookmark
        },
        duplicateBookmark(link) {
            this.link = link
            this.submitNewBookmark()
        },
        unsecuredCopyToClipboard(text) {
            const textArea = document.createElement("textarea")
            textArea.value = text
            document.body.appendChild(textArea)
            textArea.focus()
            textArea.select()
            try {
                document.execCommand('copy')
            } catch (err) {
                console.error('Unable to copy to clipboard', err)
            }
            document.body.removeChild(textArea)
        },
        copyBookmark(link) {
            if (window.isSecureContext && navigator.clipboard) {
                navigator.clipboard.writeText(link)
            } else {
                this.unsecuredCopyToClipboard(link)
            }
            this.emitter.emit("showNotification", {
                "action": "copy",
                "item": "Link"
            })
        },
        submitNewBookmark() {
            if(this.currentBookmark == null) {
              this.createBookmark({
                payload: {
                    "url": this.link
                },
                cb: (() => {
                    this.link = ""
                    this.emitter.emit("showNotification", {
                        "action": "add",
                        "item": "Bookmark"
                    })
                    this.init()
                })
            })
            }
            else {
              this.updateBookmark({
                uuid: this.currentBookmark.id,
                payload: {
                    "url": this.link
                },
                cb: (() => {
                    this.link = ""
                    this.emitter.emit("showNotification", {
                        "action": "edit",
                        "item": "Bookmark"
                    })
                    this.init()
                    this.currentBookmark = null
                })
            })
            }
        },
        init() {
            this.getAllBookmarks({
                cb: (res) => {
                    this.previousPage = res.previous
                    this.nextPage = res.next
                    this.totalPages = res.total_pages
                    this.currentPage = res.current_page_number
                }
            })
        },
        formatDate(date) {
            return moment(date).format("MMM Do YY")
        },
        removeBookmark(id) {
            this.deleteBookmark({
                uuid: id,
                cb: (() => {
                    this.init()
                    this.emitter.emit("showNotification", {
                        "action": "delete",
                        "item": "Bookmark"
                    })
                })
            })
        }
    },
    mounted() {
        this.init()
    }
}
</script>

<style>
html {
    background-color: #040405;
}
</style>
