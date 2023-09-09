<template>
<div class="flex flex-col items-center text-stone-300 font-base justify-center">
    <h3 class="mt-32 text-3xl">Welcome back</h3>
    <h3 class="mt-5 text-xl text-stone-400">Please log in to continue to your account</h3>
    <form class="w-1/3 mt-10 flex flex-col gap-8">
        <div class="flex flex-col gap-2 text-stone-300">
            <label for="">Email</label>
            <input v-model="user.email" type="email" class="bg-[#111111] border border-stone-900 px-6 py-2 rounded-md focus:outline-none focus:right-0">
        </div>
        <div class="flex flex-col gap-2 text-stone-300">
            <label for="">Password</label>
            <input v-model="user.password" type="password" class="bg-[#111111] px-6 py-2 rounded-md border border-stone-900 focus:outline-none focus:right-0">
            <div class="flex justify-end text-stone-500 underline"><a href="/reset">Forgot password?</a></div>
        </div>
        <button @click.prevent="submitLoginRequest" class="bg-[#6c53cd] rounded-md text-stone-100 py-2">Log in</button>
        <div class="flex justify-center text-stone-500 underline"><a href="/register">Don't have an acount?</a></div>
    </form>
</div>
</template>

<script>
import {
    mapActions
} from 'vuex'
export default {
    name: 'Login',
    data() {
        return {
            user: {
                email: "",
                password: ""
            }
        }
    },
    methods: {
        ...mapActions({
            loginUser: 'loginUser'
        }),
        submitLoginRequest() {
            this.loginUser({
                payload: this.user,
                cb: (() => {
                    this.$router.push({
                        "name": "home"
                    })
                })
            })

        }
    }
}
</script>

<style>
html {
    background-color: #040405;
}
</style>
