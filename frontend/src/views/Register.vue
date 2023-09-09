<template>
<div class="flex flex-col items-center text-stone-300 font-base justify-center">
    <h3 class="mt-12 text-3xl">Create your account</h3>

    <form class="w-1/3 mt-10 flex flex-col gap-8">
        <div class="flex flex-col gap-2 text-stone-300">
            <label for="">First name</label>
            <input v-model="user.first_name" type="text" class="bg-[#111111] border border-stone-900 px-6 py-2 rounded-md focus:outline-none focus:right-0">
        </div>
        <div class="flex flex-col gap-2 text-stone-300">
            <label for="">Last name</label>
            <input v-model="user.last_name" type="text" class="bg-[#111111] border border-stone-900 px-6 py-2 rounded-md focus:outline-none focus:right-0">
        </div>
        <div class="flex flex-col gap-2 text-stone-300">
            <label for="">Email</label>
            <input v-model="user.email" type="email" class="bg-[#111111] border border-stone-900 px-6 py-2 rounded-md focus:outline-none focus:right-0">
        </div>
        <div class="flex flex-col gap-2 text-stone-300">
            <label for="">Password</label>
            <input v-model="user.password" type="password" class="bg-[#111111] px-6 py-2 rounded-md border border-stone-900 focus:outline-none focus:right-0">
        </div>
        <button @click.prevent="submitNewUser" class="bg-[#6c53cd] rounded-md text-stone-100 py-2">Register</button>
        <div class="flex justify-center text-stone-500 underline"><a href="/login">Already have an acount?</a></div>
    </form>
</div>
</template>

<script>
import {
    mapActions
} from 'vuex'
export default {
    name: 'Register',
    data() {
        return {
            user: {
                first_name: "",
                last_name: "",
                email: "",
                password: ""
            }
        }
    },
    methods: {
        ...mapActions({
            createUser: 'createUser'
        }),
        submitNewUser() {
            this.createUser({
                payload: this.user,
                cb: (() => {
                    this.$router.push({
                        "name": "login"
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
