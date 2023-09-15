<template>
<div class="container font-base mx-auto">

    <div class="mx-4 lg:mx-0 flex justify-between items-center mt-5 text-stone-300">
        <div class="flex flex-col gap-2">
            <h3 class="text-2xl">Hi, {{ user?.first_name }} {{ user?.last_name }}</h3>
            <p class="text-stone-400">{{ date }}</p>
        </div>
        <button @click="logoutUser" class="bg-[#6c53cd] text-stone-100 px-8 py-1.5 rounded-md">
            Logout
        </button>
    </div>
    <Notification />

    <div class=" mx-4 lg:mx-0 flex-col gap-4 lg:gap-0 lg:flex-row flex mt-8 justify-between items-center text-stone-300">
        <div class="w-full lg:w-1/2 relative">
            <input @keyup.enter="submitNewColor" v-model="code" type="text" class="bg-[#111111] w-full rounded-lg py-2 pl-5  focus:outline-none focus:ring-0 placeholder:text-stone-400" placeholder="#">
            <svg xmlns="http://www.w3.org/2000/svg" class="absolute top-2.5 right-5" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                <path d="M18 6v6a3 3 0 0 1 -3 3h-10l4 -4m0 8l-4 -4"></path>
            </svg>
        </div>
        <div class="w-full lg:w-1/4 relative">
            <input v-model="text" type="text" class="bg-[#111111] w-full rounded-lg py-2 pl-10  focus:outline-none focus:ring-0 placeholder:text-stone-400" placeholder="Search">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 absolute top-2.5 text-stone-400 left-2 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z" />
            </svg>
        </div>

    </div>

    <div v-if="colors.length" class="mx-4 lg:mx-0 grid lg:grid-cols-4 mt-6 gap-5 gap-y-4">
        <div v-for="color in colors" class="bg-[#111111] flex flex-col gap-8 overflow-hidden text-stone-400 h-44 rounded-lg">
            <div class="flex flex-col ml-5 mr-5 mt-2">
                <div class="flex gap-2 mt-2 justify-center items-center">
                    <span :style="{backgroundColor: color.code}" class=" h-32 w-32 rounded-full"></span>
                </div>
                <div class=" text-stone-400 flex justify-between">
                    <p>{{ color.code }}</p>
                    <div class="flex gap-5">
                        <svg @click="copyColor(color.code)" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 cursor-pointer h-6">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M15.666 3.888A2.25 2.25 0 0013.5 2.25h-3c-1.03 0-1.9.693-2.166 1.638m7.332 0c.055.194.084.4.084.612v0a.75.75 0 01-.75.75H9a.75.75 0 01-.75-.75v0c0-.212.03-.418.084-.612m7.332 0c.646.049 1.288.11 1.927.184 1.1.128 1.907 1.077 1.907 2.185V19.5a2.25 2.25 0 01-2.25 2.25H6.75A2.25 2.25 0 014.5 19.5V6.257c0-1.108.806-2.057 1.907-2.185a48.208 48.208 0 011.927-.184" />
                        </svg>
                        <svg @click="removeColor(color.id)" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 cursor-pointer h-6">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M14.74 9l-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 01-2.244 2.077H8.084a2.25 2.25 0 01-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 00-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 013.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 00-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 00-7.5 0" />
                        </svg>

                    </div>

                </div>
            </div>
        </div>

        <ul v-if="colors.length" class="mt-2 text-sm font-base inline-flex -space-x-px items-center divide-x divide-stone-900">
            <li @click="goToLastPage" :class="previousPage === '' || previousPage == null ? 'text-stone-900' : 'text-stone-300'" class="flex cursor-pointer items-center justify-center px-4 h-10 ml-0 leading-tight bg-[#111111] rounded-l-md">
                Previous
            </li>
            <li v-for="i in totalPages" :class="currentPage == i ? 'text-stone-200' : 'text-stone-700'" class="flex items-center justify-center px-4 h-10 leading-tight bg-[#111111]">
                {{ i }}
            </li>

            <li @click="goToNextPage" :class="nextPage === '' || nextPage == null ? 'text-stone-900' : 'text-stone-300'" class="flex cursor-pointer items-center justify-center px-4 h-10 ml-0 leading-tight bg-[#111111] rounded-r-md">
                Next
            </li>
        </ul>
    </div>
    <div v-else class="mx-4 lg:mx-0 mt-20 lg:text-3xl text-stone-300 flex items-center justify-center">
        <h3>You have not saved any colors yet.</h3>
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
import moment from 'moment'
export default {
    name: 'Colors',
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
            code: ""
        }
    },
    computed: {
        ...mapGetters({
            storedColors: 'getStoredColors',
            storedUser: 'getStoredUser'
        }),
        colors() {
            return this.storedColors.filter((color) => {
                return color.code.toLowerCase().includes(this.text.toLowerCase())
            })
        },
        date() {
            return moment().format('MMMM Do YYYY')
        },
        user() {
            return this.storedUser
        }
    },
    methods: {
        ...mapActions({
            getAllColors: 'getAllColors',
            deleteColor: 'deleteColor',
            createColor: 'createColor',
            updateColor: 'updateColor',
            getUsersMe: 'getUsersMe'
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
        copyColor(code) {
            if (window.isSecureContext && navigator.clipboard) {
                navigator.clipboard.writeText(code)
            } else {
                this.unsecuredCopyToClipboard(code)
            }
            this.emitter.emit("showNotification", {
                "action": "copy",
                "item": "Color"
            })
        },
        submitNewColor() {
            this.createColor({
                payload: {
                    "code": this.code,
                    // "user": this.user.id
                },
                cb: (() => {
                    this.code = ""
                    this.emitter.emit("showNotification", {
                        "action": "add",
                        "item": "Color"
                    })
                    this.init()
                })
            })
        },
        init() {
            this.getAllColors({
                cb: (res) => {
                    this.previousPage = res.previous
                    this.nextPage = res.next
                    this.totalPages = res.total_pages
                    this.currentPage = res.current_page_number
                }
            })
            this.getUsersMe({
                cb: () => {

                }
            })
        },
        formatDate(date) {
            return moment(date).format("MMM Do YY")
        },
        removeColor(id) {
            this.deleteColor({
                uuid: id,
                cb: (() => {
                    this.init()
                    this.emitter.emit("showNotification", {
                        "action": "delete",
                        "item": "Color"
                    })
                })
            })
        },
        logoutUser() {
            localStorage.removeItem("bookmarks")
            localStorage.removeItem("hasPermission")
            this.$router.push({
                "name": "login"
            })
        },
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
